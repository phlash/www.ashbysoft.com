---
title: Rivendell_Chroot
date: 2015-12-28T10:20:27.000Z
author: Phlash
summary: >
  [Phil](Phlash "wikilink") got down to some Linux voodoo over the
  Christmas holiday, in order to run a slightly too old application suite
  (Rivendell Audio 1.7.2) on a supported distribution (Ubuntu 14.04 LTS),
  and without the aid of a package manager safety net (whoo!), it turns
  out [Chroot](Rivendell_Chroot "wikilink") is a winner.
---
New holiday - new self-imposed challenge!

Context
-------

My favourite radio station
[FXR](http://www.felixstoweradio.org.uk "wikilink") use [Rivendell
Audio](http://www.rivendellaudio.org "wikilink") as part of their play
out system, and have recently been donated an [HP
[TouchSmart](TouchSmart "wikilink") 300-1025
PC](http://h20564.www2.hp.com/hpsc/doc/public/display?docId=c01918320 "wikilink")
to use in the public area, which I was asked to \'make work\' for audio
management duties and general Internet stuff..

The Patient
-----------

Turns out that HP ship the !TouchSmart system with Windows 7 Home
Premium, loaded with lots of their own sloooow software (thanks to a
not-exactly-rapid hard drive and heavy use of multiple .NET versions),
then the owner / donor adds another boatload of cruft like Apple iTunes
/ Bonjour, ezRecover, several dodgy browser plugins (the usual suspects
- adware, search bars, etc.), several browsers (hello Chrome + Google
services) AVG and Norton. The result is a machine that takes 10+ mins to
become usable from a cold start and frequently stalls as background
tasks hog the I/O bandwidth\... not nice.

Fix Attempt 1: Remove the crud, switch to Security Essentials for
anti-malware, prune the browsers back to Firefox only and see if it\'s
usable.

Fix Result 1: I bricked it (almost) by uninstalling Bonjour, which seems
to completely hose the IP stack. After the uninstall, Windows event log
service fails to start and /lots/ of other stuff depends on the event
log - broken O/S :( System restore got things back working, then I
successfully cleaned out a lot of other junk with help from
!SysInternals tools (autoruns is fabulous!), and Process Hacker.
Unfortunately it wasn\'t much more usable in this state, and the Windows
version of Rivendell software is unable to play audio, which doesn\'t
make good use of the hardware capabilities. Rethink time.

Fix Attempt 2: Ubuntu 14.04 LTS live CD, re-size NTFS partition(s) and
install basic GUI system, then add Rivendell packages. Simples.

Fix Result 2: Ubuntu just worked, almost. Everything except the touch
screen was supported out of the box, including the !WiFi card and
camera, and as expected it was pretty quick, even after choosing the new
Ubuntu GNOME 3 desktop. Some additional rummaging on the \'net produced
a working touch screen too :)

Obsolete app
------------

Now I hit a problem - the Rivendell Audio version we use @ FXR is
officially obsolete (1.7.2 circa 2010) and I have lost the original
packages, not that they would install on 14.04 as the dependencies are
all wrong..

I can of course query the existing installation(s) for file lists, and
collect all the binaries & libraries together. I can also grab the
dependency lists, but how to avoid collisions when I need an old library
to be used and I have a newer one in 14.04?

Collision Avoidance
-------------------

My first thought was simply to drop the app and it\'s libraries (down to
libc) in a folder, hack the LD\_LIBRARY\_PATH and see if stuff
worked\... kind of, except the app is 32bit, whereas my host O/S was
64bit, and many libraries depended on supporting config files that
collided with the host. Hmmn.

Some Googling later, it became apparent that what I needed was a chroot
environment, something I tend to avoid as my previous experience with
such things has been fragility and continuous maintenance work (I prefer
to avoid that!). However, there are now tools available to make stuff
easier, in particular the fabulous debootstrap which can build a working
chroot version of any Debian or Ubuntu distribution, and schroot which
manages all the fragile bind mounts and authentication file copying
automatically as you enter/leave the chroot - nice :)

The Chroot
----------

With a bit of
[assistance](https://wiki.ubuntu.com/DebootstrapChroot "wikilink") I
built a chroot environment targetted at 32bit Lucid Lynx (10.04) to
match the FXR studio systems, I chose to install the minimum system,
which includes apt-get so I can add other components easily. I then
worked through the dependencies from the app, and installed appropriate
packages to satisfy these. So far so good, but I had no package for the
app itself..

The Hack
--------

Having satisfied the dependencies I then copied the remaining binaries
into place from the archive taken from the studio - did it work? Yep :)

Unfortunately Rivendell Audio relies on a number of daemon processes,
and other GUI tools to operate, whereas a default chroot expects only
transient programs, so some additional work was required, in particular
creating a session via schroot to host the daemons, then re-attaching to
that session for each transient program. Much learning curve!

Pulse Audio
-----------

Yes the daemon from hell :) However it\'s mostly useful for normal
programs, I just need to get a daemon running in a chroot to use it via
ALSA bindings.. sounds easy huh? Well it turns out that other folks have
had trouble before, the only reliable approach is to enable network
access and use it - other approaches that rely on DBus and shared memory
seem to be fragile. So enable network access, limit to localhost and
we\'re done :)

Session on Demand
-----------------

Last bit - when to run the schroot session and daemons? Given that we
depend on pulseaudio and that in turn runs per user login, I chose to
have startup scripts for each transient program check for a session and
create it.. then on logout it gets torn down. Job done.
