---
title: IlluminatedGuitar__Text
date: 2009-04-14T11:34:27.000Z
---
1.  1.  intro

[Bob](Robert "wikilink") decided to spend his 16th birthday money on a
new guitar, and he chose a rather unusual instrument, the [Wesley
Guitars](http://www.wesleyguitars.co.uk/ "wikilink") PE200wh, a clear
acrylic strat copy - cool innit?

Of course we couldn\'t just leave it at that could we? Oh no. You see
it\'s such a lovely clear piece of acrylic, it just had to be
illuminated from the inside. No really, it did\...

1.  1.  open

If you\'re gonna put lights inside a guitar, you gotta see what\'s
already there :)

Here we are opening it up to check the size and shape of the cavity,
which is nicely routed, and all the hardware is attached to the
frontplate (so no major disassembly required).

1.  1.  choose

Some rummaging on the Maplin website turned up the ideal light source -
apparantly designed for lighting around vehicle bodies, these flexible
LED strips are low power, super bright, can be cut into smaller units
and will bend round inside the cavity.

To provide a bit of colour, I bought two strips, one white and one blue,
and a toggle switch to select between them.

1.  1.  fit

After much careful measuring, some cutting and a fair bit of soldering
on wires, the light strips can be taped into the cavity like this. Note
that I have soldered the strips with the negative sides commoned
together, which cuts down on wires and prevents nasty short circuits if
the parallel strips touch.

1.  1.  switch

In order to select different colours, we put in a SPDT toggle switch
with a centre detent (ie: off). To this we connected the feeds to the
lights, and a link wire to the power input, which comes via\...

1.  1.  power

The necessary 12V supply **was** fed to the guitar via the middle ring
of this stereo jack socket, a stereo screened cable and a custom made
breakout box on the floor, to which a suitable 12V supply is connected
(we\'ve been using an old PSU from a force feedback steering wheel).

Although this worked, it wasn\'t ideal for a couple of reasons: the
pickup signal and lights share the ground connection at the socket, so
ground lift due to lighting currents causes clicks in the signal;
pulling the plug in/out momentarily short circuits all the contacts on
the plug which could damage both the supply and the amp depending on
what shorts first. Not good.

We subsequently replaced the Strat-style socket mounting plate with a
flat acrylic plate, and added a standard 2.5mm power socket. We also
changed to using a switched mode power supply from an old LCD monitor
which neatly avoids any mains hum. It\'s now quiet when operating and
safe from short circuits - still using the stereo socket with the
intention of sending digital lighting control signals to the guitar\...

1.  1.  results

Need I say anything? Just how cool is that? :)

Seeing just how darn bright this is, we are now planning on putting a
dual dimmer circuit in the guitar, with perhaps an audio sensor chip
(National Semi LM4970 or the like) so the lights follow your playing
and/or using the middle ring of the stereo socket to deliver a UART
signal from a remote lights controller (DMX via a PIC to the I2C bus
input of LM4970 maybe?). Your suggestions are welcome!

1.  1.  end
