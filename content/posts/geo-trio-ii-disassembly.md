---
title: GEO Trio II In-Home-Display Insides
date: 2021-01-25T22:13:30.000Z
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

..which bodes well for faking stuff, as it may not be encrypted at this point
(the TLS happens on the WiFi module) :)

__[update, Jan 2021]__: it's not a standard WiFi/serial module, the WiFi
board has another user-programmable device, an ESP8285, running more Geo code..
this appears to handle asynchronous comms and has a separate command and
control protocol back to the main system. This makes sense if you wanted
to use a different network technology later on, and also holds promise
that I can still emulate and transmit my own data - quite possibly by
reprogramming the existing ESP8285 =) See below...

The unpopulated devices may be related to developing SMETS2 standards for
the radio interface, or a change of display technology, moving the LCD
controller function to the LCD itself.

Next to the WiFi module connector is another set of pads that are accessible
without disassembling the device - these are very likely a JTAG (AVR layout)
connector for programming/upgrades, I still need to buzz these out to find
grounded pads, which will confirm this guess.

__[update, Dec 2020]__: the pads are indeed an
[ARM-10 JTAG/SWD](https://rowley.zendesk.com/hc/en-us/articles/210033613-What-is-the-pinout-of-the-ARM-10-pin-connector-)
(dual mode) connector, confirmed by grounding of pads 3,5,9 :)

Investigating the WiFi module
=============================

__[update, Dec 2020]__: Courtesy of an email or two with William McNicol (thanks!)
I have purchased a WiFi module direct from GEO here:
[GEO WiFi module](https://www.geotogether.com/consumer/product/wifi-module/)
plugged it in and confirmed that it's sending packets to the 'net - rather
surprisingly UDP/IP. More info once I've got the 'scope on the connector
pins!

__[update, Jan 2021]__: I finally got round to probing the WiFi module while it's
connected to the main system, and yes, it's a simple UART @ 115k2 8n1 with both
Tx and Rx lines. Attaching an FTDI FT232 at 3v3 logic levels gives me bytes, oh
so many bytes... so what to do with them?

Relationship between serial traffic and network
-----------------------------------------------

I thought it best to try and understand the relationship between traffic on the
serial interface and the network, so I hooked up the FT232 and my network sniffer
to a common clock source (thanks NTP!) and watched everything for the first few
minutes of IHD operation.

It turns out to be pretty complex - I was able to deduce some of the serial message
format, in particular the start message marker, the length and checksum fields, which
gave me accurate timestamps for each message, and some content boundaries. Trying to
relate these to the UDP traffic on the other hand was not making any sense, it looks
like the command protocol simply issues a 'connect please' request, or one of a couple
of other requests (there are obvious request type codes), and the ESP8285 operates
completely asychronously, sending multiple different network packets, none of which
appear to contain much from the serial messages. There is some consistent timing that
I have noticed:

 * serial messages are typically at 10 second intervals (per message type)
 * network packets are at 4 second intervals (per length/type)
 * network packets are repeated 4 times, each with the same timestamp
 * network packet timestamps appear to be related to ZigBee / meter time, but
   I cannot see this transferred in the serial messages when it updates from
   boot (2011) to now (2020) :=(

Full details are [in my log file](/ihd-serial-tx.log) (prepare for ASCII documentation!)
