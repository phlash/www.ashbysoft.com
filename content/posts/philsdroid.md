---
title: PhilsDroid
author: Phlash
date: 2013-03-12T11:45:54.000Z
---
New Droid for Old
=================

So I lent my droid phone (Huawei U8120 below) to
[Joseph](Joseph "wikilink"), \'cause his shiny toy got pinched :-(

Upon mentioning that I was now droidless, one of my colleagues at work
(thanks Duncan!) has lent me his unwanted Samsung GT-I5500, of a similar
vintage to the U8120, but locked to Three.. uh-huh.

Unlocking the GT-I5500
----------------------

According to the interweb (well ok, mostly the excellent [XDA Developers
Forum](http://forum.xda-developers.com "wikilink")), the network unlock
code in a GT-I5500 is stored in the ROM image in plain text - nice.

All one has to do is temporarily root the device using
rageagainstthecage or similar, connect to an adb shell as root, dump the
ROM from /dev/bml5 using cat or dd, then pull it off the phone and
search for a well-known signature near the unlock code. Power cycle the
phone and type the code in when prompted. Done.

The Stock ROM
-------------

It\'s running Froyo (2.2), with Samsung bells and whistles and of course
the G-man spyware. I\'ll be wiping this and putting ICS on when I get a
chance. There are also a bunch of Three apps (games mostly) that need to
\'authenticate\' via 3G (ie: prove you are still using their network!) -
not played any of course since I am on Vodaphone (BT Mobile).

Old Droid
=========

A colleague at work was kind enough to offer me a free, reasonably
modern handset (Vodafone 845 / Huawei U8120), so I\'m now the owner of
an Android phone - how hip is that :)

This page is here to chart my progress in
updating/modifying/hacking/developing etc. If I learn anything that
wasn\'t obvious from the \'net I\'ll let you know.

In The Beginning
----------------

It was running the stock Vodafone build of Eclair (Android 2.1), the
bootloader was not locked (dunno if Huawei bootloader can be locked),
the recovery OS was stock Huawei and it worked. Time to break it\...

NB: Getting to the recovery OS is a case of holding the \'Call\' or
green button while powering it on. Getting to the bootloader requires
holding the \'Hangup\' or red button while powering it on.

Backups and Ice-Cream
---------------------

Some rummaging on <http://forum.xda-developers.com> tells me that I can
run Ice-Cream Sandwich (ICS/Android 4.0.4), via an unofficial beta
release of
[CyanogenMod9](http://forum.xda-developers.com/showthread.php?p=20878789 "wikilink").
Of course I\'d like to keep the stock OS incase I ever need to put it
back.

The thread on XDA developers was very clear on proceedure:

-   start in bootloader mode, connect to a machine with the bootloader
    control application (fastboot), then replace the recovery OS with
    !ClockWorkMod.
-   put CM9 installation package on an SD card
-   restart in recovery mode, with the SD card installed
-   take a [NANDroid](NANDroid "wikilink") backup of remaining flash
    partitions
-   install CM9 from package on SD card

Take deep breath and restart in normal mode - wait a looong time while
Android configures. It works!

------------------------------------------------------------------------

Interesting Diversion -\> Joe\'s Droid :)
-----------------------------------------

[Joseph](Joseph "wikilink") has just got himself a shiny new HTC Desire
C on contract (so now I\'m waay less hip), and wanted to backup and root
it (as you do). A little more research turned up our [Rooting
method](http://www.modaco.com/topic/355158-r1-superboot-how-to-root-the-htc-desire-c/ "wikilink")
of choice.

Applying this method gained us a root shell (via adb), from which we
were able to copy off the raw flash partition of the recovery OS using
dd from the appropriate /dev/block/mmcpXXX device to
/sdcard/recovery.img. That accomplished we installed !ClockWorkMod and
took a full [NANDroid](NANDroid "wikilink") backup. Nice job.

------------------------------------------------------------------------

UI Pointers
-----------

Ok, so I\'ve got to get used to the UI metaphors on this touch screen
device (never had one before). Here\'s a list of all the things that I
didn\'t find obvious:

-   Unpairing bluetooth devices: Get to settings-\>bluetooth, then touch
    and *hold the icon* next to the device name. All the instructions I
    found on line forgot to mention the icon behaves differently to the
    device name area. Update: this appears to be a CM9 anomaly only -
    but I would still have expected someone to mention it (CM is
    popular!)
-   Tethering to provide Internet access for another device:
    settings-\>more-\>tethering, enable. However, do **not** then go and
    play with the connection options (accessed via the icon as above),
    as this *reverses* the tethering and the phone expects the device to
    provide it with \'net access. Took me a long while to work out what
    was going on there!

------------------------------------------------------------------------

Network Debugging
-----------------

New for ICS, it supports network connections to the debugging daemon
(adbd), so once I finally got it tethered to my laptop (see above), I
could connect to the phone\'s IP address and get a wireless shell. Yes
this also works over [WiFi](WiFi "wikilink"), but you wouldn\'t want to
expose an unauthenticated root shell to the \'net would you? eh?

Photos\...Err where?
--------------------

I took a couple of photos to check the camera works ok (it does), but
couldn\'t find them anywhere on the phone with the File Manager app..
odd. Turns out I had assumed the DCIM folder on my SD card was a
hangover from previous use, and that the Pictures folder was the obvious
place. Nope. Android follows the JEITA specification and puts photos in
DCIM. And videos. And the Gallery app in CM9 beta is broken so I
couldn\'t look at photos on the phone. Now using
[QuickPic](QuickPic "wikilink") which seems to work ok.
