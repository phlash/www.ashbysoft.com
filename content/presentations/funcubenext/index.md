+++
title = "FUNcube Next"
summary = "AMSAT colloquium talk given in Oct 2020"
date = 2020-09-29T13:54:00Z
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

## FUNcube Next
### to boldly go...
Creating an open platform in space

(with apologies to Mr Dickens)

{{% note %}}
 * Welcome back from lunch..
 * Gentle/non-technical start
 * Will cover four areas:
   * (past/present/future/actions)
     * cf:Christmas Carol
   * lessons learned
   * mission brief (to boldly go...)
   * early design thoughts
   * involvement/engagement points
{{% /note %}}

---

## FUNcube Past
(learning from the ghosts of previous missions)
 * Ambition pays off :)
 * Timing is everything!
 * Testing is also everything!
 * Team size matters - close working is effective
 * Documentation matters - multi-party confidence
 * Engagement was limited :(

{{% note %}}
 * AO-40, obc schedules, recovery/debug, dongle, telemetry variation
 * clock phase, watchdog pain, pod exit, launch ducks, engagement
 * serious bug after 2 years, community test tooling
 * get-togethers (jelly babies), small teams
 * pain when working with partial docs and others (FC-2)
 * only a few 'operators', dev/experiment exclusivity
{{% /note %}}

---

## FUNcube Present
(creating our new mission)
 * {{< frag c="Do something new and ambitious..." >}}
 * {{< frag c="Address engagement and documentation..." >}}
 * {{< frag c="Keep small teams, keep things moving..." >}}
 * {{< frag c="Build & launch an open space platform..." >}}
 * {{< frag c="Using managed, modular, popular tech..." >}}
 * {{< frag c="Materially lowering the barrier to entry..." >}}
 * {{< frag c="So *anyone* can do experiments in space!" >}}

{{% note %}}
 * Don't throw away the good stuff
 * Work openly on docs and technologies to..
   * Everything in github from the start (PRs welcome)
 * NB: teams plural, not just us :)
 * Support parallel working / experiment creation
 * Open platform separates launch from experiments
 * Choose MCUs with low cost of entry, open dev kits
 * Shipping our own dev kit/flatsat for testing
 * Extending on STEM ambitions/individuals/orgs
{{% /note %}}

---

## FUNcube Future
(what might that look like?)

{{< figure src="OBC.png" title="proposed OBC architecture" width="600" height="400" >}}

{{% note %}}
 * Here's where we are after 1 month thinking (mostly J!)
 * Two popular MCUs (STM32, K210), one with tensorflow ;)
 * Housekeeping system to guarantee behaviour for licence
 * Compatible with earlier missions (no wasted investment)
 * Optional 10GHz radio subsystem (phase synchronized).
 * Deployable as a payload in other missions (phew!)
 * Modular (more MCUs, different MCUs)
{{% /note %}}

---

## FUNcube Next
(so what happens next?)

 * FUNcube Team:
   * Firm up choice of MCUs & interconnects
   * Produce ICD/APIs (sensors, telemetry, radios)
   * Gain launch approval of design
   * Develop platform to ICD/APIs
 * Experimenters:
   * Design experiments, play with dev kits
   * Engage with FUNcube team via Github (TBD!)
   * Have fun :)

{{% note %}}
 * Long way to go, we are 1 month in!
 * Will endeavour to work 100% in open
 * Will endeavour to be API-led, allowing early engagement
 * Housekeeping functions are critical to approval
 * Want to allow full baseband access to radios..
{{% /note %}}

---

## ME :)

 * Phil Ashby (aka Phlash), M6IPX/2E0IPX
 * Retired Technical Architect @ GBG Plc.
 * Ex-BT (twice!)
 * Troublemaker/software for FUNcube
 * phil.funcube@ashbysoft.com
 * https://twitter.com/phlash909
 * https://dev.to/phlash909


{{% note %}}
 * Might go for full licence now M0IPx looks available ;)
 * Retied == more time for FUNcube!
 * See my dev.to blog post for more historical bits
 * Slides are available on my website.
{{% /note %}}


---


## YOU?

 * Questions?


{{% note %}}
 * Over to Q&A collector...
 * Jim/Graham may want to field a few ;)
{{% /note %}}
