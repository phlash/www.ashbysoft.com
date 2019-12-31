---
title: ScopeHacking
date: 2014-04-18T18:50:26.000Z
---
Have DSO, Will Hack :)
----------------------

I\'ve got a lot of stuff in the house (that I should probably chuck, but
hey), including a [Netgem
iPlayer](http://www.radioandtelly.co.uk/iplayer.html "wikilink") and
it\'s associated infra-red full qwerty keyboard. The iPlayer unit is
pretty much useless now, but the keyboard might be fun as a remote for
an under-TV PC, I just need to know the protocol to program
[LIRC](http://www.lirc.org/ "wikilink")..

So how to decode an IR protocol? Well, I\'ve got a [Digital Storage
Oscilloscope](http://www.rapidonline.com/Test-Measurement/Owon-Oscilloscope-25MHz-2-Channel-Colour-85-2792 "wikilink"),
and found a photo transistor in the box of bits - hooking them up with a
couple of resistors for bias and a 5v supply (USB cable) gets me an IR
receiver:

This happened to be pointing at my dimmable lights when connected, which
showed me a nice 100Hz hum :-)

A bit of fiddling with the controls and I can now detect the signal
coming from the keyboard, a pulse train of IR carrier bursts at 38kHz
(the usual), with variable width pulses in blocks repeated at intervals
while I hold a key down.

Part 1: Pulse timing
--------------------

I adjusted the \'scope such that one pulse train block fits into the
screen width, set the trigger point at the left edge of the screen and
selected single capture mode, then hit \'Space\' and grabbed the pulse
train into storage (all timing in milliseconds):

\|\| on \|\| 2.4 \|\| \|\| 0.8 \|\| \|\| 1.6 \|\| \|\| 0.8 \|\| \|\| 3.2
\|\| \|\| 2.4 \|\| \|\| off\|\| \|\| 0.8 \|\| \|\| 0.8 \|\| \|\| 0.8
\|\| \|\| 0.8 \|\| \|\| 2.4 \|\| \|\|

Hmmn. Looks like everything is a multiple of 0.8 msecs - so let\'s
convert those timings to bits and see if it looks like a serial
protocol:

\|\| Space \|\| 111010110101111000111 \|\| 21 bits? Not sure, let\'s try
another key \|\| \|\| Menu \|\| 11101011010100100111 \|\| 20 bits? Less
sure now, try another one.. \|\| \|\| News \|\| 11101011010111001111
\|\| 20 bits again. First 11/12 are the same.. \|\|

If this was using partiy and start/stop bits (sensible given the
unreliable IR carrier), there should be 11 bits/byte, which fits in with
the first 11/12 bits being the same (address byte followed by keycode
perhaps?). Let\'s divide the bits up, include a final stop bit (0) and
check if a parity bit works:

\|\| Space \|\| 1(S) 11010110(V) 1(P) 0(T) / 1(S) 11100011(V) 1(P) 0(T)
\|\| Looks like even parity.. \|\| \|\| Menu \|\| 1(S) 11010110(V) 1(P)
0(T) / 1(S) 00100111(V) 0(P) 0(T) \|\| Checks out, still even.. \|\|
\|\| News \|\| 1(S) 11010110(V) 1(P) 0(T) / 1(S) 11001111(V) 0(P) 0(T)
\|\| Could be right here :) \|\| \|\| LShift\|\| 1(S) 11010110(V) 1(P)
0(T) / 1(S) 01110011(V) 1(P) 0(T) \|\| Yep - rekon I\'m right! \|\|

So it looks to be 1200 baud serial data with even parity (aka 8E1), two
bytes per pulse train block.

Part 2: Block repeats & press / release bit
-------------------------------------------

Are blocks repeated to provide resilience? Or just while a key is held
down?

Re-adjusting the \'scope, I can see that holding a key down produces a
pulse train block every 100 msecs, by capturing two blocks and zooming
in (gotta love [DSOs](DSOs "wikilink")!), I can see that the same pulse
train is emitted while a key is held, this gives me a nice key-repeat
feature if I want one.

What about if I just tap a key?

I can just about hit and release a key in \<100 msecs, the resulting
blocks have a short spacing between the first two blocks, then 100 msecs
to the third block, then nothing. Zooming in again shows that the second
and third blocks are the same, but are different from the first, like
this (omitting start/stop/parity bits):

\|\| Menu 1st Block \|\| 11010110 / 00100111 \|\| \|\| Menu 2nd Block
\|\| 11010100 / 00100111 \|\|

Ah-ha! We\'ve found the press / release bit in the first byte, and we
also know that release blocks are always sent twice.

Protocol - ***hacked***.
