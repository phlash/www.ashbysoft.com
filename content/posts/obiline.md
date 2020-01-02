---
title: OBiLINE
date: 2015-06-07T21:00:25.000Z
summary: >
  While looking for a usable cheap FXO port to connect the PSTN to his
  home server, [Phil](Phlash "wikilink") came across the OBIHAI product
  line, and bought a couple of toys to play with: an
  [OBIHAI110](http://www.obihai.com/docs/OBi110DS.pdf "wikilink") voice
  service bridge, which will do pretty much what\'s required without the
  server attached, and an
  [ObiLINE](http://www.obihai.com/obiline "wikilink") USB FXO adapter,
  which is [being reverse engineered](OBiLINE "wikilink") for fun :)
---
1.  1.  page was renamed from ObiLINE

OBiLINE USB FXO Adapter
=======================

Those lovely folks at OBIHAI have recently produced the cheapest USB FXO
device I\'ve seen: [OBiLINE](http://www.obihai.com/obiline "wikilink"),
available from Amazon all over the world, but thus far nobody seems to
have taken the lid off - until now :)

\|\|\<tablestyle=\"float:right;\" style=\"padding: 1em;\":\>\|\|

What\'s in the case?
--------------------

Not a lot it turns out (kind of expected since it\'s £25.00 inc. VAT!).

### Parts

-   [NuvoTon](NuvoTon "wikilink") Nano120LD, ARM-Coretex M0 Micro + USB
    [Datasheet](http://www.keil.com/dd/docs/datashts/nuvoton/nano1xx/trm_nano100%28b%29_series_en_rev1.06.pdf "wikilink")
-   [SiLabs](SiLabs "wikilink") 32178-FM1, Telephone interface chipset
    [Datasheet](http://media.digikey.com/pdf/Data%20Sheets/Silicon%20Laboratories%20PDFs/Si3217x_291x_Brief.pdf "wikilink")
-   [SiLabs](SiLabs "wikilink") 32919-A-FS, paired with above to provide
    FXO parts

What does it look like on USB
-----------------------------

Here\'s the interesting part: the device works in conjunction with
OBIHAI\'s closed-source VoIP gateway products (e.g. Obi202). One guy
plugged one into his Windows PC
<http://www.obitalk.com/forum/index.php?topic=7236.0>, but didn\'t get
much info.

I\'ve just bunged mine into my Ubuntu lappy, and it turns up as a sound
card (S16\_LE, 8kHz fixed), no other control interfaces are apparent, so
I don\'t know how it\'s used to seize the line (perhaps by just opening
the device?) or how ring detect works. I will attach the other end to a
PSTN line next and see what happens!

### Can I make it work?

Short answer: no :(

I\'ve tried playing with declared audio controls via alsamixer - nothing
much happens. Opening the device for record or playback results in a
stalled device.. there is something that needs to happen to wake this
thing up.

lsusb dump:

    root@lenny:~# lsusb -vs 3:5

    Bus 003 Device 005: ID 4f42:6901  
    Device Descriptor:
      bLength                18
      bDescriptorType         1
      bcdUSB               1.10
      bDeviceClass            0 (Defined at Interface level)
      bDeviceSubClass         0 
      bDeviceProtocol         0 
      bMaxPacketSize0         8
      idVendor           0x4f42 
      idProduct          0x6901 
      bcdDevice            1.00
      iManufacturer           1 Obihai
      iProduct                2 USB Audio Device
      iSerial                 0 
      bNumConfigurations      1
      Configuration Descriptor:
        bLength                 9
        bDescriptorType         2
        wTotalLength          192
        bNumInterfaces          3
        bConfigurationValue     1
        iConfiguration          0 
        bmAttributes         0x80
          (Bus Powered)
        [[MaxPower]]               64mA
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        0
          bAlternateSetting       0
          bNumEndpoints           0
          bInterfaceClass         1 Audio
          bInterfaceSubClass      1 Control Device
          bInterfaceProtocol      0 
          iInterface              0 
          [[AudioControl]] Interface Descriptor:
            bLength                10
            bDescriptorType        36
            bDescriptorSubtype      1 (HEADER)
            bcdADC               1.00
            wTotalLength           70
            bInCollection           2
            baInterfaceNr( 0)       1
            baInterfaceNr( 1)       2
          [[AudioControl]] Interface Descriptor:
            bLength                12
            bDescriptorType        36
            bDescriptorSubtype      2 (INPUT_TERMINAL)
            bTerminalID             1
            wTerminalType      0x0101 USB Streaming
            bAssocTerminal          0
            bNrChannels             1
            wChannelConfig     0x0001
              Left Front (L)
            iChannelNames           0 
            iTerminal               0 
          [[AudioControl]] Interface Descriptor:
            bLength                 8
            bDescriptorType        36
            bDescriptorSubtype      6 (FEATURE_UNIT)
            bUnitID                 5
            bSourceID               4
            bControlSize            1
            bmaControls( 0)      0x03
              Mute Control
              Volume Control
            iFeature                0 
          [[AudioControl]] Interface Descriptor:
            bLength                 9
            bDescriptorType        36
            bDescriptorSubtype      3 (OUTPUT_TERMINAL)
            bTerminalID             2
            wTerminalType      0x0101 USB Streaming
            bAssocTerminal          0
            bSourceID               5
            iTerminal               0 
          [[AudioControl]] Interface Descriptor:
            bLength                10
            bDescriptorType        36
            bDescriptorSubtype      6 (FEATURE_UNIT)
            bUnitID                 6
            bSourceID               1
            bControlSize            1
            bmaControls( 0)      0x01
              Mute Control
            bmaControls( 1)      0x02
              Volume Control
            bmaControls( 2)      0x02
              Volume Control
            iFeature                0 
          [[AudioControl]] Interface Descriptor:
            bLength                 9
            bDescriptorType        36
            bDescriptorSubtype      3 (OUTPUT_TERMINAL)
            bTerminalID             3
            wTerminalType      0x0301 Speaker
            bAssocTerminal          0
            bSourceID               6
            iTerminal               0 
          [[AudioControl]] Interface Descriptor:
            bLength                12
            bDescriptorType        36
            bDescriptorSubtype      2 (INPUT_TERMINAL)
            bTerminalID             4
            wTerminalType      0x0201 Microphone
            bAssocTerminal          0
            bNrChannels             1
            wChannelConfig     0x0001
              Left Front (L)
            iChannelNames           0 
            iTerminal               0 
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        1
          bAlternateSetting       0
          bNumEndpoints           0
          bInterfaceClass         1 Audio
          bInterfaceSubClass      2 Streaming
          bInterfaceProtocol      0 
          iInterface              0 
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        1
          bAlternateSetting       1
          bNumEndpoints           1
          bInterfaceClass         1 Audio
          bInterfaceSubClass      2 Streaming
          bInterfaceProtocol      0 
          iInterface              0 
          [[AudioStreaming]] Interface Descriptor:
            bLength                 7
            bDescriptorType        36
            bDescriptorSubtype      1 (AS_GENERAL)
            bTerminalLink           2
            bDelay                  1 frames
            wFormatTag              1 PCM
          [[AudioStreaming]] Interface Descriptor:
            bLength                11
            bDescriptorType        36
            bDescriptorSubtype      2 (FORMAT_TYPE)
            bFormatType             1 (FORMAT_TYPE_I)
            bNrChannels             1
            bSubframeSize           2
            bBitResolution         16
            bSamFreqType            1 Discrete
            tSamFreq[ 0]         8000
          Endpoint Descriptor:
            bLength                 9
            bDescriptorType         5
            bEndpointAddress     0x81  EP 1 IN
            bmAttributes            5
              Transfer Type            Isochronous
              Synch Type               Asynchronous
              Usage Type               Data
            wMaxPacketSize     0x0100  1x 256 bytes
            bInterval               1
            bRefresh                0
            bSynchAddress           0
            [[AudioControl]] Endpoint Descriptor:
              bLength                 7
              bDescriptorType        37
              bDescriptorSubtype      1 (EP_GENERAL)
              bmAttributes         0x00
              bLockDelayUnits         0 Undefined
              wLockDelay              0 Undefined
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        2
          bAlternateSetting       0
          bNumEndpoints           0
          bInterfaceClass         1 Audio
          bInterfaceSubClass      2 Streaming
          bInterfaceProtocol      0 
          iInterface              0 
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        2
          bAlternateSetting       1
          bNumEndpoints           1
          bInterfaceClass         1 Audio
          bInterfaceSubClass      2 Streaming
          bInterfaceProtocol      0 
          iInterface              0 
          [[AudioStreaming]] Interface Descriptor:
            bLength                 7
            bDescriptorType        36
            bDescriptorSubtype      1 (AS_GENERAL)
            bTerminalLink           1
            bDelay                  1 frames
            wFormatTag              1 PCM
          [[AudioStreaming]] Interface Descriptor:
            bLength                11
            bDescriptorType        36
            bDescriptorSubtype      2 (FORMAT_TYPE)
            bFormatType             1 (FORMAT_TYPE_I)
            bNrChannels             1
            bSubframeSize           2
            bBitResolution         16
            bSamFreqType            1 Discrete
            tSamFreq[ 0]         8000
          Endpoint Descriptor:
            bLength                 9
            bDescriptorType         5
            bEndpointAddress     0x02  EP 2 OUT
            bmAttributes           13
              Transfer Type            Isochronous
              Synch Type               Synchronous
              Usage Type               Data
            wMaxPacketSize     0x0100  1x 256 bytes
            bInterval               1
            bRefresh                0
            bSynchAddress           0
            [[AudioControl]] Endpoint Descriptor:
              bLength                 7
              bDescriptorType        37
              bDescriptorSubtype      1 (EP_GENERAL)
              bmAttributes         0x80
                [[MaxPacketsOnly]]
              bLockDelayUnits         0 Undefined
              wLockDelay              0 Undefined
    Device Status:     0x0000
      (Bus Powered)
    root@lenny:~#

Hi-res photos
-------------

[](attachment:OBiLINE2.jpg "wikilink")
[](attachment:OBiLINE3.jpg "wikilink")
