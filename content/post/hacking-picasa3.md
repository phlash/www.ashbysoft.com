---
title: Hacking Picasa3
date: 2012-03-13T01:00:25.000Z
---
The Need
========

I have a whole pile of photos of family and friends that I have indexed
with Picasa v3.8 and it\'s face recognition ability, using the Windows
version of Picasa3 (because it was the \'right\' way to do this a couple
of years ago).

In the middle of some facebook\'ery using my preferred OS (Ubuntu 10.10
ATM) I decided I wanted a photo of a friend to post, so grabbed the
Picasa installer and ran it up in wine. All went well, but I got a nice
empty list of albums and no people, despite telling it where the photos
are on the network file server. Time to find out where Picasa hides the
metadata :)

The Research
============

Of course I went straight to the \'net and found a couple of posts back
in 2007 that talked about copying album information from the Application
Data area of the Windows user to the same area in wine\'s emulation:
kudos to these guys:

<http://forensicir.blogspot.com/2007/07/picasa.html>

<http://smallutilitiesforfree.blogspot.com/2007/11/how-to-copy-picasa-albums-from-windows.html>

The Hacking :)
==============

A little prodding around on my Windows partition shows that pretty much
the same structure is still there in current Picasa3 builds, along with
the all important Picasa2/contacts folder that has a nice XML file with
all my people in, *and their Picasa hash values*. These hash values are
what ties together the contact details and the faces in photos, which
are stored in special files (.picasa.ini), one for each folder through
the image archive itself (on the file server).

I therefore copied the contacts.xml file, and the album XML files (from
[Picasa2Albums](Picasa2Albums "wikilink")/<hash>) from my Windows disk
to wine\'s emulation area (\~/.wine/\...).

The next trick is to convince Picasa3 that I have the same mapped drive
letter (S:) in wine for the file server that I have in Windows - easy to
arrange with winecfg.

The final hack was to open up the
[Picasa2Albums](Picasa2Albums "wikilink")/watchedfolders.txt file and
remove the slightly broken assumption that I have C:\\Documents and
Settings within wine..

The Result
==========

Startup Picasa3 again, and lo! I have albums with photos in, but
**still** no people. Bah. Just out of curiosity I tried adding a folder
and Picasa did it\'s thing, scanning for faces and then *oh joy*
reconnecting the faces with the contact details. So the fix is simply to
rescan all the photos and it will pick up all the existing data
(slowly). Time for bed while it chews through 10000 photos!

Phil.
