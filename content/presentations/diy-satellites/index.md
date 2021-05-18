+++
title = "DIY Satellites"
summary = "Ipswich Sync Developers talk given in May 2021"
date = 2021-05-18T12:00:00Z
layout = "bundle"
outputs = ["Reveal"]

author = "Phlash"
header_image = "FUNcube-Logo.png"

[reveal_hugo]
	theme = "blood"
	transistion = "zoom"
	slide_number = "c/t"
	embedded = true

+++

## DIY Satellites
### it's only rocket science..
The current state of the art in 'home made' satellites

{{% note %}}
 * I'll talk about 5 areas (briefly!)
   * Satellite background info (why, what, costs)
   * Amateur Satellite organisation (AMSAT)
   * FUNcube mission(s)
   * Satellite data on the 'net
   * Current FOSS initiatives (where you can get involved)
{{% /note %}}

---

### 1. Background Info
#### But...why?
{{< figure src="All-sats.png" title="Celestrak viewer showing satellites @ 2021-04-30T12:26Z" width="758" height="374" >}}

{{% note %}}
 * Earth observation (weather [NOAA], climate [SENTINEL], agriculture [PlanetLabs])
   * National Oceanic & Atmospheric Administrtaion (US): https://www.noaa.gov/
   * ESA Copernicus Sentinel missions (currently at 6): https://sentinel.esa.int/web/sentinel/home
   * PlanetLabs, daily whole earth imaging: https://www.planet.com/
 * Communication (INTELSAT/EUTELSAT, STARLINK)
   * INTernation TELecommunications SATellite organisation (now defunct)
   * EURopean TELEcommunications SATellite organisation (see a pattern?)
   * STARLINK - just a cool name from SpaceX :)
 * Navigation (GNSS - GPS/GLONASS/BDS/Galileo)
   * Global Navigation Satellite System
   * Global Positioning System (US)
   * GLObal NAvigation Satellite System (RU)
   * BeiDou navigation Satellite system (CN)
   * Galileo - Named after the astronomer (EU)
{{% /note %}}

---

### 1. Background info
#### History & sizes:Getting bigger..

'57 Sputnik-1|'81 Intelsat-V|'11 KA-SAT
-|-|-
{{< figure src="Sputnik_1_Exploded_View.png" width="250" height="200" >}} | {{< figure src="intelsat-5a.jpg" width="250" height="200" >}} | {{< figure src="KA-SAT_Copyright_Dominique_Marques-Astrium.jpg" width="250" height="200" >}}

{{% note %}}
 * 1957: Sputnik-1 58cm sphere, 83kg (mostly battery), 1W beacon, low earth orbit, 3 months in orbit (NB: nitrogen-filled!)
 * 1981: Intelsat-V, 1.5x1.5x2m box, 1928kg, 15m solar panels, 1800W to 25x transceivers, geo-stationary.
 * 2011: KA-SAT, 2.5x2.5.5m box, ~6000kg, 45m solar panels, 16kW to 80+ transceivers, 90GBits/sec, geo-stationary.
{{% /note %}}

---

### 1. Background info
#### History & sizes:Getting smaller..

'98 CNES programs|'05 ESA programs|'99 CubeSat|'09 PocketQube
-|-|-|-
{{< figure src="myriade.gif" width="200" height="150" >}} | {{< figure src="sseti-express.jpg" width="200" height="200" >}} | {{< figure src="Cubesat2.png" width="200" height="160" >}} | {{< figure src="pocketqube.png" width="150" height="150" >}}

{{% note %}}
 * 1998: Centre National d'Etudes Spatiale programmes, Myriade, 0.6x0.6x0.8m, ~150kg, fold out solar panels, 180W to payloads.
 * 2005: European Space Agency programmes, eg: SSETI Express (2005), 0.6x0.6x1.0m, 62kg, 12W to 2x transceivers, low earth orbit.
 * 1999: Cubesat /standard/, 0.1m cube, 1kg (1U=>12U modular), Cal Poly / Stanford.
 * 2009: PocketQube /standard/, 0.05m cube, 0.25kg, Morehead Uni / Kentuck Space.
{{% /note %}}

---

### 1. Background info
#### Cost to reach space

KA-SAT ~$350m(total)|FC-1 ~$100k+$100k|$50SAT ~$250+??
-|-|-
{{< figure src="KaSat_Eads02_0.jpg" width="300" height="225" >}} | {{< figure src="FUNcube1-small.jpg" width="250" height="225" >}}| {{< figure src="s50sat.jpg" width="300" height="214" >}}

{{% note %}}
 * KA-SAT proprietary single system: ~$350m inc launch.
 * FUNcube-1 standard format (Cubesat), COTS parts, homebrew (see below): ~£100k+~£100k launch
 * $50sat standard format (PocketQube), COTS parts, homebrew: ~$250+ unknown launch (GAUSS rideshare)
{{% /note %}}

---

{{< slide class="white-bg" >}}

### 2. AMSAT

AMSAT (US)|AMSAT-UK|AMSAT-NL
-|-|-
{{< figure src="AMSATALTLOGO.png" width="200" height="150" >}} | {{< figure src="AMSAT-UK logo2_2.png" width="133" height="150" >}}| {{< figure src="amsat-nl.png" width="320" height="122" >}}
AMSAT-BR|AMSAT-SA|JAMSAT (JP)
{{< figure src="amsat-br.png" width="150" height="150" >}} | {{< figure src="AmsatSA.png" width="150" height="150" >}}| {{< figure class="jam" src="JAMSATLogoOriginalWhite.png" width="320" height="100" >}}

{{% note %}}
 * https://www.amsat.org/amsats-around-the-world/
 * US initiative providing funding, global co-ordination, national bodies (AMSAT-UK, JAMSAT, etc.) obtain licences/insurance
 * global receiver network, more aerials than any governmental body (even NASA!), first to receive many signals
 * HAM radio transponders, facilitating both experimental work (protocols, modulation etc.) and long-distance comms (DXing), non-governmental, openly published global communications technology
 * Educational outreach (hello!)
   * STEM enthusiasts abound
   * Good contacts into educational systems/schools (lots of parents/governers/university relationships)
   * Opportunities to lower barriers further (see below!)
{{% /note %}}

---

### 3. FUNcube missions
#### FC 1->6

FC-1 QSL card | RX Dongles | Dashboard
-|-|-
{{< figure src="FC1-QSL.jpg" width="300" height="225" >}} | {{< figure src="FCDboth.jpg" width="300" height="225" >}} | {{< figure src="Nayif-1-Dashboard.jpg" width="300" height="225" >}}

{{% note %}}
 * 2009-2017, FC1 & subsequent iterations: 1U Cubesat, ~950g, 6W to one transceiver, LEO (550km)
   * Educational outreach initiative (GB4FUN), part funded by a legacy
   * AMSAT-UK + SSETI Express folks + helpers (me!)
   * As homebrew/HAM radio as we could make it (depending on skills and time), standard parts for: frame, solar panels, power supply/batteries, antenna+deployment system, AMSAT-UK/NL parts for radios, power amps, sensors, compute (+software), ground station kit (dongle)
   * Novel features: 'fitter' messages (store/forward 200 byte blocks) & whole orbit historical data downlinked every 2 mins, turnkey solution for educational reception (antenna, FUNcube dongle [USB], SDR software), centralised data warehouse collecting telemetry globally.
   * FUNcube-1 (AO-73) launched Nov 2013, still operational, success resulted in educational links and creation of Nayif-1 & JY1SAT with Emirate & Jordanian universities and a HAMradio payload on ESEO (ESA) mission
   * Each mission added features (magnetorquer stabiliser, higher power TX, images & digital audio messages)
   * Receiver deployed to Antarctica (excellent as all polar orbits go by!)
   * Receiver software open sourced (eventually, delayed for various reasons)
{{% /note %}}

---

### 3. FUNcube missions
#### FUNcube Next: OBC proposal..
{{< figure src="OBC.png" width="750" height="465" >}}

{{% note %}}
 * 2020+, FUNcube Next, a new hope: https://phil.ashbysoft.com/www.ashbysoft.com/presentations/funcubenext/#/
   * More open/inclusive development process (diversity, driving the Cubesat/PocketQube standardisation process)
   * An open platform in space, not a complete (closed) system, enables launch without completion (shorter dependency chain!) and 'fly your own code' initiative, on uncommited application MCUs attached to all sensors and radio systems. We are not alone in working towards this (SpaceTeamSat1: https://spaceteam.at/?lang=en)
   * Early design phase (diagram!)
     * Clear separation between housekeeping processor (HP)+radios / application MCUs (legal reasons!)
     * Extended Cubesat bus, new high-speed connections, defined protocols/APIs (extended standards)
     * User experiments run as applications under control of HP
     * Multiple applications available for scheduling by HP
{{% /note %}}

---

{{% section %}}

### 4. Internet data
#### SatNOGS
{{< figure src="SatNOGS.png" width="750" height="465" >}}

{{% note %}}
 * SatNOGS: https://satnogs.org/faq/
   * DIY ground station project, founded 2014, collect as much raw data/telemetry as possible globally
   * Includes currently non-decodable signals (as raw IQ data) for analysis (cf: SpaceX video decodes)
   * Focus on design and operation of a telemetry receiver station, plus a warehouse
   * All open source in Python on RPi3+ (or similar) & Arduino for motor control
{{% /note %}}

---

### 4. Internet data
#### FUNcube warehouse
{{< figure src="Warehouse.png" width="750" height="465" >}}

{{% note %}}
 * FUNcube warehouse: http://data.funcube.org.uk/missions
   * All received telemetry (via FUNcube SDR package) from launch day onwards for all FUNcube missions
   * Reception league table per mission ;)
   * Downloadable for long term analysis (facinating work on spin state over the years!)
   * Useful educational resource prior to direct reception to explain concepts (doppler, fading)
{{% /note %}}

---

### 4. Internet data
#### TLE (Gpredict)
{{< figure src="GPredict.png" width="750" height="465" >}}

{{% note %}}
 * TLEs (two-line-elements, celestrak: https://celestrak.com/, NORAD [via celestrak])
   * Position and velocity vectors for all tracked objects, proximity prediction/alerting (eek!)
   * Prediction/modelling of visibility of satellites from ground stations (eg: gpredict)
     * Automated control of directional aerial systems/receivers
{{% /note %}}

---

### 4. Internet data
#### Opportunities (Polaris)
{{< figure src="Polaris.png" width="750" height="465" >}}

{{% note %}}
 * Opportunities for ground-based development (eg: Polaris)
   * Machine learning across multiple data sets identifying emergent behaviour/patterns
   * Long term analysis of single mission data sets (eg: unexpected correlations)
   * ML based reentry prediction allowing better future mission planning
{{% /note %}}

{{% /section %}}

---

### 5. FOSS Projects
#### Things to dive into!

gr-satellites|FoxTelem|r00t.cz
-|-|-
{{< figure src="gr-satellites.png" width="300" height="225" >}} | {{< figure src="FoxTelemIQ-300x300.png" width="300" height="225" >}} | {{< figure src="r00t.png" width="300" height="225" >}}

{{% note %}}
 * gr-satellites: https://gr-satellites.readthedocs.io/en/latest/
   * Decoders for as many satellite telemetry formats as possible, started 2015
   * Popular well-maintained codebase (thanks to EA4GPZ, Daniel Estévez), modules for GNU-radio
 * Foxsat & FUNcube decoders
   * FoxTelem: https://github.com/ac2cz/FoxTelem
     * Java, bundles GUI and backend together
   * FUNcube decoder: https://github.com/funcube-dev/
     * C/C++ backend and go wrappers to pipe telemetry around (used in Antarctic to re-send via QO-100..)
 * Satellite hunters - SpaceX, Chang'e-5 & Tianwen-1 telemetry: https://r00t.cz/
   * Bleeding edge signal hunting and analysis ;)
   * First to publish decoded SpaceX Falcon-9 video from direct reception
   * Tracking Chinese missions through solar system
   * Looking at RocketLab, SpaceX Starship and Mars missions
{{% note %}}

---

## ME :)

 * Phil Ashby (aka Phlash), M6IPX/2E0IPX
 * Retired Technical Architect @ GBG Plc.
 * Ex-BT (twice!)
 * Troublemaker/software for FUNcube
 * phil.funcube@ashbysoft.com
 * https://twitter.com/phlash909
 * https://dev.to/phlash909
 * https://github.com/phlash


{{% note %}}
 * Might go for full licence now M0IPX looks available ;)
 * Retied => more time for FUNcube!
 * See my dev.to blog post for more historical bits
 * Slides are available on my website.
{{% /note %}}

---

## YOU?

 * Questions?


{{% note %}}
 * Over to Q&A collector...
{{% /note %}}
