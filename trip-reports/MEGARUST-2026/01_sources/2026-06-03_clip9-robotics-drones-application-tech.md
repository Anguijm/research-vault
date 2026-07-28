---
type: source
event: MegaRust 2026
session: Technical Track #4 — Robotics, Drones, and Advanced Application Technologies for Maritime Corrosion Management (Day 2 afternoon)
session_segment: Four 25-30 minute presentations moderated by Nate Livesey (NAVSEA, Anti-Rust Program PM Acting): George Samet (SwRI) on robotics state-of-the-art; Jim Kunkle (Apellix / Apellix) on spray-painting drones; Jeff Apt (Edify) on magnetic-crawler hull inspection in wet dock; Jim McCarthy (PPG Protective and Marine Coatings) on electrostatic coating application
audio_file: Voice_260603_130038.m4a
audio_duration: 01:45:04
transcript_file: ../audio/Voice_260603_130038.transcript.md
date: 2026-06-03
time_local_approx: 13:00–14:45 (Voice_260603_130038 timestamp implies 13:00 local recording start)
location: Marriott Mission Valley, San Diego — Sierra 5 room (per Dave Zilber's Day-2 agenda from clip 7)
classification: OSI — open conference proceedings
transcription_method: faster-whisper medium.en, local CPU
transcribed: 2026-06-04
citation_slug: mr26-clip9-robotics-drones-application-tech-2026-06-03
content_sha256: 27b8fd468fa859c9412a008b125a10b027cad7a2ee546f3c6b26c0e574255b1f
backfilled_hash: true
---

# MegaRust 2026 — Day-2 afternoon Technical Track #4 (Robotics, Drones, Application Tech)

## Summary

The Day-2 afternoon technical track #4 — moderated by Nate Livesey (NAVSEA, the Anti-Rust Program Manager Acting from clip 7) — covered industry-side technology offerings for maritime corrosion management. The moderator opened by framing all four presentations under his own program lens ("we're implementing technologies on the ships, and so that's the background of the program that I run for the Navy"), then handed off to four industry speakers in sequence.

The four presentations break into two paired themes:

- **Robotics for inspection and assessment:** George Samet (SwRI) presented the state of the art across crawlers, drones, snake-like arms, ROVs, quadrupeds, humanoids, industrial arms, and wall climbers — flagging inspection as the most mature task and the data-to-action gap as the most underdeveloped capability. Jeff Apt (Edify) gave the concrete in-water-dock application: magnetic crawler with pulsed eddy current array (PECA) and ultrasonic for hull-thickness assessment **while the ship is still wet, before dry dock**, so dry-dock scope can be planned before the ship hauls out. Apt cited a CBO analysis of 14 years of yard-period data showing dry-dock-overrun patterns (scope creep / post-haul-out discoveries) as the operational driver.

- **Advanced coating application:** Jim Kunkle (Apellix) presented spray-painting drones as a force multiplier for Navy shipyard coating operations — the extended version of the Day-1 clip-4 Apellix pitch. Jim McCarthy (PPG Protective and Marine Coatings, Director of Technical Operations US/Canada) presented electrostatic coating application — pinch-hitting for Bart Dima.

Operator's Anti-Rust Program (Lattner's organization per clip 7) sits at the receiving end of all four of these capability offerings; Nate Livesey moderating the track is a structural signal that the program is actively evaluating these industry products for SWARM Team adoption.

## FACT — quoted material

The presentations are speaker-by-speaker below. Transcription quality is broadly clean; persistent Whisper artifacts on company names — operator-confirmed canonical (2026-06-04): "Apellix" was rendered as "PCS" / "Pearl Coast Tech LLC" / "Pellex" / "Pelix"; "Edify" was rendered as "85 Technologies" (moderator intro) and "NFI Robotics" (Apt self-intro).

### Moderator — Nate Livesey opening framing

> **[00:01 → 01:11]** (Nate Livesey opening) "I'm Nate Lucy [Livesey per operator-confirmed Day-1], NFCO5, you might've saw me stand up a couple times this morning helping out with the anti-rust swimming team [SWARM Team] efforts. So we're implementing technologies on the ships, and so that's the background of the program that I run for the Navy. ... we've got three wonderful presentations this afternoon that we're going to go through, each one will be about 30 minutes."

(Moderator said "three" but four speakers presented — Jim McCarthy pinch-hit for Bart Dima as a fourth speaker per McCarthy's own opening at ~01:21:42.)

### Speaker 1 — George Samet (SwRI, Intelligent Systems Division)

> **[01:30 → 02:33]** (Nate Livesey intro of Samet) "Mr. George Samet, he's the staff computer scientist at Southwest Research Institute, SwRI ... George serves both as an advisor and project manager, contributing his expertise to groundbreaking initiatives in the maritime-enabled robotics. ... This program focuses on pioneering robotic applications for shipyards and vessels, driving advancements in efficiency, safety, and operational capability."

> **[02:37 → 03:24]** (Samet, scope of talk) "I'm going to talk about using robots to address corrosion management. ... When we want to use robots, we need to first ask ourselves, are we replacing repetitive, monotonous jobs? ... Are they going to boost productivity? Are they going to ensure quality and consistency? And in terms of maritime-enabled corrosion management, I think the answer is yes."

> **[03:26 → 03:47]** (Samet, four-category framing) "Today, I'm going to talk about corrosion management across four categories. First is above water at topside. Then inside the ship or confined access spaces. Fourth, underwater and submerged structures. And then maintenance, repair, and overhaul. And I also loop new development and new builds in that category."

> **[03:47 → 04:09]** (Samet, SwRI institutional framing) "Southwest Research Institute, or SwRI, as we're commonly called, we've been a nonprofit applied R&D organization for over 75 years. Our goal is to bridge that gap from on the left, where you see universities and emerging technologies, to production-level quality industry through applied research and development."

> **[04:22 → 04:31]** (Samet, on the AI-generated examples) "Now, we're an unbiased organization, so the examples and pictures that I'm giving today are not vector-specific. They're all AI-generated, so we keep that unbiasedness."

> **[04:55 → 05:34]** (Samet, robotic platforms covered) "What is the state of the art? Here is a diagram of what we see being used in industry and what things I think may be used in industry. On the top left, you see crawlers, as well as tracked robots, snake-like arms, underwater remote-operated vehicles, a duplication of snake-like arms, industrial arms, quadrupeds, or little dog robots, you may have seen the spot robot. Humanoids, I don't think I've seen those being talked about in terms of corrosion management, but they're a pretty exciting technology. Industrial arms, drones, and wall [climbers]."

> **[05:43 → 06:17]** (Samet, the inspection-vs-action gap) "In terms of what we see today, inspection seems to be the most prevalent task, and that's typically done with crawlers or drones. ... The level of quality and the results that we see are varying. They tend to be higher quality for repeatable, discrete inspection-type operations. We also see that there's a gap, and that's a gap between inspection and action. Going from simply collecting data, to assessing that data, to planning, making a plan for the corrosion remediation, to executing that plan, and then to reporting on the results of that execution."

> **[06:23 → 06:39]** (Samet, emerging trends) "In terms of emerging trends, we see that in surface work, specifically cleaning, prep, and coating. We don't see that too much in the way of actual repair work. And then we see it in intake inspections. Ironically, you're going to see some examples of that in the presentations to follow on."

> **[06:39 → 07:13]** (Samet, on the data-not-assessment limitation) "In inspection, really the idea there is that the sensors used for inspection are significantly smaller, they're less weight, and they require less power. That means you have smaller robots, which are able to access tighter confined areas. But those robots are really just collecting data. They're not actually assessing the environment around them. They're not actually assessing the corrosion that they're seeing. They're not actually really even seeing corrosion. They're just collecting that data in most cases."

> **[07:13 → 07:34]** (Samet, on preparation/protection/repair gaps and digital twins) "In terms of preparation, protection, and repair, we don't really see too much of that, presumably because those tasks require larger payloads, larger tools, and more power. Digital twins is an exciting opportunity in terms of monitoring and tracking corrosion over time."

> **[17:58 → 18:01]** (Samet, on cybersecurity risk) Robotic systems introduce cybersecurity risks. (Context-fragment quote — operator may want to confirm full context if cybersecurity is a CACI-relevant angle.)

### Speaker 2 — Jim Kunkle (Apellix / Apellix)

> **[32:49 → 33:18]** (Nate Livesey intro) "We have Mr. Jim Kunkle from PCS [Whisper artifact — confirmed below as Apellix, contracting with Apellix]. He's a technical principal, business development leader, and a recognized authority in protective coatings, corrosion mitigation, and pipeline asset protection. With his career spanning more than three decades..."

> **[33:18 → 33:48]** (Cumble self-intro, naming the right company) "Thank you, Nick. ... I want to let you know that I am the technical principal with **Apellix, and I contract with Apellix**. Apellix is at booth number 43, so make sure you stop over and check out the spray-painting [drones]. ... It's related to force multiplier, how we can advance Navy shipyard coating operations through the use of spray-painting drone technology."

(Cross-reference: Apellix is the same firm that gave the clip-4 pitch 2 spray-painting drone presentation on Day 1. The Day-1 speaker was named as Jim Kunkle per Whisper; the Day-2 speaker is Jim Kunkle per Whisper. Possible the names are different Whisper renderings of the same person, or two different Apellix-affiliated speakers — operator may know.)

> **[33:48 → 34:04]** (Cumble, scope of talk) "When I talk about spray-painting and drone technology, I'm talking about it being semi-autonomous or autonomous, as it's needed to be. But we're looking at this as a force multiplier to be an augmentation of skilled crews."

> **[34:12 → 34:57]** (Cumble, the shipyard environment trend) "In modern Navy shipyard operations, we're not always dealing with the same vessels all the time. ... And the conditions, they vary. And in fact, things are more aggressive today than they've ever been over decades in the past. You mix that in with future ship designs. They're going to become more complex. We're seeing that as things are getting planned out with tighter geometries, deeper recesses, and larger surface areas that are going to push traditional coating methods and processes to its limit. ... At the same time, we have maintenance windows that are shrinking. The fleet needs to turn faster."

> **[35:01 → 35:10]** (Kunkle, on QA/QC standards) "You layer on top of that the QA, QC expectations under MASS-C [NAVSEA likely, per operator 2026-06-04] standards. So coating performance isn't always just that issue."

### Speaker 3 — Jeff Apt (Edify)

> **[01:01:51 → 01:02:42]** (Nate Livesey intro of Apt) "Next up we have Jeff Apt. ... a graduate of Lamar University and a Houston, Texas, resident that works hand in hand with service providers and asset owners to determine the exact solutions for their robotic crawler needs. ... since joining the force of the [Edify — Whisper rendered as '85 Technologies'; operator-confirmed 2026-06-04] team, Jeff has been essential in providing expert analysis in robotic crawler solutions for the oil and gas, petrochemical, mining, and nuclear sectors."

> **[01:03:05 → 01:03:25]** (Apt, self-intro and topic) "Jeff Apt. I'm the global business and company manager for **Edify**. And today we're going to be talking about a robotic [hull] inspection in [wet] dock using a magnetic crawler integrated with pulse[d] eddy current array, and ultrasonic for corrosion assessment and planning."

> **[01:03:27 → 01:03:53]** (Apt, Edify framing) "Edify is a robotic manufacturer for crawlers, non-destructive testing instruments, and our key is providing these industries with tools to help eliminate confined space entry working from heights and producing the same human-like results for inspection, maintenance, and any work in confined spaces."

> **[01:03:53 → 01:04:26]** (Apt, scope of the Navy application) "Today I'm going to be speaking about the naval ship maintenance and the effects of the dollar amount and the planning that goes into a ship coming into dry dock and how can we help minimize that time in dry dock utilizing a magnetic crawler to assess [hull] thicknesses in wet dock to allow these groups to better plan for their maintenance schedules."

> **[01:04:26 → 01:05:08]** (Apt, the CBO dry-dock-overrun data) "The CBO produced analysis of 14 years of data for yard periods that exceeded the planned estimated times for different ship fleets. And the major driver of these overruns were scope, creep, and discoveries that were made after dry docking began. So the root cause of these dry dock overruns are the ability to assess [hulls] below the waterline and that's due to them being inaccessible from the interior or they're diver-based inspections."

### Speaker 4 — Jim McCarthy (PPG Protective and Marine Coatings)

> **[01:20:22 → 01:20:48]** (Nate Livesey intro) "For our next one here, we have Mr. Jim McCarthy. He is the Director of the Technical Operations for **PPG Protective and Marine Coatings**. With more than 20 years in the marine coating sector, he focuses on driving innovation, innovative application technologies, and helping shipyards and owners optimize coating performance."

> **[01:21:19 → 01:21:44]** (McCarthy self-intro, identifying that he's a substitute presenter) "Jim McCarthy, Director of the Technical Operations for the U.S. and Canada for PPG Protective and Marine Coatings. I think maybe part of that was **Bart Dima's biography**. ... He is our expert in electrostatic coating application. **I'm pinch hitting for him today**."

(This explains the moderator's "three presentations" count vs. the four-speaker reality — McCarthy substituted for Bart Dima of PPG at short notice. Bart Dima is PPG's actual electrostatic-application subject-matter expert.)

> **[01:21:44 → 01:22:02]** (McCarthy, scope of talk) "I'll walk through this presentation with you and tell you a little bit about what we've been doing in terms of taking the application process for marine vessels to the next level and doing that through electrostatic application."

> **[01:22:02 → 01:22:15]** (McCarthy, what electrostatic application brings) "I'll talk a little bit about the efficiencies that that brings as well as the consistency with the coating film, the thickness, smoothness, et cetera."

> **[01:22:33 → 01:23:17]** (McCarthy, the technology framing) "Electrostatic application is nothing new. It's been used for decades in industries like aerospace, automotive OEM, industrial, metal parts finishing. The difference here is that we're doing electrostatic application in a dry dock, in a largely unprotected environment exposed to the elements, as opposed to an automotive OEM manufacturer working under a roof and essentially a clean room. So major difference in terms of scale."

> **[01:23:17 → 01:23:51]** (McCarthy, value-prop summary) "I'll be discussing today is some of the opportunities that that brings, including improved coating efficiency, enhanced environmental performance, environmental impacts, and application consistency at scale. So we're painting large vessels. It's hard to get perfectly uniform films on such a large object. And electrostatic application brings advantages in terms of [standard area] application in that regard."

### Closing

> **[01:44:58 → 01:45:01]** (Moderator close) "Thank you all. Have a good rest of the day."

## FACT — paraphrased content

### Speaker 1 — George Samet (SwRI Intelligent Systems Division)

- **SwRI institutional framing.** Southwest Research Institute is a nonprofit applied R&D organization, 75+ years history. Intelligent Systems Division does maritime robotics. Position: bridge gap from universities/emerging-tech to production-quality industry through applied R&D.

- **Four-category corrosion-management framing.** (1) Above water topside; (2) inside ship / confined access spaces; (3) underwater / submerged structures; (4) maintenance, repair, and overhaul (including new builds).

- **Robotic-platform inventory covered.** Crawlers, tracked robots, snake-like arms, ROVs, industrial arms, quadrupeds (Spot-style), humanoids, drones, wall climbers.

- **State of the art per Samet.** Inspection is the most-deployed task. Cleaning / prep / coating in surface work is emerging. Repair work is not — payload, tool, and power constraints. Digital twins are an "exciting opportunity" for monitoring corrosion over time.

- **The data-to-action gap.** Current robots collect inspection data but don't assess the data, don't plan remediation, don't execute remediation, don't report on results. Samet framed this gap as the most underdeveloped capability area.

- **The smaller-robots-only-collect-data limitation.** Smaller robots can access tighter confined areas but their sensor payload is just data collection — they're not actually "seeing" corrosion in any analytical sense, just collecting raw data.

- **Cybersecurity risk** flagged briefly (~17:58–18:01). Robotic systems introduce cybersecurity risks. Sample-quote only; operator may want to confirm full context.

### Speaker 2 — Jim Kunkle (Apellix contracting with Apellix)

- **Affiliation correction from moderator intro.** Cumble is technical principal at **Apellix** (not "PCS" per Whisper artifact). Contracts with **Apellix** specifically for Apellix's spray-painting drone product line. Apellix was at MegaRust booth #43.

- **Cross-clip cross-reference.** Cumble's presentation is the extended version of the Day-1 clip-4 pitch 2 by Jim Kunkle (Apellix co-founder per Day-1 Whisper rendering). Operator should disambiguate whether Cumble and Kunkle are the same person with different Whisper renderings or two different Apellix-affiliated speakers.

- **Topic.** Spray-painting drone technology as a force multiplier for Navy shipyard coating operations. Semi-autonomous or fully autonomous. Augmentation of skilled crews rather than replacement.

- **Shipyard environment trends framing.**
  - Varied vessels (no "rinse-and-repeat" workload).
  - Conditions are "more aggressive today than they've ever been over decades."
  - Future ship designs will be more complex: tighter geometries, deeper recesses, larger surface areas.
  - Maintenance windows are shrinking; fleet turn time pressure is increasing.
  - QA/QC expectations under NAVSEA (Whisper: "MASS-C"; operator-disposition 2026-06-04) standards layered on top.

- **The 30-minute deep version of the clip-4 5-minute pitch.** Day-1 clip 4 captured the abbreviated pitch (NSI 009-32 compliance, OSHA, 3-person crew, 10,000 linear ft / 3 hrs goal, $200K project cost). Day-2 clip 9 has the extended technical version with the shipyard-environment-trend framing as the value-prop spine.

### Speaker 3 — Jeff Apt (Edify)

- **Affiliation correction from moderator intro.** Apt is the global business and company manager for **Edify** (not "85 Technologies" per Whisper artifact in moderator intro). Edify manufactures crawlers and non-destructive testing instruments for confined-space inspection.

- **Apt's background.** Lamar University graduate. Houston, Texas resident. Worked on robotic crawler solutions for oil & gas, petrochemical, mining, nuclear sectors before Navy work.

- **Topic.** Robotic hull inspection in **wet dock** (i.e., before the ship hauls out for dry dock) using a magnetic crawler integrated with **pulsed eddy current array (PECA)** and **ultrasonic** sensors for corrosion assessment and dry-dock-scope planning.

- **The CBO data point.** CBO analyzed **14 years of yard-period data** (not a 14-year overrun) showing that dry-dock periods routinely exceed planned estimated times. Major driver of overruns: scope creep / discoveries made after the ship is dry-docked. Root cause: ability to assess hull thickness below the waterline is currently constrained to (a) interior inaccessible spaces or (b) diver-based inspection.

- **Value proposition.** Magnetic crawler with PECA + ultrasonic NDI can be deployed while the ship is still wet, before haul-out, so scope can be planned before the ship hits dry dock — reducing the post-haul-out discovery surprises that drive overruns.

### Speaker 4 — Jim McCarthy (PPG Protective and Marine Coatings)

- **McCarthy is substituting for Bart Dima.** Bart Dima is PPG's actual subject-matter expert on electrostatic coating application; McCarthy is "pinch hitting" for him today. This explains the moderator's "three presentations" count vs. the four-speaker reality — the planned roster was three, McCarthy was a late substitution.

- **PPG affiliation and role.** Jim McCarthy is Director of Technical Operations, U.S. and Canada, for PPG Protective and Marine Coatings. 20+ years in marine coating sector. Innovation, application technologies, shipyard/owner coating-performance optimization.

- **Topic.** Electrostatic coating application for marine vessels — moving the application process "to the next level" via electrostatic delivery.

- **Technology framing.** Electrostatic application is not new — decades of use in aerospace, automotive OEM, industrial, metal-parts finishing. PPG's application is different because it's done in a dry dock in a largely unprotected environment exposed to the elements, vs. the clean-room conditions of automotive OEM.

- **Value props McCarthy will discuss.** Improved coating efficiency. Enhanced environmental performance. Application consistency at scale. Standard-area application uniformity on large vessels (where it's hard to get perfectly uniform films otherwise).

## Assessment

(Provisional — based on speaker intros and opening framings; deeper Q&A and technical detail not fully sampled.)

- **The track is industry showcase for Anti-Rust Program / SWARM Team adoption.** Nate Livesey moderating signals that NAVSEA's Anti-Rust Program is actively evaluating these four product/service categories for SWARM Team integration. Per clip 7, the SWARM Initiative uses contractors for "C2 Prime" production work alongside the CCAT-traditional sailor-training track. The four MegaRust track-#4 speakers are exactly the categories of contractor capability the SWARM Teams would pull from (inspection robots, drones, NDI crawlers, electrostatic application). Operator can decide whether any of these vendors are CACI BD-relevant.

- **Three of the four speakers represent industry capability gaps NSWC PHD and Anti-Rust Program have explicitly flagged.** Day-2 clip-8 Duldulao keynote called out the "by the time you see corrosion it's way too late" hidden-corrosion problem; Apt's wet-dock magnetic crawler with PECA + ultrasonic NDI is a direct response. Clip-8 also flagged the AEM/S "interior surfaces not accessible" structural concern; Samet's confined-access framing is the same problem space. Clip-7 Lattner's rapid-deployment SWARM Team philosophy aligns with Cumble's spray-painting drone as a force multiplier.

- **Apellix / spray-painting drone is now a 3-touchpoint pattern across the trip-report.** Day-1 clip 4 pitch 2 (Jim Kunkle, NSRP COMPASS framing), Day-2 clip 7 explicit reference (Lattner's "industry day next month with Josh [Chapman]" + Apellix mentioned in Lattner's team callouts), and now Day-2 clip 9 30-minute deep-dive (Jim Kunkle, Apellix). Apellix's specific NAVSEA engagement path is visibly building.

- **Edify is new to the trip-report.** Jeff Apt's Edify presentation introduces a vendor not previously surfaced. The wet-dock pre-haul-out inspection use case is operationally distinct from the dry-dock inspection robots in Samet's state-of-the-art framing. For any CACI BD posture touching surface-ship-maintenance pre-availability planning, Edify' wet-dock NDI is a candidate cross-reference.

- **PPG is a major Navy coating supplier and now has a named MegaRust contact (Jim McCarthy, Director Tech Ops US/Canada).** Cross-reference to clip 7 Mark Ingle's MIL-PRF-24635F polysiloxane spec work: PPG is one of the suppliers whose products fall under that spec. Electrostatic application is a delivery-mechanism innovation atop the same coating chemistries.

- **The "data-to-action gap" Samet named is the structural framing that ties all four presentations together.** Current corrosion-inspection robots collect data; the gap is data → assessment → plan → execute → report. Apt's NDI crawler is data-collection-focused; Samet wants the gap closed; Cumble's spray-painting drone is execution-focused; McCarthy's electrostatic delivery is also execution-focused. Closing the gap requires linking the four capability categories that the track surfaces.

## Cross-references

- **Day-1 clip 4 pitch 2 (Jim Kunkle / Apellix spray-painting drone)** — Jim Kunkle's clip-9 presentation is the 30-minute extended version of the Day-1 5-minute pitch. Same Apellix company. Whether Kunkle and Cumble are the same person with different Whisper renderings or two different Apellix-affiliated speakers is an open question.

- **Day-2 clip 7 (Mark Lattner Anti-Rust Program / SWARM Initiative)** — Nate Livesey moderating clip 9 is the same Nate Livesey on Lattner's team per clip 7 ("Nate's been helping me out tremendously"). Track #4 speakers are exactly the contractor categories the SWARM Team integrates per Lattner's framing.

- **Day-2 clip 8 (CAPT Duldulao NSWC PHD)** — Duldulao's "by the time you see corrosion it's way too late" hidden-corrosion problem is structurally what Apt's wet-dock PECA+ultrasonic NDI is trying to solve. Duldulao also cited thermography and fiber-optics as patent-pending NDI technologies at NSWC PHD; Apt's Edify PECA+ultrasonic is a complementary (commercial) NDI approach.

- **Day-1 clip 2 (NRL Oxsol-Free polysiloxane via ESTCP)** — Samet's SwRI is the same Southwest Research Institute that has SERDP/ESTCP project history (per Day-1 web research, "SwRI's James Dante Receives SERDP/ESTCP Project of the Year Award"). SwRI's Intelligent Systems Division (Samet's home division) is one of several SwRI divisions doing Navy work.

- **CACI capability book** — Robotics for corrosion management, drone-based application, magnetic-crawler NDI, and electrostatic coating application are all non-CACI corporate capability areas. CUSTOMER-INTEL classification fits.

- **CACI BD pipeline** — None of the four vendors are CACI direct competitors. Apellix (spray-painting drone) and Edify (wet-dock NDI) are candidates for subcontractor / teaming consideration if a future CACI-led Navy maintenance contract has a coating-application or NDI subcontract scope.

## Open questions for operator

1. ~~**Jim Cumble vs Jim Kunkle (Apellix affiliation).**~~ **Resolved 2026-06-04:** Jim Kunkle from **Apellix**. Same person as Day-1 clip 4. Whisper rendered "Apellix" as "PCS" / "Pearl Coast Tech LLC" / "Pellex" / "Pelix" in clip 9, and rendered Kunkle's surname correctly in clip 4 but as "Cumble" in clip 9. Operator-confirmed canonical: Jim Kunkle, Apellix.

2. ~~**Bart Dima at PPG.**~~ Closed 2026-06-04 — operator does not need to chase.

3. ~~**"85 Technologies" Whisper artifact.**~~ **Resolved 2026-06-04:** Jeff Apt's actual company is **Edify** (operator-confirmed). Whisper rendered the name as "85 Technologies" in the moderator intro and as "NFI Robotics" in Apt's self-intro — both are artifacts. Canonical: Edify.

4. **The CBO report — 14 years of yard-period data, not a 14-year overrun.** Operator clarification 2026-06-04: the CBO analysis spans 14 years of data on dry-dock yard periods that exceeded planned estimated times. **What I'm asking:** if you know the CBO report by title or year, the citation could strengthen any future BD brief that needs to argue for pre-haul-out NDI capability. Otherwise it's a "per Jeff Apt's MegaRust 2026 presentation" citation. (Framing in source file now corrected from "14-year dry-dock-overrun analysis" to "14 years of yard-period data analysis.")

5. **MASS-C** (cited by Kunkle at 35:01–35:10). Whisper artifact — operator-disposition 2026-06-04: likely "NAVSEA" (the phrase being "QA/QC expectations under NAVSEA standards"). Resolved.

6. **The cybersecurity risk Samet flagged at ~17:58.** Sample-quote only; I didn't pull the full Q&A context. **What I'm asking:** if cybersecurity-of-corrosion-robotics is a CACI-relevant adjacency (CACI does cybersecurity work), the Samet framing is worth pulling more carefully. Operator can decide whether to chase.

## Source-ledger entry (to be appended to `../source-ledger.md`)

```
### mr26-clip9-robotics-drones-application-tech-2026-06-03

- Audio file: Voice_260603_130038.m4a
- Session: Day-2 afternoon Technical Track #4 — Robotics, Drones, and Advanced Application Technologies for Maritime Corrosion Management
- Date / time (local): 2026-06-03 13:00–14:45 (1:45:04 audio)
- Moderator: Nate Livesey (NAVSEA, Anti-Rust Program PM Acting per clip 7 cross-reference)
- Speakers (four; planned for three per moderator opening, Jim McCarthy substituted for Bart Dima): (1) George Samet (Southwest Research Institute / SwRI, Intelligent Systems Division) — robotics state of the art for maritime corrosion management; (2) **Jim Kunkle (Apellix)** — spray-painting drone technology as force multiplier (operator-confirmed 2026-06-04; same person as Day-1 clip 4; Whisper artifacts on company and surname both rendered); (3) **Jeff Apt (Edify global business and company manager)** — robotic hull inspection in wet dock using magnetic crawler with pulsed eddy current array and ultrasonic (operator-confirmed 2026-06-04; Whisper rendered "Edify" as "85 Technologies" and "NFI Robotics"); (4) Jim McCarthy (PPG Protective and Marine Coatings, Director Technical Operations U.S./Canada) — electrostatic coating application (pinch-hitting for Bart Dima).
- Transcription method: faster-whisper, medium.en model, local CPU
- Transcribed: 2026-06-04
- Source file: `01_sources/2026-06-03_clip9-robotics-drones-application-tech.md`
- Notes: 1:45:04 audio, 3770 transcript lines. Transcription quality is broadly clean. Whisper artifacts (operator-confirmed corrections 2026-06-04): "Nate Lucy" for "Nate Livesey"; "Apellix" rendered as "PCS" / "Pearl Coast Tech LLC" / "Pellex" / "Pelix"; surname "Jim Cumble" for "Jim Kunkle" (same Apellix speaker as Day-1 clip 4); "Edify" rendered as "85 Technologies" (moderator intro) and "NFI Robotics" (Apt self-intro); "MASS-C" for likely "NAVSEA" in Kunkle's QA/QC reference (operator-disposition 2026-06-04). Substantive findings: (1) Anti-Rust Program is actively evaluating four contractor capability categories for SWARM Team integration — Nate Livesey moderating signals program-level industry-evaluation posture; (2) Samet's "data-to-action gap" framing is the structural thread tying all four presentations — current inspection robots collect data but don't assess, plan, execute, or report; (3) Apellix is now a 3-touchpoint pattern in the trip-report (Day-1 clip 4 pitch, Day-2 clip 7 Lattner reference, Day-2 clip 9 30-minute deep dive — Jim Kunkle is the consistent Apellix speaker across all touchpoints); (4) Edify is new to the trip-report — wet-dock pre-haul-out magnetic-crawler NDI with PECA + ultrasonic, citing CBO analysis of 14 years of yard-period data showing dry-dock-overrun patterns as data foundation; (5) PPG is now a named MegaRust contact via Jim McCarthy (Director Tech Ops US/Canada); (6) Jeff Apt's wet-dock NDI use case is operationally complementary to NSWC PHD's clip-8 patent-pending thermography and fiber-optics NDI development; (7) McCarthy's electrostatic-application work sits atop the same coating chemistries Mark Ingle's spec work covers (clip 7 MIL-PRF-24635F polysiloxane); (8) SwRI's Intelligent Systems Division (Samet) is the same SwRI that has SERDP/ESTCP project history per Day-1 web research.
```
