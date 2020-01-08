---
title: Bosch SMS Disassembly
date: 2016-12-05T20:54:30.000Z
summary: >
  Phil] just experienced a dishwasher failure, it started tripping
  the house power and thus some disassembly was required.
---
Trip!
-----

So last Wednesday the house power tripped out while I was away at just
before midnight, [Joseph]({{< relref "joseph.md" >}}) did the right thing,
checking for burning things before pushing the trip back on. All
appeared well again. Chalk one up to weirdness.

Then on Thursday it happened again, while I was present. We checked for
obvious failures again, pushed the trip back on and it popped straight
back out this time. Pulling all the plugs around the house got it to
stay on, so we worked through the list of 'things we turned on about
midnight Weds and 10pm today' - the dishwasher was the only option.
Plug everything except the suspected kit back in - all good, problem
identified.

Grab the multi-meter, measure the resistance between live and earth on
the plug pins, above 20 Mohm with the power off, below 1 Mohm with the
power button in. Time to pull it apart and find the short...

Disassemble!
------------

This is where it gets tricky as there are no disassembly instructions
for my Bosch SMS40T42UK/09 that I can find on the 'net and no obvious
way in (like screws on the back on the lid). I'll have to wing it,
possibly break stuff and **document as I go**. If you are going to
follow along at home, you'll need a Torx T20 and a large flat screwdriver.
Here's the teardown photo stream :)

### the lid

{{< figure src="../../images/upload/IMG_20161203_131159.png" class="float-left" >}}
{{< figure src="../../images/upload/IMG_20161203_131257.png" class="float-left" >}}

Two catches, accessible through the rectangular apertures just
below the lid hold the whole lid on at the front, which then slides off
the back on hooks. I discovered these the hard way by breaking one
:(

<div class="float-clear"/>

### the side panels

{{< figure src="../../images/upload/IMG_20161203_131507.png" class="float-left" >}}

Once the lid was off, the rest was easy, a series of three
(different) screws hold each side panel on. All Torx T20 heads.
Once the screws are removed, the panels tilt outwards and drop
down from hooks underneath.

<div class="float-clear"/>

### trouble spotted

{{< figure src="../../images/upload/IMG_20161203_132138.png" class="float-left" >}}

No need to remove any more panels, at this point I spotted
moisture where it shouldn't be, above the electronics and in the base
tray. What I thought especially odd was that there was a sheet here to
deflect water away from the electrics at all, looks like a known
issue!

<div class="float-clear"/>

### confirmation of short

{{< figure src="../../images/upload/IMG_20161203_133201.png" class="float-left" >}}

Pulling the cover off the electrics revealed a wiring loom with
one obvious fat connector for the heater, which I disconnected and
measured for resistance to the earth / chassis: <1Mohm, confirmation
that the heater had lost integrity and making the whole machine
suspect.

<div class="float-clear"/>

### abandon hope

At this point it looks like a known sealing / leakage issue around the
side of the wash tub has resulted in considerable water ingress to the
base tray and thus the heater (which practically rests on the tray),
destroying its insulation from the outside. Further disassembly and
possible replacement of the failed part might resurrect the machine, but
its over 3 years old, and the pipework on the other side (not shown)
looked pretty manky / furred up, so I abandoned further attempts at
fixing and bought a replacement washer. I figured it had depreciated at
under 2 pounds/week so didn't owe me much!
