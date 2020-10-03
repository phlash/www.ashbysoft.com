---
title: "Face Recognition"
date: 2019-12-28T10:23:34Z
author: Phlash
summary: >
  Phil recently noticed that Google Picasa has been
  discontinued since 2016 on all platforms, and he's heavily invested in
  the facial recognition capability (over 200 people tagged in 20000+
  photos over several years), with increasing likelihood that it will stop
  working at any point. Time to rescue the knowledge and find alternative
  technology.
---

TL;DR: Where's the code?
------------------------

Hi impatient person, it's here:
<https://github.com/phlash/faces_in_photos> and the gThumb plugin is
here: <https://github.com/phlash/gthumb-faces>

Motivation
----------

Google killed off Picasa desktop, which [Phil]({{< relref "phlash.md" >}})
has been using for a number of years, in particular because of it's
ability to recognise faces and tag / group them. With over 20000 photos,
and 200+ people tagged, it's time to get out before losing all that
knowledge.

Data escape
-----------

Provided the appropriate option is ticked, Picasa will save a
`.picasa.ini` file in each folder it knows about, containing rectangles
that locate faces in image files, and where those faces have been
tagged, the name tag used. While this preserves the output data, it does
not include the trained recognition model Picasa is using to accurately
match faces, this is buried in a custom binary database, and unlikely to
make any sense outside of the particular recognition engine used, so we
need to start again for this...

New recogniser tech
-------------------

After a bit of rummaging Phil found the excellent `face_recognition`
project from Adam Geitgey: <https://github.com/ageitgey/face_recognition>
and his clear blog series explaining stuff:
<https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78>,
fabulous job Adam!

Armed with this code, and after a fair amount of trial & error getting
dependencies working (see below), some testing showed that careful
tuning of image size and algorithm selection could result in decent face
detection & landmark extraction through a batch of images without eating
vast compute time.

Sane storage
------------

Because I intend to save overnight image processing results in a format
that can be easily queried by other tools on multiple systems, I need
portability, indexing and structure, preferably without a lot more
installation / maintenance pain: step forward SQLite :)

The current database schema supports two distinct jobs:

- keeping a record of all files (images or not) in the searched areas,
  detecting changes and duplicates (via file hashes).
- keeping a record of facial co-ordinates in each image (file hash),
  grouping them into similar clusters and labelling clusters.

Bootstrapping the clustering
----------------------------

Since I already have tags from Picasa, on some image files, I can
pre-load clusters from this Picasa data (including the multiple groups
per label), which gives me a starting point for clustering unknown faces
too.

Sage advice
-----------

Having got this far, I ran off the end of the tutorials from Adam and
was unsure on how to approach the classification / training stages, so I
asked my friend and colleague, GBG's resident data scientist
[Ian](https://twitter.com/IanHopkinson_). After my poor problem
description, Ian wisely suggested that I probably didn't have
enough training data to get a good machine learning model, it may well
'overfit' and have problems, besides that's all hard work with new
libraries (Scikit probably), and there are effective simpler means to an
end: analysis!

Encoding analysis
-----------------

Ian suggested I try and improve the basic face matcher that comes in the
`face_recognition` package, by looking at the variance of the elements in
a facial encoding (128 of them) across my data set, and weighting
towards those with higher variance when doing simple vector (euclidean)
distance measures. He also thought it would speed up the comparison if I
reduced the n(n-1) complexity back to n by averaging the already
labelled/grouped Picasa faces and comparing new data to those averages,
rather than every member of a group. Good advice, thanks Ian!

gThumb as a viewer
------------------

I went looking for a way to visualise outputs as it's tedious picking
through log files and firing up eog for sample images. After some
initial rummaging at <https://alternativeto.net> I installed gThumb from
the standard distro and started work on a plugin
<https://github.com/phlash/gthumb-faces>, which currently intercepts
image loading to draw red markers on images, and extends the tree menu
with a Faces tree showing all images that contain labelled faces.

face_recognition install
-------------------------

Adam provides instructions on installing the C library used (dlib) from
source here:
<https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf>

Having been through this, I discovered that the python package manager
does just as well, so my final install list to get this working was:

    # aptitude install python-pip python-setuptools python-numpy libboost-python-dev libjpeg-dev cmake
    # pip install dlib
    # pip install face_recognition

Speeding it all up
------------------

With everything in place and mostly working, I started running lots of
image files through.. which is when I discovered the need to tune face
detection settings to get any workable speed. Unfortunately the current
tuning misses a lot of faces that aren't square-on (it relies on HOG
first, only running CNN if nothing turns up, or not at all). I need GPU
power to make this all go faster!

Fortunately [Simon]({{< relref "simon.md" >}}) has just upgraded our
desktop PC which means there is a spare AMD Turks (6670) device and the
Xeon / Haswell integrated Intel graphics device I could use..
Cue installation montage of AMD card into my server and BIOS poking to
stop it disabling the Intel GPU when the AMD was plugged in :)

NB: If you want both integrated and extension GPUs working in a Dell
machine - you _must_ [enable 'Multi-Display' in the BIOS]
(https://www.dell.com/community/PowerEdge-Hardware-General/Dell-PowerEdge-T20-xeon-Multi-Display-bios-setting/td-p/4542733)
and you _must_ have a VGA device (or emulator) plugged into the VGA
port at boot - otherwise the BIOS turns off the integrated chip.

Now it gets fun again - I've never written any GPGPU code, and it looks
like I may have to port the underlying `dlib` library from CUDA to
OpenCL, since there is no CUDA for AMD or Intel devices (kind of..).

I thus started from zero: got a demo working, then got an FIR filter
implementation working (thanks [gr-clenabled](https://github.com/ghostop14/gr-clenabled))
then started comparing performance between CPU, Xeon GPU, AMD GPU and
was surprised that the Xeon GPU only just outperforms the CPU, while
the AMD GPU is _slower_, due to data shifting delays across PCI. Hmmn.
I'm still looking at tuning the code for AMD, since I was hoping for
at least 10x over the CPU, perhaps an FIR filter isn't a reasonable
testbed?

A word of caution here: at one point I wrote some bad GPGPU code which
didn't specify resources correctly, and didn't release them either -
running this a few times started producing errors, then *hard locked*
my whole server when it crashed on the Intel GPU - eek!

