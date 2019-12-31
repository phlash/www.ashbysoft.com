---
title: RivendellHacking
date: 2011-01-31T19:01:07.000Z
---
Rivendell Hacking
=================

Open source software is great, even when it has faults, since one can
fix it oneself and return the patch to the community right? Well almost,
here\'s what I\'ve been up to with the play-out software used at the
local community radio station <http://www.felixstoweradio.co.uk>:

Win32 Binary Fixes
------------------

### Short story

It seems none of the Rivendell developers are interested or able to
build Win32 binaries at the moment, so I had to patch the binary program
using IDA Pro to prevent a crash when creating new logs.

Get the patched file here: <attachment:rdlogedit2.exe>

### Long story

About a year ago we installed the Windows binaries to allow our editing
/ production teams to create play lists from the comfort of their
desktop(s) in the station office, or indeed at home. Unfortunately we
found that it crashes when attempting to create a new play list (aka a
\'log\'): so I grabbed the source, a helpful stack dump from wine and
settled down to fix the fault. The problem wasn\'t hard to find, a
simple null pointer dereference because the Win32 version doesn\'t
support multiple users, but someone forgot and referenced the currently
logged in user name variable. All I had to do now was build a fresh
binary and test it - this is where it all came unstuck as for some
reason the developers had chosen to use a *closed source* version of QT
(3.21) on Win32, so I had no means to rebuild the binary. Never mind,
I\'ll just post the patch to the developers mailing list and ask them to
rebuild it. I was duly thanked for finding the problem and lo! a new
version of the source code appeared with the fix - but *no Windows
binaries* :(

I waited for 6 months, pestered the developers slightly and waited some
more - still no new binaries. It seems whoever had the right build tools
and libraries (ie: a QT3.21 license) has gone away. So now I have to
choose between trying to port everything to QT4 (which is open source on
Win32), as suggested *may* be possible on the Wiki, or do something ugly
- patch the binary :)

Well I chose the later since it was going to be quicker and we need it
working now: a brief sojourn with IDA Pro, and the excellent advice from
[Marco
Ramilli](http://marcoramilli.blogspot.com/2011/01/how-to-patch-binary-with-ida-pro.html "wikilink")
did the trick, overwriting the pointer reference with nop instructions
and inserting a reference to the constant user name instead.
Surprisingly this *just worked*. The fixed file is attached above.
