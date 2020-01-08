---
title: Lenovo Battery Hack
date: 2016-06-03T19:31:21.000Z
summary: >
  Yep, that's actually a post title. it turns out that Phil's laptop
  is fussy about the brand of battery you use, or to put another way:
  Lenovo like to lock users into their expensive batteries..right..
---
The Itch
--------

[Phil]({{< relref "phlash.md" >}}) bought himself a replacement high-capacity
battery for his Lenovo T430 laptop recently. It was from a reputable
supplier in Germany, clearly listed the T430 as 'compatible' on the
product description and was half the price of an official Lenovo
battery. What could possibly go wrong...

Upon insertion all looked well, the T430 worked fine, Ubuntu was able to
read the capacity and charge level (68%), but after an hour of use while
plugged into the AC power it didn't seem to have charged up (still
68%). Hmmn. Rebooting displayed a warning message:

    The battery installed is not supported by this system and will not charge.
    Please replace the battery with the correct Lenovo battery for this system.
    Press the ESC key to continue.

WTF!

I contacted the seller who promptly offered a return of the item, and a
postage refund once I had a receipt for posting. So I repacked the
battery and popped down to the post office, who told me that Royal Mail
won't handle a battery pack without it's associated 'device' aka my
laptop. Great, so back on the 'net to find a delivery company who will
ship a battery to Germany. No one. Nowt. Zilch. At least, not for less
than the cost of the thing (£40)!

Research
--------

Searching the 'net for the displayed error message it becomes clear
that Lenovo laptops have a 'Smart Battery', and that from the T430
onwards, they implemented a challenge/response authentication mechanism
to lock users into buying Lenovo supplied parts, ostensibly to protect
systems from battery fires when 'fast charging' the pack. Seems like
3rd party manufacturers are unable to replicate this behaviour properly,
and some (thanks INTENSILO) mis-label their batteries as compatible when
they are not.

It also turns up the splendid work of zmatt
<http://www.zmatt.net/unlocking-my-lenovo-laptop-part-1/>, who had the
exact same problem on his X230, but chose to reverse engineer the
problem rather than return the battery - good man!

A little later I come across more good work by Hamish Coleman
<https://github.com/hamishcoleman/thinkpad-ec>, who has automated the
earlier work of zmatt and added other patches to support different
keyboards on multiple IBM/Lenovo laptops, including the original battery
fix for the X230.

The Scratch
-----------

Since I have no sane way to return my 3rd party battery, and prior work
exists which is /almost there/ to fix my problem I decide to go for it
(what's the worst that can happen? I'll brick my laptop):

Step 1: Replace the original battery and check all is well (apart from
the rubbish capacity).

Step 2: Carefully work through zmatt's BIOS unpacking and editing
descriptions, double checking with Hamish's Makefile and tooling, and
teaching myself to drive
[radare2](https://github.com/radare/radare2) (also awesome),
I arrive at a point of no return: I /think/ I have a correctly patched
BIOS file, there is only one way to test it: flash my laptop and hope
for the best... I'm good: it starts up :)

Step 3: Swap to the 3rd party battery and see if it charges.. yep!
Relief!

The Payback
-----------

It's how open source works: I've got a new capability in front of me -
one that can fix battery charging issues on T430 laptops with a specific
BIOS version (2.57 if you're interested). I have to do the decent thing
and work that into Hamish's tools to give back to the community.

[edit: pull request accepted] Go get it from Hamish's Github above!
