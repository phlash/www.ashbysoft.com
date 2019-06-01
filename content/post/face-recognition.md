---
title: "Face Recognition"
date: 2019-02-21T10:23:34Z
---

TL;DR: Where's the code?
------------------------

Hi impatient person, it's here:
<https://github.com/phlash/faces_in_photos> and the gThumb plugin is
here: <https://github.com/phlash/gthumb-faces>

Motivation
----------

Google have killed off Picasa desktop, which [Phil](Phlash "wikilink")
has been using for a number of years, in particular because of it's
ability to recognise faces and tag / group them. With over 20000 photos,
and 200+ people tagged, it's time to get out before losing all that
knowledge.

Data escape
-----------

Provided the appropriate option is ticked, Picasa will save a
.picasa.ini file in each folder it knows about, containing rectangles
that locate faces in image files, and where those faces have been
tagged, the name tag used. While this preserves the output data, it does
not include the trained recognition model Picasa is using to accurately
match faces, this is buried in a custom binary database, and unlikely to
make any sense outside of the particular recognition engine used, so we
need to start again for this...

New recogniser tech
-------------------

After a bit of rummaging Phil found the excellent face\_recognition
project from Adam Geitgey:
<https://github.com/ageitgey/face_recognition> and his clear blog series
explaining stuff:
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

`* keeping a record of all files (images or not) in the searched areas, detecting changes and duplicates (via file hashes).`  
`* keeping a record of facial co-ordinates in each image (file hash), grouping them into similar clusters and labelling clusters.`

Bootstrapping the clustering
----------------------------

Since I already have tags from Picasa, on the same images, I can
pre-load clusters from this Picasa data (including the multiple groups
per label), which gives me a starting point for clustering unknown faces
too.

Sage advice
-----------

Having got this far, I ran off the end of the tutorials from Adam and
was unsure on how to approach the classification / training stages, so I
asked my friend and colleague, GBG's resident data scientist
[Ian](https://twitter.com/IanHopkinson_ "wikilink"). After my poor
problem description, Ian wisely suggested that I probably didn't have
enough training data to get a good machine learning model, it may well
'overfit' and have problems, besides that's all hard work with new
libraries (Scikit probably), and there are effective simpler means to an
end: analysis!

Encoding analysis
-----------------

Ian suggested I try and improve the basic face matcher that comes in the
face\_recognition package, by looking at the variance of the elements in
a facial encoding (128 of them) across my data set, and weighting
towards those with higher variance when doing vector (euclidean)
distance measures. He also thought it would speed up the comparison if I
reduced the n(n-1) complexity to n by averaging the already
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

face\_recognition install
-------------------------

Adam provides instructions on installing the C library used (dlib) from
source here:
<https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf>

Having been through this, I discovered that the python package manager
does just as well, so my final install list to get this working was:

    # aptitude install python-pip python-setuptools python-numpy libboost-python-dev libjpeg-dev cmake
    # pip install dlib
    # pip install face_recognition
