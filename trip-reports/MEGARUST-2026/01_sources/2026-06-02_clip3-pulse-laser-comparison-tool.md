---
type: source
event: MegaRust 2026
session: NSRP SPC Panel Meeting
session_segment: Pulse Laser Comparison Tool — Near-Complete Project Presentation
audio_file: LA-near-complete-project.m4a
audio_duration: 42:35
transcript_file: ../audio/LA-near-complete-project.transcript.md
date: 2026-06-02
time_local_approx: 10:38–11:20
location: Marriott Mission Valley, San Diego — NSRP SPC Panel meeting room
classification: OSI — open conference proceedings
transcription_method: faster-whisper medium.en, local CPU
transcribed: 2026-06-03
citation_slug: mr26-clip3-pulse-laser-comparison-2026-06-02
---

# MegaRust 2026 — NSRP SPC Panel: Pulse Laser Comparison Tool (Near-Complete Project)

## Summary

This was a 42-minute NSRP-funded project report-out by two presenters (Missy and Steve, both joined virtually) on a Pulse Laser Comparison Tool. The tool is a process-map overlay framework that lets shipyards compare different commercial pulsed-laser ablation systems against each other on the same chart, so testing performed on one laser can be projected onto another laser the yard might want to buy. The project closes July 6, 2026. HII Newport News Shipbuilding (James Brooks) is the self-funded industry partner, with Bath Iron Works and Huntington Ingalls listed as additional participants. The clip closes with Q&A from John McRory (NAVSEA 05 plate Technical Warrant Holder, joined virtually) and a separately-identified coatings-side TWH referred to as "Mark" — the same TWH split (substrate effect vs. substrate-for-paint) is explicitly stated by the questioner and confirmed by the presenter.

The technical heart of the clip is Steve's work on a novel parameter the project has coined "local hit cadence" — captured indirectly via infrared camera — that measures the timing between successive laser pulses on the same spot, beyond the simpler "fluence" (energy density) and "pulse count" parameters that prior NSRP/MANTEC work had identified as the two dominant factors. The project also caught a real instrumentation gap: their beam profiler was broken, so they could not directly measure waist diameter and fell back on manufacturer-reported spot sizes (with a written disclaimer). Pulse duration, by contrast, was directly measured and was found to be far from what laser vendors report on spec sheets — a finding worth flagging.

## FACT — quoted material

The following are direct quotes from the transcript. Timestamps refer to the transcript file. Transcription artifacts (Whisper substitutions) are flagged inline.

### Project framing and lineage

> **[00:42 → 01:10]** "The Pulse Laser Comparison Tool is a project that Steve and I have been working on with James Brooks at Newport News Shipbuilding. I want to point out here it's self-funding on this project. They've done this on another project that we've done previously too, so I just want to try to get the kudos for that because it is, for the amount of work that's being done here, we definitely needed them to fund themselves, so it's very much appreciated."

> **[01:36 → 02:14]** "As you know Newport News Shipbuilding has been very interested in using laser [ablation — Whisper rendered as 'relation'] in a number of applications. We were involved with one starting around 2017. We started talking about it. In fact there was a [NSRP — Whisper rendered as 'MSRP'] project that Newport News Shipbuilding had, James Brooks had, that led to then a MANTEC project that Steve and I participated with James on. It really focused on laser [ablation] of pre-construction primer that's used in their steel fabrication facility, primarily HSLA steels. We identified hundreds of parameter sets that really could affect material degradation in different ways."

### Project end date and panel transitions

> **[05:35 → 05:41]** "...now is going to conclude on July 6th of 2026."

> **[06:01 → 06:11]** "...we were SIB, then we were MIB, now back to SIB again so that this information can be leveraged across the different shipyards..."

### Lasers selected for study

> **[08:18 → 08:38]** "So we focused on the GC-500X, which is one of the ones of primary interest to CIB. The ADAPT laser system, like I said, that really checks the box for the CL-1000 because we're crossing over in terms of energy density in many of the areas. And then of course the p-laser QFC-100."

### Equipment loan / rental constraints

> **[33:54 → 34:16]** "...CIB actually knew [NUWC] Keyport loaned us their GC500X. It was on loan for us. It's actually been shipped back to [NUWC] Keyport actually just this past week. But that was on loan to us. So there's a warranty associated with that piece of equipment. If we stopped the beam on that to do some of the measurements that we did on the other one [we'd void the warranty]."

> **[34:29 → 34:43]** "Similarly the P laser which we actually were rather renting under an ONR MANTAC project. We got permission from ONR MANTAC to use it on a non-interfering basis for this project as well also avoided the warranty."

### Coating selected and its effect on test correlation

> **[11:05 → 11:38]** "So we were looking at the epoxy off-white this is Milperv 23236 [MIL-PRF-23236] and then there was also another type 6 epoxy that is an above color that's being used by BIW. So that's when we decided that the off-white epoxy is, you know, fairly similar to the buff. There was a lot of availability of that and it was available in the required time frame so we needed to really move out with that one. So that's how we selected the coating."

> **[37:13 → 37:45]** "we actually have talked to Montgomery you know a number of times we were putting together a test but as I mentioned we couldn't correlate to the original fatigue data because of the fact that there weren't sufficient samples in terms of the inorganic zinc primers we had to go to that epoxy obviously and it's also white so of course there's more energy input to take off that white epoxy than others so it limited the correlation well it actually ended the correlation to previous test data"

### Two dominating parameters from prior MANTEC project

> **[17:48 → 18:30]** "in prior testing the MANTEC project that Missy mentioned with Newport News we identified two primary parameters that were most that produced them the strongest effect or the result and one of them was the fluence so that's a measure of energy density how much pulse energy in the laser spot divided by the area of that spot size so that fluence was one of the primary parameters of interest and then the number of times we hit if you imagine how many bullets hit a specific place on your substrate how many pulses hit it that was our second primary number or parameter of interest"

### "Local hit cadence" — the novel parameter Steve coined

> **[19:10 → 19:30]** "...the local hit cadence and so this is something you won't see anywhere else yet but I anticipated some other people, they use different terminology but they're not getting the same information we're getting from it and so the idea is if you think of a drum beat somebody drumming can hit the same spot quickly in repetition or they can wait and come back..."

> **[20:00 → 20:22]** "...we know for example that some materials will build up heat and the heat in the substrate or in the coating will affect the [ablation], whether or not it comes off, whether it gets sticky when it comes off and so we need a measure for that which is something that wasn't directly measured... The emissivity is a material property which is also not something we could directly measure but we have a way to get it and that affects the output."

### Wavelength finding

> **[21:14 → 21:34]** "Every laser we measured had effectively an identical wavelength. That's not going to be the case if you buy another laser that just happens to be what's most common because you get the most power for your dollar for these wavelengths and they're effective. A lot of materials absorb this wavelength well."

> **[16:54 → 16:58]** (Steve, earlier) "each of these lasers is just above [visible-light range, in] the infrared so you can't see it..."

(Transcript context: ~1064 nm with some lasers at 1070 / 1080 nm — see transcript line 859–863: "most of the wavelengths we're looking here are 1064 or very close sometimes depending on the condition it might be 1070, 1080.")

### Pulse-duration vs. manufacturer-reported finding

> **[22:50 → 23:08]** "the pulse duration is something that's reported by most of these laser manufacturers. What actually was measured was pretty far from what was reported and it strongly affects the output and so we measured it pretty closely lots of times."

> **[23:10 → 23:28]** "The pulse frequency was relatively easily maintained so when people report that they're firing the laser at 10 kilohertz or 100 or 500 kilohertz almost across the board they were outputting exactly what they reported but the pulse duration was far from it..."

### Beam-profile measurement failure

> **[24:16 → 24:33]** "There are specific pieces of equipment that are designed to measure this well. We have one and it was broken. We didn't realize it but we tried and tried and it was having issues and so we ended up to capture what you see on the screen. We built our own. It was insufficient and so we were not able to measure the actual waist diameter which is the smallest diameter at focus."

> **[24:43 → 24:49]** "We're using the recorded values for what the spot size is in our analysis."

### Data volume

> **[32:40 → 33:06]** "...about 200 gigabytes that's being distilled right now using like physics driven algorithms. There's a lot of computational heavy data that's just hours upon hours of iterative processing. Steve's going through that right now. ... 400,000 unique observations with hundreds of features each and multiple responses."

### Test-plan use cases (laser ablation comparison contexts)

(Note: this material is presented as a recap by the speaker around 13:10–13:50 referencing AMPP-standard ablation levels; the AMPP-standard breakdown is the same one cited in clip 1.)

The two evaluated use cases in this project: removing pre-construction primer before further steel fabrication, and resurfacing aged MIL-PRF-23236 Type 6 epoxy via partial ablation. The AMPP-spec ablation levels referenced map to SSPC-SP-10/SP-11 (thorough ablation to bare steel) and SP-6/SP-3 (partial ablation, spot-and-sweep).

### Q&A — Technical Warrant Holder split confirmed

> **[36:53 → 37:07]** (Q&A speaker, addressing presenter and presumably John McRory on the line)
> "Just to clarify, I think you flipped through that last slide really fast. The tech warrant you're dealing with looking at the effect of a laser on the substrate is John [McRory], and the tech warrant you're dealing with about how this is a substrate for paint is myself working, right."

> **[37:07 → 37:11]** (presenter response) "Okay yes."

> **[37:45 → 37:59]** "Mark and I actually need to talk to you about something else offline sometimes so when you're back in the office if you can give me a call we can definitely talk more about this as well as I have some other questions for you I'd like to run by you."

### Acknowledgments

> **[36:01 → 36:29]** "...thank the folks the acknowledgement of all the different panels that have supported us surface and coatings preparation welding the PPPF as well as the sustainment panels. So we really appreciate that along with all the executive board members and then of course our NSRP project team from Newport News and Bath Ironworks as a participant and Huntington [Ingalls]."

## FACT — paraphrased content

The following are factual claims from the transcript, condensed but not editorialized. Each is attributable to a specific speaker.

- **Project organizational position.** The Pulse Laser Comparison Tool is an NSRP project led by two presenters (Missy and Steve, virtual). HII Newport News Shipbuilding via James Brooks is the self-funded industry partner. Bath Iron Works and Huntington Ingalls are additional NSRP project team participants per the acknowledgments slide. (Missy.)

- **Project lineage.** Discussions on laser ablation between the presenters and James Brooks (HII Newport News) began approximately 2017. The thread ran NSRP → MANTEC → the present NSRP comparison-tool project. The earlier MANTEC project focused on laser ablation of pre-construction primer in Newport News' steel fabrication facility, primarily on HSLA steels, identifying hundreds of parameter sets affecting material degradation. (Missy.)

- **NSRP panel transitions.** Project funding rode through SIB → MIB → back to SIB during execution. (Missy. Note: the literal panel acronyms — SIB, MIB — are not expanded on tape; operator should confirm whether these are standing NSRP panel names or transcription artifacts.)

- **Project closeout date.** July 6, 2026. All quarterly reports submitted, including one extra to cover the project extension. Final report still to be written. (Missy.)

- **Lasers selected.** Final test set: GC-500X (the system NSRP shipyards have in greatest deployment), ADAPT laser system CL-1000 (energy-density crossover with the GC-1000 they could not include), and the P-laser QFC-100 (a small fully-Gaussian-beam ~100-watt system, valued for its different beam type rather than its power). (Missy.)

- **Lasers deferred to future studies.** The 1000-watt-class systems — GC-1000, P-laser 1000, and ADAPT laser 1000 — were deferred for funding and time reasons. (Missy.)

- **Comparison anchor.** The IPG YLP-M 1-kilowatt laser from the earlier MANTEC project was carried forward as a comparison anchor for the new test set. (Missy.)

- **Equipment-loan constraints.** The GC-500X used in this project was loaned by NUWC Keyport (transcript renders Keyport with "[NUWC] knew" — a Whisper artifact). The unit was returned to Keyport the week before this MegaRust session. The P-laser was on rental under an ONR MANTEC project; permission was obtained from ONR MANTEC to use it non-interferingly. Both arrangements meant the team could not stop the beam mid-scan for some measurements (warranty risk on the loaned/rented hardware). (Missy.)

- **Coating selected and its consequence.** MIL-PRF-23236 Type 6 epoxy in off-white was selected based on availability and timing. The original plan was to use inorganic zinc primer (matching prior MANTEC fatigue test data) but insufficient quantities of zinc primer were available in the project's required timeframe. The substitution broke the correlation back to the prior fatigue dataset. The white epoxy color is more reflective and harder to remove, which also affected energy-input-per-removal-rate numbers. (Missy.)

- **BIW coating reference.** Bath Iron Works uses a different Type 6 epoxy in an above-water-line color ("buff"); the off-white selected for this project is fairly similar to that BIW color. (Missy.)

- **Two dominating parameters carried over from prior MANTEC work.** Fluence (pulse energy divided by spot area) and number of pulses hitting the same spot. (Steve.)

- **Local hit cadence — novel parameter.** The project has coined "local hit cadence" to describe the timing pattern of successive pulses hitting the same surface location. The motivation: hitting a spot ten times in rapid succession is thermally not the same event as hitting it ten times spread out, because the substrate or coating can build heat between pulses and change the ablation behavior (including whether ablated material gets sticky on the way off). This is captured indirectly via infrared camera analysis pixel-by-pixel, then fit to a physics-driven curve. (Steve.)

- **Emissivity — also recovered indirectly.** Same IR-camera analysis recovers an effective emissivity measurement that is sensitive to how much paint has been ablated (paint removal changes emissivity, which is time-dependent over the scan). (Steve.)

- **Wavelength finding.** All measured lasers had effectively identical wavelength (~1064 nm; some at 1070 or 1080 nm). The convergence reflects market-supplier economics: most power per dollar at that wavelength, and many materials absorb it well. Buying a new laser of a different wavelength would invalidate the wavelength-equivalence assumption. (Steve.)

- **Pulse-duration finding (worth flagging).** Measured pulse duration was "pretty far" from what laser manufacturers report on their spec sheets, and pulse duration strongly affects ablation output. This is a real-world calibration finding the project surfaced. (Steve.)

- **Pulse-frequency finding.** Pulse frequency, by contrast, matched manufacturer specs almost across the board (10 / 100 / 500 kHz). (Steve.)

- **Beam profiler was broken.** The project's commercial beam profiler had a hidden defect; the team did not initially realize and spent time trying. They built their own, which was insufficient, and ultimately fell back on using laser-manufacturer recorded values for spot size in the analysis (documented disclaimer). The measured value they could capture was qualitative only — not the true waist diameter. (Steve.)

- **Profilometry retained over original plan.** The technical warrant holder originally said profilometry was optional, but James, Steve, and Missy chose to include it to discern differences between beam types (spot size, waveform shape, hot-spot risk on asperities). (Missy.)

- **X-ray diffraction stress analysis was dropped.** Cost was prohibitive and very few service providers exist. Flagged to the TWH as a potential follow-on if future funding becomes available. (Missy.)

- **Data volume and analysis approach.** ~200 GB of raw test data; ~400,000 unique observations with hundreds of features each and multiple responses. Steve is running physics-driven algorithms plus machine-learning models to find parameter-knob combinations that overlap across systems. (Missy.)

- **Coating-color and production-rate questions surfaced for future work.** A Q&A questioner asked whether removal-rate-by-coating-color was a project deliverable; the answer was no, that was outside scope but could be calculated from the data they have. Both Missy and the participant suggested this might be a follow-on panel project. (Missy + unnamed questioner.)

- **Beam-stop measurements are a known follow-on need.** The team explicitly flagged that stopping the laser scan for certain diagnostic measurements could only be done on owned (not loaned/rented) equipment; this is a path forward for a follow-on project. (Missy.)

- **Two Technical Warrant Holders cover this project — split confirmed in Q&A.** One TWH covers laser effect on the substrate (John McRory, NAVSEA 05 plate TWH per cross-reference). A second TWH covers substrate-as-paint-base (referred to in Q&A as "Mark," referenced by the questioner as "myself working"). (Q&A — questioner stated the split; presenter confirmed.)

## Assessment

This section is the analyst's interpretation, flagged separately from FACT.

- **A notable finding from the project: the pulse-duration calibration gap.** "What actually was measured was pretty far from what was reported, and it strongly affects the output" is the kind of vendor-spec-vs-empirical-reality finding that has CACI implications: any program office or shipyard procuring a pulsed-laser ablation system based on vendor pulse-duration specs is at risk of getting different ablation behavior than the spec sheet implied. Candidate for the CACI exec brief if CACI's role under DTIC IAC MAC ever touches surface-prep tooling acquisition oversight.

- **The IR-camera-derived "local hit cadence" is methodologically novel.** Steve's claim that the term and its measurement approach are new ("you won't see anywhere else yet") suggests there is a publishable result here. For CACI's purposes this is interesting only if a downstream Navy adopter (e.g., NAVSEA 05P) takes the parameter into a procurement or qualification standard.

- **The broken-beam-profiler episode is a cautionary tale, not a critique.** The team caught it, documented the limitation, fell back to manufacturer-reported spot sizes, and continued. It does NOT undermine the rest of the project's findings — but it is the kind of fact that would surface in any rigorous independent technical review of the final report.

- **The Newport-News-as-self-funded-partner pattern is repeated from clip 1.** Both clip 1 (Laser Ablation Shipyard Implementation) and clip 3 (Pulse Laser Comparison Tool) report HII Newport News as a self-funded participant on NSRP laser-ablation work. Two data points is not a trend, but it is a pattern to watch when looking at HII MT's NSRP-investment posture. This is a soft cross-reference to the BDR opportunity (HII MT is on the BDR entity allowlist).

- **The TWH split confirmed in Q&A is operationally useful.** Two NAVSEA Technical Warrant Holders share oversight of laser-ablation-prior-to-coating: John McRory (NAVSEA 05, plate / substrate side) and Mark Ingle (NAVSEA 05, coatings side; per operator confirmation 2026-06-03). If the operator's CACI work ever touches Navy surface-prep policy, both names matter.

- **The Keyport equipment-loan story is a useful access pattern.** NUWC Keyport loaned commercial laser equipment to an NSRP study via the SIB/CIB panel relationship. This is the kind of inter-NSRP-and-NSWC equipment-sharing arrangement that may matter for future BDR-adjacent capability discovery (NSWC Keyport is in the operator's broader Pacific-region peer set, although not the SRF-JRMC primary mission set).

- **The MIL-PRF-23236 substitution story matters for any future "what coating system are Type-6 epoxy projects testing against" question.** Inorganic zinc primer is the preferred test bed but availability constraints push projects to off-white MIL-PRF-23236 epoxy. Color matters because reflectance changes energy-input requirements. This is the kind of fact a CACI BD assessment of laser-ablation-readiness-by-shipyard would need.

## Cross-references

- **Clip 1** (`2026-06-02_clip1-laser-ablation-shipyard-implementation.md`) — same panel session, ~30 minutes earlier. Same project family (NSRP laser-ablation thread, HII Newport News partner, AMPP-spec ablation-level taxonomy, MIL-PRF-23236 coating test bed, John McRory TWH cross-reference). Clip 1's questioner mentioned Matt Bensfield's prior cathodic-disbondment work at Newport News showing poor performance under laser-ablated surface — clip 3 does not loop back to this thread, but a final-report reader should connect them.

- **Clip 2** (`2026-06-02_clip2-1k-polysiloxane-oxal-free-viability-study.md`) — same panel session, between clips 1 and 3. Different project (polysiloxane coating viability, not laser ablation), but Clip 2 is also self-funded by Newport News and uses the same Newport-News-as-industry-partner pattern. The "Mark" referenced in clip 3's Q&A is the same coatings-side TWH (Mark Ingle, NAVSEA 05; operator-confirmed 2026-06-03) referenced in clip 2's coating-rationale discussion.

- **MegaRust 2026 agenda** (`../agenda-snapshot.md`) — Mark Ingle (NAVSEA 05; agenda lists him with the Wednesday Technical Warrant Holder Update slot) is the "Mark" in this clip's Q&A per operator confirmation. Mark Lattner (NAVSEA 05P, Wednesday morning) is a separate person. John Robinson (SWRMC, Thursday keynote) is operator-team-adjacent but not directly referenced in this clip.

- **BDR entity allowlist** — HII Newport News (and HII MT more broadly) is on the allowlist. Bath Iron Works and Huntington Ingalls are also named in the acknowledgments. The repeated HII-self-funded-partner pattern across this morning's panel is a soft signal worth tracking.

- **Vault glossary candidates** — terms appearing in this clip that may earn a `_meta/glossary.md` entry if they recur: NSRP SPC (NSRP Surface Preparation & Coatings Panel), SIB / MIB (operator should confirm full names), MIL-PRF-23236 (Navy chemical-agent-resistant coating, Type 6 epoxy off-white), SSPC SP-3 / SP-6 / SP-10 / SP-11 (steel-surface-preparation grades — already implicitly in clip 1), AMPP (Association for Materials Protection and Performance — operator-confirmed 2026-06-03; standards body whose spec defines the laser-ablation level taxonomy), MANTEC (ONR program — operator should confirm full name and current branding), HSLA steels (high-strength low-alloy — clip 1 cross-ref), fluence (laser energy density, pulse energy / spot area), local hit cadence (this project's coined parameter).

## Open questions for operator

1. **Speaker identification.** "Missy" is the primary speaker; "Steve" is the analyst presenter. Operator: who is Missy? Who is Steve? Are they from the same vendor / consultancy? (Best candidate based on the project lineage: an MANTEC-experienced laser-ablation analytical firm. The MegaRust attendee list may identify them. See `../agenda-snapshot.md` and the exhibitor list.)

2. ~~**TWH "Mark" identity.**~~ **Resolved 2026-06-03:** Mark = Mark Ingle, NAVSEA 05 (coatings-side TWH).

3. **NSRP panel acronyms — SIB and MIB.** The clip says "we were SIB, then we were MIB, now back to SIB again." Operator: confirm whether these are real NSRP standing panel acronyms (and what they expand to) or Whisper artifacts. SPC is confirmed. Welding and PPPF and Sustainment are mentioned by full name. SIB and MIB are not.

4. ~~**AMP standards body — full expansion.**~~ **Resolved 2026-06-03:** AMPP = Association for Materials Protection and Performance. Standards body developing the laser-ablation surface-cleanliness taxonomy referenced in clips 1 and 3.

5. **Was the Newport News fatigue testing under inorganic zinc primer ever published?** Clip 3 references "previous fatigue data" tied to inorganic-zinc-primer baseline. Operator: is there a public NSRP / MANTEC report from the prior project on this dataset? If yes, it should be referenced in the trip-report final.

6. **MANTEC current status / branding.** Clip references ONR MANTEC. Operator: confirm program is still active under that name (was rebranded once historically per industry-press archives).

7. **Production-rate-by-coating-color as a possible follow-on panel project.** Q&A questioner asked about this and was redirected to a future panel project. Operator: is this a CACI-actionable BD signal (a future NSRP solicitation worth tracking via Opportunity Screening)? If so, the relevant NSRP panel and the typical solicitation pathway should be added to the trip-report final.

8. **Stop-the-beam diagnostic measurements as follow-on work.** Presenters explicitly said this is path-forward work that requires owned (not loaned/rented) equipment. Operator: is there a Navy shipyard or NSWC owning the relevant laser hardware where this could be pursued, or does the project team need to acquire it?

## Source-ledger entry (to be appended to `../source-ledger.md`)

```
### mr26-clip3-pulse-laser-comparison-2026-06-02

- Audio file: LA-near-complete-project.m4a
- Session: NSRP SPC Panel Meeting — Pulse Laser Comparison Tool Near-Complete Project Presentation
- Date / time (local): 2026-06-02 10:38–11:20 (approximate)
- Panelists / speakers: Missy (lead presenter, virtual) and Steve (co-presenter, virtual). Industry partner: James Brooks at HII Newport News Shipbuilding (referenced, not on call). Q&A participants: John McRory (NAVSEA 05 plate TWH, virtual); a coatings-side NAVSEA TWH referred to as "Mark"; one or more unidentified in-room questioners; NSRP SPC panel moderator Conlan Hsu (called "Colin" by speaker).
- Transcription method: faster-whisper, medium.en model, local CPU
- Transcribed: 2026-06-03
- Source file: `01_sources/2026-06-02_clip3-pulse-laser-comparison-tool.md`
- Notes: 42:35 audio, 1246 segments. File renamed by operator from original Voice_*.m4a filename before disk-side processing — original filename not preserved. Transcription artifacts include "MSRP" for "NSRP" (early in clip), "Milperv 23236" for "MIL-PRF-23236", "Coach"/"Colin" for "Conlan" (cross-clip artifact pattern), and "ablation"/"relation" substitution throughout. Operator-confirmed identifications (2026-06-03): the in-Q&A "Mark" is Mark Ingle (NAVSEA 05, coatings-side TWH); AMP → AMPP (Association for Materials Protection and Performance). Remaining unexpanded technical terms (HSLA, SIB, MIB, PPPF, MANTEC) still pending operator confirmation. The TWH split (John McRory plate-side, Mark Ingle coatings-side) is confirmed in Q&A.
```
