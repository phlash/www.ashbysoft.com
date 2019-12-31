---
title: News
date: 2019-02-21T10:30:36.000Z
---
21-Feb-2019: Facial recognition (updated)
=========================================

[Phil](Phlash "wikilink") recently noticed that Google Picasa has been
discontinued since 2016 on all platforms, and he\'s heavily invested in
the facial recognition capability (over 200 people tagged in 20000+
photos over several years), with increasing likelihood that it will stop
working at any point. Time to [rescue the knowledge and find alternative
technology](Face_Recognition "wikilink")! Update: a working gThumb face
browser plugin now exists!

7-May-2018: [KeePass2](KeePass2 "wikilink") extension fun
=========================================================

Earlier this year the [Have I Been
Pwned?](https://haveibeenpwned.com "wikilink") service released their
new API, with a cool \'k-anonymity\' partial hash checker function to
permit searches of potentially compromised password hashes without
providing a materially significant proportion of your password.
[Phil](Phlash "wikilink")\'s favourite password manager,
[KeePass2](https://keepass.info/ "wikilink"), supports this new API, but
doesn\'t work on Debian (or possibly other derivatives) as the
mono-runtime does not have [TLS1](TLS1 "wikilink").2 capable networking
- shame on you Debian, it\'s been available in Mono since 4.8.0 in Feb
\'17. So what\'s a hacker to do? Write their own plugin of course:
<https://github.com/phlash/keepass_hibp>

26-Mar-2018: TLS all the things!
================================

So [Chrome will soon be flagging /any/ web
content](https://www.theregister.co.uk/2018/02/08/google_chrome_http_shame/ "wikilink")
served over plain HTTP as not secure. I suspect other browsers will
follow soon enough, so it\'s time to ensure everything served from here
is over TLS\... cue montage of rapid terminal activity\... aand it\'s
done. thanks Let\' Encrypt and NGiNX for handling SNI so easily! If you
have content hosted with us, and anything seems to have gone a bit
weird, please [let us know](mailto:support@ashbysoft.com "wikilink").

29-Dec-2017: gpredict for Windows
=================================

[Phil](Phlash "wikilink") has been keeping himself busy over the
Christmas holiday period by helping with the Windows port of
[gpredict](http://gpredict.oz9aec.net/ "wikilink"), a popular satellite
tracking program. It\'s not done yet, but a workable binary is available
here:
<http://files.oz9aec.net/gpredict/temp/gpredict-win32-2.1.156.zip>. No
installer required, simply unzip and execute.

27-Dec-2017: 34C3 is here!
==========================

[Phil](Phlash "wikilink") really wanted to be there in person this year,
but tickets are surprisingly hard to come by, even when there are 15,000
of them! Anyway, the brilliant author (and friend of a friend :))
[Charles
Stross](http://www.antipope.org/charlie/blog-static/index.html "wikilink")
gave a terrifying warning of future AI\...
<https://media.ccc.de/v/34c3-9270-dude_you_broke_the_future>

7-Nov-2017: Debian 9 everywhere
===============================

After a few years of Ubuntu on home desktops/laptop,
[Phil](Phlash "wikilink") got weary of the growing instability, and
decided to look at Debian again. Turns out it\'s got pretty much
everything we need in the stable repository (stretch ATM), including a
working Gnome3 desktop setup (no more weird multi-screen issues as
below), so after upgrading his laptop, then the family desktops, we are
now a Debian 9 home :)

20-Aug-2017: New home for ashbysoft.com
=======================================

Today ashbysoft.com services (web hosting, email, source repository)
were migrated to a new server in Microsoft Azure, and we finally say
goodbye to the lovely people at
[Atomwide](http://www.atomwide.com/ "wikilink") who have looked after us
for the last 12 years - it was awesome guys!

23-Jul-2017: Blackhole / Sinkhole / Exfil hunting..
===================================================

Over the last couple of months, [Phil](Phlash "wikilink") has been
helping [Joseph](Joseph "wikilink") track down a credential leak problem
using various [network defence techniques](Blackhole_DNS "wikilink").

20-Apr-2017: Time to take something apart :)
============================================

Long time, no blog entry, but [Phil](Phlash "wikilink") has been playing
with some toys since Christmas, including an [HDMI Switcher that almost
worked right](HDMI_Switch_Reversing "wikilink").

22-Dec-2016: Lets Encrypt /and/ restart services
================================================

So, Let\'s Encrypt has been working smoothly, renewing TLS certificates
for us however, [Phil](Phlash "wikilink") noticed today that the
certificate presented by this website was about to expire! It turns out
that nginx hasn\'t been restarted since October (thanks Debian stable
:)), so we\'ve added a post-hook to /etc/letsencrypt/cli.ini that does
exactly that if new certs appear. Job done.

5-Dec-2016: Dishwasher disassembly
==================================

[Phil](Phlash "wikilink") just experienced a dishwasher failure, it
started tripping the house power and thus [some disassembly was
required](Bosch_SMS_Disassembly "wikilink").

23-Oct-2016: How Did I Miss This!?
==================================

Back in August it seems, some intrepid (cf: crazy) people started
playing with [GPUs](GPUs "wikilink") in the cloud for game streaming.
Yep - DIY [OnLive](https://en.wikipedia.org/wiki/OnLive "wikilink")
(other game streaming services have also failed). Not for the feint of
heart though, there are a lot of ugly config steps, but the most
important bit: [It Works
:)](http://lg.io/2016/10/12/cloudy-gamer-playing-overwatch-on-azures-new-monster-gpu-instances.html "wikilink")

07-Aug-2016: Real Certificates
==============================

Now that [Let\'s Encrypt](https://letsencrypt.org/ "wikilink") is
enabled by default in the majority of mainstream browsers, this site can
switch to HTTPS by default - today [Phil](Phlash "wikilink") threw the
switch to make that happen :) Let us know
[mailto:the.guys\@ashbysoft.com](mailto:the.guys@ashbysoft.com "wikilink")
if you are seeing certificate warnings!

02-Jun-2016: Laptop Battery Hacking
===================================

Yep, that\'s actually a post title. it turns out that
[Phil](Phlash "wikilink")\'s laptop is fussy about the brand of battery
you use, or to put another way: Lenovo like to lock users into their
expensive batteries, [yeah sure they
do..](Lenovo_Battery_Hack "wikilink")

02-Mar-2016: Reflow!
====================

[Joseph](Joseph "wikilink") brought his laptop home last weekend, with a
nasty problem: hard shut downs shortly after powering on. It seemed
thermal, mostly as the shut down would happen sooner with a warm system
and he\'d already tried the usual fault finding stuff, removing RAM
sticks, resetting CMOS etc, so we re-pasted and re-seated the heatsinks:
it got worse 8-/ In desperation we decided to \'reflow\' the motherboard
in the oven, 8mins @ 200C seemed to be the recommended procedure.. as
long as you have a good thermometer (not the oven thermostat). A bit of
rework extending the probe on a digital jam thermometer gave us an
internal temperature reading, and the cooking went ahead. Result? It
worked! Following re-assembly and a number of short reboot cycles while
the CMOS sorted itself out it\'s stayed working for a couple of days.
\[update 2016-03-14\]: it lasted just over a week, then the same bug
resurfaced :( [Joseph](Joseph "wikilink") is now on the backup laptop.
\[closure 2016-05-08\]: The supplier fitted a new motherboard after
their own investigation, so far so good..

25-Dec-2015: Chroot goodness
============================

[Phil](Phlash "wikilink") got down to some Linux voodoo over the
Christmas holiday, in order to run a slightly too old application suite
(Rivendell Audio 1.7.2) on a supported distribution (Ubuntu 14.04 LTS),
and without the aid of a package manager safety net (whoo!), it turns
out [Chroot](Rivendell_Chroot "wikilink") is a winner.

21-Nov-2015: [FUNcube](FUNcube "wikilink")-1 Birthday
=====================================================

Well blow me down if the ol\' cubesat is still working on it\'s [2nd
Birthday](FUNcube_2nd_Birthday "wikilink"). Cake was required.

07-May-2015: Obihai toy hacking
===============================

While looking for a usable cheap FXO port to connect the PSTN to his
home server, [Phil](Phlash "wikilink") came across the OBIHAI product
line, and bought a couple of toys to play with: an
[OBIHAI110](http://www.obihai.com/docs/OBi110DS.pdf "wikilink") voice
service bridge, which will do pretty much what\'s required without the
server attached, and an
[ObiLINE](http://www.obihai.com/obiline "wikilink") USB FXO adapter,
which is [being reverse engineered](OBiLINE "wikilink") for fun :)

15-Dec-2014: More Ham goodness
==============================

Not content with having one callsign, [Phil](Phlash "wikilink") recently
took his intermediate radio amateurs exam and is now known as
[2E0IPX](http://20ipx.uk "wikilink"). Yes that\'s a second vanity
domain, along with <http://m6ipx.uk>

31-Aug-2014: Trusty Tahir arrives
=================================

Yeah I know - all the kool kids were installing Ubuntu 14.04 (Trusty
Tahir) back in March.. I ([Phil](Phlash "wikilink")) like to leave it a
few months for the early pain to settle down and the Internet to fill up
with useful advice :) Speaking of which: moving the window buttons
around has changed (again!) - If you\'re using GNOME Flashback
(previously Classic), you\'ll need to fire up dconf-editor (not
gconf-editor any more), search for \'button-layout\', which is probably
in org.gnome.desktop.wm.preferences, then edit to suit (as before).
Inspired by Felipe Lavín (https://coderwall.com/p/76mwva). \[edited -
5/Oct/2014\]: Seriously annoyed with how cr\*p Gnome desktop is on my
dual monitor setup - pretty much every time I boot and log in DBus is
broken in some way and I get mirrored screens. Switching out to a
terminal (Ctrl-Alt-F1), then restarting lightdm service usually fixes
the DBus fail (probably some stupid race condition introduced in an
effort to get a login screen faster than Windows..), but by then it\'s
mangled my .config/monitors.xml file so I have to manually reset\...
\[edited - 9/Dec/2014\]: Looks like this annoying bug has been fixed..
mirrored screens in the greeter, but dual after login: aaand relax.
\[edited - 4/May/2015\]: the bug is back :( updated kernel seems to have
screwed up the Gnome Settings Daemon which is required to configure the
monitors (apparently). /Sigh/ \[edited - 24/Aug/2015\]: Still boots with
mirrored screens, but logging in fixes that promptly.. logging out again
leaves the screens separate: slightly better I suppose.

17-Jul-2014: EBS numbers - such fun!
====================================

[Erdos Bacon Sabbath
Numbers](http://erdosbaconsabbath.com/lists/ebs/ "wikilink") are a fun
(and slightly nerdy) measure of how close someone is to all three of
Paul Erdos, Kevin Bacon and Black Sabbath. Terry Pratchett is listed
with an EBS number of 9, but I think he\'s now one step closer to
Sabbath via a recent collaboration with Steeleye Span on the
\"Wintersmith\" album:
<http://www.folkradio.co.uk/2013/11/steeleye-span-wintersmith/> mentions
that the producer of Wintersmith is Chris Tsangarides
<http://en.wikipedia.org/wiki/Chris_Tsangarides>, who also worked with
Black Sabbath. TerryP-\>ChrisT-\>Sabbath? [Phil](Phlash "wikilink")
\[edited: 2014-12-15\] Well the EBS team don\'t do producers but I get a
credit for improving the musical linkage :)
<http://erdosbaconsabbath.com/terry-pratchett/>

04-Jun-2014: D-I-Y telecine machine
===================================

[Stu](Slash "wikilink") has been converting a Super8 film projector into
a telecine machine to convert his father-in-laws movies to digital
format. Inspired by [similar
projects](http://www.movie2video.com/index.php "wikilink") he has hacked
at a 1970s projector and some free animation software to produce some
watchable results. Still some way to go before they could be considered
a replacement for professional telecine services, but not bad for a few
quid in parts!

18-Apr-2014: Hacking Old Keyboards With a \'Scope
=================================================

Yup - Easter holidays allow one time to play with one\'s own toys, so
just for the fun (and practice) I [reverse engineered the
protocol](ScopeHacking "wikilink") on an old infra-red keyboard (it came
with a [Netgem set top
box](http://www.radioandtelly.co.uk/iplayer.html "wikilink") many years
ago).

31-Mar-2014: Phil\'s A Ham!
===========================

It was bound to happen after all that time associating with
[FUNcube](http://funcube.org.uk "wikilink") people, Phil and a colleague
have just taken and passed the RSGB Foundation Course in amateur radio,
so Phil\'s got a callsign. You may now refer to him as:
**[M6IPX](http://m6ipx.uk "wikilink")** (yes, my favourite protocol).

11-Feb-2014: Grabbing the Stack for Fun & Profit
================================================

Ok, I\'m sorry about the subject line, just how
[Phil\'s](Phlash "wikilink") brain works I\'m afraid. I\'ve been amusing
myself recently by writing a [memory allocation
tracer](StackGrabbing "wikilink") in VC++ to track down some pesky
memory leaks in a large app.

13-Nov-2013: New Job
====================

Well, [Phil](Phlash "wikilink")\'s got one anyway,
[Stu](Slash "wikilink") just got himself bought out recently :)

19-Mar-2013: New Webcomics!
===========================

I think I have a new addiction: <http://www.dumbingofage.com>. Spent 4
hours recently catching up with this from panel \#1 back in 2010 to
date.. need more sleep!

12-Mar-2013: Toy Update
=======================

I loaned my droid phone to Joe (who broke it!), so I have another one
[PhilsDroid](PhilsDroid "wikilink")..

14-Aug-2012: Phils Got a New Toy
================================

Phil\'s just acquired (for nothing!) an [Android
Phone](PhilsDroid "wikilink"). So he\'s breaking it of course!

8-Apr-2012: Stark Raving Genius
===============================

I guess a few folks read XKCD? Well I only just found out about the
April 1st comic, [\"Umwelt\"](http://xkcd.com/1037 "wikilink"). Like a
lot of readers, I thought, it\'s a bit odd, then went on my way. However
- did you know that almost everyone sees a *different* comic? It varies
according to a whole range of variables, browser size & type, time of
day, IP address, location, language settings\... it *turns the whole
Umwelt idea into reality*, at least as far as browsing the web goes, and
readers are still finding new versions a *week* later! how much work
went into this comic? - stark raving genius Randell :)

13-Mar-2012: Picasa hacking :)
==============================

Driven by the need to use Picasa\'s face recognition ability, but not
wanting to reboot the PC into Windows (again), I decided to [hack at
Picasa3](Hacking_Picasa3 "wikilink") until it worked on Linux..

27-Feb-2012: Bah. Malware :(
============================

I popped my USB drive into the printer earlier and grabbed a scanned
image, then put it into the home PC while it was running Windows.. got a
pop up saying that malware had been detected on my USB drive. Bah. Now
scanning the home PC from Linux. Either my own PC is infected, or
possibly worse, the last machine I put my USB drive in - at the radio
station (which might explain a few things!). Another scanning job for
me. Oh joy.

27-Dec-2011: Upgraded :)
========================

Much to my surprise the upgrade to this server operating system (as
prompted by the failure back in August) went swimmingly :) Welcome to
Debian stable (squeeze), and hopefully no surprises for hosted sites..
if anything isn\'t working as before, do please hassle
[Phlash](Phlash "wikilink")..

29-Aug-2011: Weekend trouble
============================

Apologies to everyone for the absence of ashbysoft.com for the last
couple of days - and thanks to Scott at Atomwide for getting us back
running again. We are considering the failure as a hint that it\'s time
to upgrade the server again.. some planning required!

29-Apr-2011: ISP switchover, mostly
===================================

Yesterday our hosting company (http://atomwide.com) changed their ISP,
so everything in their data centre had to change IP address, including
us. It all went well, apart from me forgetting to save the new DNS zone
file for ashbysoft.com at my DNS provider (http://gandi.net) until about
8pm -doh! Thanks for the smooth service Scott :)

17-Apr-2011: Digital recording at last!
=======================================

Whilst playing with Ubuntu on the PC in [TheShed](TheShed "wikilink")
studio I finally discovered a way to [get digital audio input to work
reliably](CMI-8738_vs_Jack "wikilink") using our impressively cheap
CMI-8738 based Trust sound card (£15). This has been bugging me for
*years*.

12-Feb-2011: ZTE-G X930 Insides
===============================

[Tom](Thomas "wikilink") broke the USB connector off his phone, so I had
to disassemble it (no I really did!), and took the opportunity to take
some photos [ZTE-G X930 Insides](ZTE-G_X930_Insides "wikilink")

*08-Apr-11 Update*: I finally soldered a new connector back on - there
aren\'t many distributors of micro-USB surface mount sockets in the uk -
just Farnell it seems.

30-Jan-2011: Rivendell Hackery
==============================

Yeah I know, you all thought the site was dead and stuff\... anyhow, as
part of my role looking after the tech at [Felixstowe
Radio](http://www.felixstoweradio.co.uk "wikilink"), I maintain the
installation of [Rivendell](http://www.rivendellaudio.org "wikilink"),
one of our play-out software packages, which needed some attention on
Windows.. gory details [here](RivendellHacking "wikilink").

### anyone remember 2010?
