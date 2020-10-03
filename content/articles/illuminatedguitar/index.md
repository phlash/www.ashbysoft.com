---
title: IlluminatedGuitar
author: Robert
date: 2009-04-14T11:34:27.000Z
summary: Internal lighting for a Wesley PE200wh acrylic guitar - oh yeah.
---
1.  1.  intro

{{< figure src="open.jpg" link="open.jpg" width="256" height="192" class="float-right" >}}

[Bob]({{< relref "robert.md" >}}) decided to spend his 16th birthday
money on a new guitar, and he chose a rather unusual instrument, the
[Wesley Guitars](https://www.wesleyguitars.co.uk/) PE200wh, a clear
acrylic strat copy - cool innit?

Of course we couldn't just leave it at that could we? Oh no. You see
it's such a lovely clear piece of acrylic, it just had to be
illuminated from the inside. No really, it did...

<div class="float-clear"/>

{{< figure src="cavity.jpg" link="cavity.jpg" width="256" height="192" class="float-right" >}}

If you're gonna put lights inside a guitar, you gotta see what's
already there :)

Here we are opening it up to check the size and shape of the cavity,
which is nicely routed, and all the hardware is attached to the
frontplate (so no major disassembly required).

<div class="float-clear"/>

{{< figure src="ledstrip.jpg" link="ledstrip.jpg" width="256" height="192" class="float-right" >}}

Some rummaging on the Maplin website turned up the ideal light source -
apparantly designed for lighting around vehicle bodies, these flexible
LED strips are low power, super bright, can be cut into smaller units
and will bend round inside the cavity.

https://www.maplin.co.uk/Search.aspx?criteria=N56CF&DOY=13m12

To provide a bit of colour, I bought two strips, one white and one blue,
and a toggle switch to select between them.

<div class="float-clear"/>

{{< figure src="lights1.jpg" link="lights1.jpg" width="256" height="192" class="float-right" >}}

{{< figure src="lights2.jpg" link="lights2.jpg" width="256" height="192" class="float-right" >}}

After much careful measuring, some cutting and a fair bit of soldering
on wires, the light strips can be taped into the cavity like this. Note
that I have soldered the strips with the negative sides commoned
together, which cuts down on wires and prevents nasty short circuits if
the parallel strips touch.

<div class="float-clear"/>

{{< figure src="switch.jpg" link="switch.jpg" width="256" height="192" class="float-right" >}}

In order to select different colours, we put in a SPDT toggle switch
with a centre detent (ie: off). To this we connected the feeds to the
lights, and a link wire to the power input, which comes via...

<div class="float-clear"/>

{{< figure src="power.jpg" link="power.jpg" width="256" height="192" class="float-right" >}}

The necessary 12V supply **was** fed to the guitar via the middle ring
of this stereo jack socket, a stereo screened cable and a custom made
breakout box on the floor, to which a suitable 12V supply is connected
(we've been using an old PSU from a force feedback steering wheel).

Although this worked, it wasn't ideal for a couple of reasons: the
pickup signal and lights share the ground connection at the socket, so
ground lift due to lighting currents causes clicks in the signal;
pulling the plug in/out momentarily short circuits all the contacts on
the plug which could damage both the supply and the amp depending on
what shorts first. Not good.

We subsequently replaced the Strat-style socket mounting plate with a
flat acrylic plate, and added a standard 2.5mm power socket. We also
changed to using a switched mode power supply from an old LCD monitor
which neatly avoids any mains hum. It's now quiet when operating and
safe from short circuits - still using the stereo socket with the
intention of sending digital lighting control signals to the guitar...

<div class="float-clear"/>

{{< figure src="blue.jpg" link="blue.jpg" width="256" height="192" class="float-right" >}}

{{< figure src="white.jpg" link="white.jpg" width="256" height="192" class="float-right" >}}

Need I say anything? Just how cool is that? :)

Seeing just how darn bright this is, we are now planning on putting a
dual dimmer circuit in the guitar, with perhaps an audio sensor chip
(National Semi LM4970 or the like) so the lights follow your playing
and/or using the middle ring of the stereo socket to deliver a UART
signal from a remote lights controller (DMX via a PIC to the I2C bus
input of LM4970 maybe?). Your suggestions are welcome!
