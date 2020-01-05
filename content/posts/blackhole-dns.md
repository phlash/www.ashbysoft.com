---
title: "Blackhole DNS"
date: 2017-08-10T22:16:10Z
summary: >
  Over the last couple of months, Phil has been helping Joseph track
  down a credential leak problem using various network defence techniques.
---

TL;DR gimme the scripts!
------------------------

OK, chill... they're all here: <https://github.com/phlash/sinkhole>

Err why?
--------

Since Christmas [Joseph]({{< relref "joseph.md" >}}) had noticed a number of
login attempts to Steam from weird locations, none successful due to
using 2 factor authentication (yay!), but concerning as it's an
indicator of compromise. Steam passwords getting stolen / ex-filtrated
from somebody, are a cause of concern for the victim as they may have
other (more important) stuff going the same way.

Early investigation, by changing the password then carefully sharing it
round the family members who have a need to know, did not turn up
anything obvious such as leakage occurring directly after a specific
individual used it on their device(s). So we thought we would try
setting a trap...

DNS for the win
---------------

All network traffic, from inside our home to outside, will very likely
use a DNS lookup to locate external services before making a connection
or sending UDP packets (there are some exceptions of course, more on
these later). Since we already operate our own DNS server, for
split-brain purposes, we should be able to use this as a filter to pick
up any unexpected lookups, record the device that asked and follow up
with more detailed investigation. Simples. Almost.

First we need to prevent any DNS requests bypassing our own server, so
that's adding a firewall rule to the home router to block port 53
(TCP+UDP). Turns out this /also/ blocks all ICMP traffic, as an
undocumented side-effect, which was rather confusing for a while (thanks
TP-Link!)

Next we need to enable logging on dnsmasq (our local DNS service). This
done we investigate the logs, and promptly get swamped by the thousands
and thousands of DNS requests in a day. We'll need to add some
intelligence!

Blackhole lists
---------------

Network intelligence comes in the form of a curated list of 'bad host
names' from github, courtesy of Steven Black
<https://github.com/StevenBlack/hosts>. Adding this to dnsmasq as a
local hosts file prevents lookups going to the real world, instead
dnsmasq responds with whatever IP address we choose to put in the file,
so we choose 127.0.0.1 (there's no place like home), and ::1 (IP6
equivalent as some evil scripts do IP6 lookups of CNAME records to
bypass DNS blackhole filters like this one).

This turns out to be /really/ effective, no more adverts on devices,
much faster load times in many cases, but unfortunately in other cases,
no page loading at all. Bah. It seems a number of advert-supported sites
(comics mostly) will not load the content until the ad has arrived, or
sites rely on responses to their stats trackers (looking at you Azure!).
Some exclusions need to be applied to the block list to get everything
back up and running.

Automating stuff
----------------

Black hole lists change on a daily basis, exclusions need applying and
reports need emitting: so I've written a couple of scripts to help
automate these parts (see github above).

Sinking traffic
---------------

Rather than 'blackhole' DNS requests with a local IP(6) address,
[Phil]({{< relref "phlash.md" >}}) thought it might be fun to operate a true
'sinkhole', that is, an endpoint for potentially malevolent TCP/IP
traffic, so it can be captured and investigated. Given the nature of the
traffic, it is unwise to use a real TCP/IP stack in a live system (there
may be exploits arriving!), and it may be useful to avoid the kernel
overheads of processing traffic for real (memory mostly), so the fun
begins:

Inspired by articles like this
<https://umbrella.cisco.com/blog/2014/02/28/dns-sinkhole/>, and starting
with sample code like this <https://github.com/jedisct1/iptrap>
Phil wrote a Python/Scapy based sinkhole program
(pysink.py in github repo). This worked, but Scapy is seriously slow and
it ground our quad core server to a halt! A second try, this time using
the raw socket API and writing all the protocol dissection required in
custom code (raw.py in github), works much better. To separate
potentially dangerous traffic from normal stuff, we added a USB Ethernet
adapter to the server (borrowed from the Wii!) but did not assign an
address, thus traffic is not passed up/down to IP or higher layers,
allowing the script to fake everything. We /did/ have to disable
promiscuous ARP responses (`/etc/sysctl.conf:
net.ipv4.conf.all.arp_ignore = 1`), otherwise the ARP layer would
respond to physical broadcast packets on the unaddressed interface.

OK, we're terminating dodgy traffic to the point where we have the first
payload packet arriving, which is usually enough to classify it, so how
to do that? Turns out there is an off-the-shelf solution, Suricata!
Suricata is a traffic analysis tool/IDS, designed to be fed from the
span or tap port of a physical switch, however it will work just as well
from the raw interface used to terminate the sinkhole :)

What do we learn/see then? Well, there are several damn noisy bits of
kit on the home network (Windows PCs, Humax STB) and Dropbox and Chrome
do weird things (broadcasting to detect peers
<https://blogs.dropbox.com/tech/2015/10/inside-lan-sync/>, sending fake
DNS requests
<https://isc.sans.edu/diary/Google+Chrome+and+%28weird%29+DNS+requests/10312>).
Unfortunately we don't see any Steam credentials flying about, nor do we
detect any known malware (yet).

Catching the problem
--------------------

So after all that fun (and it was fun!), we are no nearer finding how
Steam passwords are leaking out. Joseph made yet another password change
late one evening, and didn't pass it to anyone else as they were all
asleep. In the morning we discover it has leaked! This clearly indicates
Joe's laptop as the source, so we dive into the DNS and packet logs to
try and find any evidence. After a couple of exciting
<junk>.cloudfront.net names turn up, only to be discarded as they used
by HP (they run cloudfront and dogfood their own CDN), we run out of
data in the time period involved. So we must conclude that the malware
is carefully avoiding DNS, most likely by operating it's own
peer-to-peer network with bootstrap IP addresses. Much as we'd like to
attach Suricata to our outbound router to see all the traffic, it cannot
provide a span port (thanks again TP-Link). We also considered putting
Joe's laptop through a real hub (I have kept an old 10M hub for this
purpose) and monitoring that for a while, but time was against us, so we
take a pragmatic route..

Resolution (by fire!)
---------------------

Given Joe needed his laptop cleaned up, and we are unlikely to catch the
malware in action over a short time period, we took the nuclear option:
boot into Linux from a live CD, image the on board drive (SSD) and parts
of the game store (HDD), then wipe the partitions and re-install Windows
from a known good ISO. While Windows was installing several years worth
of patches (at least there is a roll up pack now!), we scanned the
images using ClamAV to see if anything turned up. Sadly not, a few false
positives discovered by putting hash values through VirusTotal, and that
was it :(

Resolution (by Valve)
---------------------

Trying to be helpful, we contacted Valve support and explained the issue
to them, whereupon they asked "which account?"... Turns out Joseph had
two, one active and one forgotton - guess which one had a known password in
a data breach? NB: Never use the same email address for >1 account!
