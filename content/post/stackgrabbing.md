---
title: StackGrabbing
date: 2014-02-21T08:45:09.000Z
---
Grabbing the Stack for Fun & Profit
===================================

So I\'m at a work, trying to track down some memory leaks in a
long-running VC++ application (actually a COM object DLL out the back of
a .NET web service - you don\'t need to know that bit). No problem,
I\'ll use the Microsoft C Run-Time library memory debugging features.. a
quick read / web search later, I have the necessary incantation in a
common code header:

     #define _CRTDBG_MAP_ALLOC
     #include <stdlib.h>
     #include <crtdbg.h>
     #define new new(_NORMAL_BLOCK,__FILE__,__LINE__)

..all goes well, the application terminates and I get a dump file of
leaked memory blocks: 34MB of text, with very few file and line numbers.
Of those entries that do provide file and line numbers, they\'re all
just a few places, buffer management classes that could be called from
anywhere. Back to square one.

OK, so I need more context, in particular I need to see the stack when
those allocations are made. No problem, I can use a [debug memory
allocation hook
function](http://msdn.microsoft.com/en-us/library/z2zscsc2.aspx "wikilink"),
take a stack back trace for each alloc, remove it for each free then
dump what\'s left at the end.

Attempt 1: [StackWalker](StackWalker "wikilink")
------------------------------------------------

So - how to grab a stack back trace? I first came across some excellent
but rather involved code from Jochen Kalmbach:
<http://stackwalker.codeplex.com/> which he wrote primarily for printing
a crash dump stack trace with lots of extra info.

This turns out to be pretty easy to use, but rather slow, mostly because
it does symbol lookups while walking the stack. I\'m seeing \~20 million
allocations during a test run, and !StackWalker is tracing at about
100/sec, so a test run would take 200k secs or about 2.3 days. Try
again.

Attempt 2: [CaptureStackBackTrace](CaptureStackBackTrace "wikilink")
--------------------------------------------------------------------

My Google fu improved after attempt 1, and I found
[CaptureStackBackTrace](http://msdn.microsoft.com/en-us/library/windows/desktop/bb204633%28v=vs.85%29.aspx "wikilink"),
a kernel/RTL function that does exactly what it says on the tin -
fabulous and fast, no symbol lookups or callbacks to read process
memory, using this made no discernible difference to memory allocation
speed - winner!

CRT Oops
--------

So now I can run a test - result: \~20 million allocations, followed by
zero frees. Nothing. Not one. That can\'t be right can it?

Back to the debugger to trace what\'s going on in the memory allocation
hook function where I\'m supposed to be matching allocation requests
with free\'s and removing those from the list to print out. Turns out
that when Microsoft wrote the debug memory library they chose to not
provide the hook function with any useful information when callers free
memory blocks, so I\'m unable to associate free\'s with allocs. Genius.
A little more digging and some bodgery results in me being able to
extract the allocation request ID and record memory leakage with stack
traces like this:

    #define _CRTDBG_MAP_ALLOC
    #include <stdlib.h>
    #include <crtdbg.h>
    #include <DbgHelp.h>

    // stolen from dbgint.h - because M$ in their wisdom don't provide matching request serial numbers between alloc/free hook calls. Sheesh.
    #define nNoMansLandSize 4
    typedef struct _CrtMemBlockHeader
    {
            struct _CrtMemBlockHeader * pBlockHeaderNext;
            struct _CrtMemBlockHeader * pBlockHeaderPrev;
            char *                      szFileName;
            int                         nLine;
    #ifdef _WIN64
            /* These items are reversed on Win64 to eliminate gaps in the struct
             * and ensure that sizeof(struct)%16 == 0, so 16-byte alignment is
             * maintained in the debug heap.
             */
            int                         nBlockUse;
            size_t                      nDataSize;
    #else  /* _WIN64 */
            size_t                      nDataSize;
            int                         nBlockUse;
    #endif  /* _WIN64 */
            long                        lRequest;
            unsigned char               gap[nNoMansLandSize];
            /* followed by:
             *  unsigned char           data[nDataSize];
             *  unsigned char           anotherGap[nNoMansLandSize];
             */
    } _CrtMemBlockHeader;
    #define pbData(pblock) ((unsigned char *)((_CrtMemBlockHeader *)pblock + 1))
    #define pHdr(pbData) (((_CrtMemBlockHeader *)pbData)-1)

    // require dbghelp.lib for SymXX() calls
    #pragma comment(lib, "dbghelp.lib")

    ...

    // collect stack traces during allocation, remove when free'd
    static int maxreq=20000000;
    static ULONG skipframes=5;
    static ULONG maxframes=10;
    typedef struct {
        PVOID trc[10];
        ULONG len;
        ULONG cnt;
    } stack_t;
    static stack_t stacks[20000000];

    static volatile BOOL inWalk = FALSE;
    static long acount = 0;
    int __cdecl allochook(int type, void *usr, size_t size, int block, long req, const unsigned char *file, int line) {
        wchar_t msg[80];
        if (inWalk) // ignore recursive requests
            return TRUE;
        inWalk = TRUE;
        acount++;
        if (acount%10000==0) {
            wsprintf(msg, L"%ld\n", acount);
            OutputDebugString(msg);
        }
        if (req<maxreq) {
            DWORD hash;
            switch (type) {
            case _HOOK_ALLOC:
                // insert into map - alert collisions
                if (0==stacks[req].len)
                    stacks[req].cnt=1;
                else
                    stacks[req].cnt++;
                stacks[req].len=CaptureStackBackTrace(skipframes, maxframes, stacks[req].trc, &hash);
                if (stacks[req].len>maxframes) {
                    DebugBreak();
                }
                break;
            case _HOOK_REALLOC:
                // update/insert into map - may collide
                stacks[req].len=CaptureStackBackTrace(skipframes, maxframes, stacks[req].trc, &hash);
                if (stacks[req].len>maxframes) {
                    DebugBreak();
                }
                break;
            case _HOOK_FREE:
                // AWOOGA! AWOOGA!! HIDEOUS BODGE ALERT!!! Recover request ID from CRT debug memory header because
                // Microsloth DO NOT PROVIDE IT IN THE HOOK FUNCTION CALL. Numpties.
                if (usr==NULL) {
                    OutputDebugString(L"NULL [[UserData]] in free hook\n");
                    DebugBreak();
                }
                req = pHdr(usr)->lRequest;
                // remove from map - alert missing entries
                if (0!=stacks[req].len) {
                    stacks[req].len=0;
                } else {
                    wsprintf(msg, L"free without alloc ID: %d\n", req);
                    OutputDebugString(msg);
                }
                break;
            }
        } else {
            OutputDebugString(L"Oops: out of request array!");
            DebugBreak();
        }
        inWalk = FALSE;
        return TRUE;
    }
    static void dumpstacks(_HFILE hFile) {
        char buf[4096];
        DWORD nw;
        int cnt=0;
        HANDLE hProc = [[GetCurrentProcess]]();
        wcstombs(buf, path, wcslen(path));
        SymInitialize(hProc, buf, TRUE);
        wsprintfA(buf, "------ stacks\r\n");
        WriteFile(hFile, buf, strlen(buf), &nw, NULL);
        for (int req=0; req<maxreq; req++) {
            if (0!=stacks[req].len) {
                int o;
                wsprintfA(buf, "{%d/%d}: ", req, stacks[req].cnt);
                o=strlen(buf);
                for (USHORT stk=0; stk<stacks[req].len && o<4080; stk++) {
                    char tmp[256];
                    char tmp2[sizeof(SYMBOL_INFO)+256] = {0};
                    SYMBOL_INFO *pSym = (SYMBOL_INFO *)tmp2;
                    pSym->MaxNameLen = 255;
                    pSym->SizeOfStruct = sizeof(SYMBOL_INFO);
                    if (SymFromAddr(hProc, (DWORD64)stacks[req].trc[stk], 0, pSym))
                        wsprintfA(tmp, "%s (%08x),", pSym->Name, pSym->Address);
                    else
                        wsprintfA(tmp, "%08x,", stacks[req].trc[stk]);
                    strcpy(buf+o, tmp);
                    o+=strlen(tmp);
                }
                WriteFile(hFile, buf, strlen(buf), &nw, NULL);
                WriteFile(hFile, "\r\n", 2, &nw, NULL);
                ++cnt;
            }
            if (req%1000==0) {
                wsprintfA(buf, "%d/%d\n", cnt, req);
                OutputDebugStringA(buf);
            }
        }
    }

    ...

    int main() {
    ...
        memset(&stacks, 0, maxreq*sizeof(stack_t));
        _CRT_ALLOC_HOOK oldHook = _CrtSetAllocHook(allochook);
    ...
        hFile = [[CreateFile]](L"leaks.txt", GENERIC_WRITE, FILE_SHARE_READ, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
        _CrtSetReportMode(_CRT_WARN, _CRTDBG_MODE_FILE);
        _CrtSetReportMode(_CRT_ERROR, _CRTDBG_MODE_FILE);
        _CrtSetReportMode(_CRT_ASSERT, _CRTDBG_MODE_FILE);
        _CrtSetReportFile(_CRT_WARN, hFile);
        _CrtSetReportFile(_CRT_ERROR, hFile);
        _CrtSetReportFile(_CRT_ASSERT, hFile);
        OutputDebugString(L"Dumping stacks\n");
        dumpstacks(hFile);
        OutputDebugString(L"Dumping memory leaks\n");
        _CrtDumpMemoryLeaks();
        CloseHandle(hFile);
        return 0;
    }

..fun eh? But this at least works (whilst eating \~1GB of RAM for the
tracing buffer!).

Leakage Found!
--------------

After all that entertainment, I finally had \~180k memory blocks that
weren\'t free\'d on program termination, this time with stack traces,
all with a common ancestor method - victory is mine! I won\'t bore you
with the details of the bug (besides it\'s proprietary code from work),
but I will say that ATL COM objects are ugly voodoo, and rolling your
own makes stuff much clearer (and not dependant on the paid for version
of Visual Studio).
