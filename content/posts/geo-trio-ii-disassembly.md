---
title: GEO Trio II In-Home-Display Insides
date: 2020-11-02T12:53:30.000Z
author: Phlash
summary: I'd like to build my own modules for this extensible display..

---
Why would you do this?
======================
I have just joined the millions who have 2nd gen (SMETS2) smart metering
installed, and was interested in sending metering data to other systems
(like home automation), but it turns out the existing standards and
devices don't really support this (which is a bit crap but hey..)

The In-Home-Display (IHD) unit I have is a Green Energy Options (GEO)
Trio II, which also works as a Consumer Access Device (CAD), if the
optional WiFi module is fitted. Turns out this will only talk to the
energy company web site and send _them_ the data for fancy cloud based
app stuff - not what I want.

However - if the _interface_ to the WiFi module is easy to understand,
then it might be possible to build a special module that can divert
the data to a sane protocol such as MQTT. So what's the module interface?

Here's what's in a GEO Trio II
==============================

[Teardown photos](https://photos.app.goo.gl/Viq3mZQFctv81QUDA)

As you can see, it's a fairly simple beast, with just a few ICs, the
aerial (ZigBee for meter network), the LCD and buttons. The devices are
all identifiable (eventually, once you type the right text into search
engines).

 * MCU#1: NXP LPC54605J512ET180 low power MCU /
   ARM Cortex-M4, 512k Flash, 200k SRAM, USB (x2), many serial/GPIOs
 * MCU#2: NXP JN5169 wireless micro controller /
   ARM (unstated), 512k Flash, 32k SRAM, 2.4GHz radio I/O, serial/GPIOs
 * Flash: GigaDevices GD25Q32CSIG 32Mbit serial flash

The WiFi adapter connects to the 6 pin 0.1" header at the top, two pins
(1,2) are Vdd and Gnd, one is likely a module detect line, leaving just
three for data - most likely an SPI or UART interface to a full-stack
WiFi+TCP/IP package such as this from Radicom:
[Radicom embedded WiFi Serial Module](http://www.radi.com/modular101.htm)

which bodes well for faking stuff, as it won't be encrypted at this point
(the TLS happens on the WiFi module) :)

The unpopulated devices may be related to developing SMETS2 standards for
the radio interface, or a change of display technology, moving the LCD
controller function to the LCD itself.

Next to the WiFi module connector is another set of pads that are accessible
without disassembling the device - these are very likely a JTAG (AVR layout)
connector for programming/upgrades, I still need to buzz these out to find
grounded pads, which will confirm this guess.

__[update]__: the pads are indeed an
[ARM-10 JTAG/SWD](https://rowley.zendesk.com/hc/en-us/articles/210033613-What-is-the-pinout-of-the-ARM-10-pin-connector-)
(dual mode) connector, confirmed by grounding of pads 3,5,9 :)

What happens next?
==================

I really want to get hold of a WiFi module, which will confirm the guess
about it being a complete WiFi+TCP/IP design and provide the pinout with
more certainty, then it's a job for a logic analyser to snaffle the data
while it's plugged in and confirm if plain text is available, if the IHD
holds certificates that it expects to be verified, etc. etc. and if the
protocol is fakeable on an ESP8266 or similar to map into MQTT packets!

Anyone got a WiFi module I can look at please?
