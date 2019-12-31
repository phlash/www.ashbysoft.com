---
title: CMI-8738 vs Jack
date: 2011-04-17T18:39:34.000Z
---
The Problem
-----------

A few years ago I bought an impressively cheap CMI-8738 based sound card
from Trust, it cost £15 I think. Ever since I have been trying to find a
way to use it reliably under Ubuntu linux for digital recording from our
Akai DPS-12.

The root cause is that as soon as you enable the S/PDIF input, the card
stops delivering sample buffers via Alsa unless there is a valid S/PDIF
signal present (ie: the DPS-12 is connected and *switched on*). This is
fine except that we are using jackd at the bottom end of the audio
stack, and jackd doesn\'t like a card that doesn\'t sample regularly, it
crashes out with a watchdog error.

We *could* remember to switch the DPS-12 on *before* the PC every time
we switch the PC on\... not gonna happen unless someone intends to
record something, or we can live with no digital input (as we have been
doing for a number of years).

The Solution
------------

..for which I owe Mr Torben Hoen a beer: **alsa\_in**

It\'s so darn simple - leave jackd running with output only (S/PDIF and
analogue are fine and nice low-latency), then in my audio startup
script, run alsa\_in to read samples from the S/PDIF input and pretend
to be the standard capture backend for jackd (ie: call it \'system\').

The magic is that alsa\_in is *happy to work with no input*, it just
delivers empty buffers to jackd unless the S/PDIF signal is provided,
thus samples arrive from the CMI-8738, whereupon alsa\_in delivers those
to jackd - genius :)

/me dances a little jig :)
