---
type: source-ledger
event: MegaRust 2026
created: 2026-06-03
purpose: Citation index for every claim in any MegaRust 2026 trip-report artifact.
---

# Source ledger — MegaRust 2026

Every fact, quote, or assessment in any artifact under `trip-reports/MEGARUST-2026/` must reference an entry below. Add entries as audio clips are ingested.

## Citation format

```
### <citation-slug>

- Audio file: <filename in audio/>
- Session: <verbatim session title>
- Date / time (local): <YYYY-MM-DD HH:MM-HH:MM>
- Panelists / speakers: <names + affiliations>
- Transcription method: <gemini-audio | whisper-local | manual>
- Transcribed: <YYYY-MM-DD>
- Source file: <01_sources/...md>
- Notes: <caveats — audio quality, partial coverage, off-the-record exclusions>
```

## Sources

### mr26-clip1-laser-ablation-impl-2026-06-02

- Audio file: 80b4803b-Voice_260602_101029.m4a
- Session: NSRP SPC Panel Meeting — Laser Ablation Shipyard Implementation Presentation
- Date / time (local): 2026-06-02 10:10–10:21 (approximate)
- Panelists / speakers: NSRP SPC Panel led by Conlan Hsu and Angel Zepeda (NSRP). Presenter unidentified in this clip. Q&A participants: Conlan Hsu, John McRory (virtual).
- Transcription method: faster-whisper, medium.en model, local CPU
- Transcribed: 2026-06-03
- Source file: `01_sources/2026-06-02_clip1-laser-ablation-shipyard-implementation.md`
- Notes: 10:33 audio, 62 segments, clean transcription. Minor artifacts (e.g., "bare steel" → "Bear Steel", "MIL-PRF-23236" → "2-3-2-3-6", "disbondment" → "despondment") noted in the source file's FACT-quoted section.

### mr26-clip2-1k-polysiloxane-2026-06-02

- Audio file: 9fa50ed7-Voice_260602_102216.m4a
- Session: NSRP SPC Panel Meeting — 1K Polysiloxane Oxal-Free Coatings Viability Study Presentation
- Date / time (local): 2026-06-02 10:22–10:37 (approximate)
- Panelists / speakers: NSRP SPC Panel led by Conlan Hsu and Angel Zepeda (NSRP). Presenter: Eric (Elzly Technology, likely). Q&A participants: Glenn (NCP Coatings, likely); one questioner referenced as "Coach" — possible Whisper artifact for "Conlon" (Conlan Hsu).
- Transcription method: faster-whisper, medium.en model, local CPU
- Transcribed: 2026-06-03
- Source file: `01_sources/2026-06-02_clip2-1k-polysiloxane-oxal-free-viability-study.md`
- Notes: 14:20 audio, 189 segments. Several transcription artifacts on technical terms (Whisper rendered "MIL-PRF-24635F" as "PRF24635F" and "middle 2, 4, 6, 3, 5, F-type, 5-com1"; "Elzly Technology" as "LZ Technology"; "NCP Coatings" as "MCP Codings"; "Mark Ingle" as "Mark Ingalls"). Chemical identity of "Oxal/Oxyl" — central project topic — is unresolved on tape and the most important verification item for the operator.

### mr26-clip3-pulse-laser-comparison-2026-06-02

- Audio file: LA-near-complete-project.m4a
- Session: NSRP SPC Panel Meeting — Pulse Laser Comparison Tool Near-Complete Project Presentation
- Date / time (local): 2026-06-02 10:38–11:20 (approximate)
- Panelists / speakers: Missy (lead presenter, virtual) and Steve (co-presenter, virtual). Industry partner: James Brooks at HII Newport News Shipbuilding (referenced, not on call). Q&A participants: John McRory (NAVSEA 05 plate TWH, virtual); a coatings-side NAVSEA TWH referred to as "Mark"; one or more unidentified in-room questioners; NSRP SPC panel moderator Conlan Hsu (called "Colin" by speaker).
- Transcription method: faster-whisper, medium.en model, local CPU
- Transcribed: 2026-06-03
- Source file: `01_sources/2026-06-02_clip3-pulse-laser-comparison-tool.md`
- Notes: 42:35 audio, 1246 segments. File renamed by operator from original Voice_*.m4a filename before disk-side processing — original filename not preserved. Transcription artifacts include "MSRP" for "NSRP" (early in clip), "Milperv 23236" for "MIL-PRF-23236", "Coach"/"Colin" for "Conlan" (cross-clip artifact pattern), and "ablation"/"relation" substitution throughout. Operator-confirmed identifications (2026-06-03): the in-Q&A "Mark" is Mark Ingle (NAVSEA 05, coatings-side TWH); AMP → AMPP (Association for Materials Protection and Performance). Remaining unexpanded technical terms (HSLA, SIB, MIB, PPPF, MANTEC) still pending operator confirmation. The TWH split (John McRory plate-side, Mark Ingle coatings-side) is confirmed in Q&A.

### mr26-clip4-spc-panel-five-pitches-2026-06-02

- Audio file: Voice_260602_104940.m4a
- Session: NSRP SPC Panel Meeting — five back-half project pitches (NATs / Apellix drone / Elzly plasma / Elzly thermal-spray / TIC)
- Date / time (local): 2026-06-02 10:49–11:27 (approximate)
- Panelists / speakers: NSRP SPC Panel moderated by Conlan Hsu. Pitch presenters: Asa Wooster + Steve Kelly + Ron Knight (DCI Defense Group); Jim Kunkle + Jeff Potchen (Apellix / Cro-Co-Tec); Mike Kibler (LZ Technology / Elzly Technology); Eric (Elzly Technology); Tom (TIC lead, last-pitch). In-room interventions: Mark Ingle (NAVSEA 05, coatings-side TWH; operator-confirmed 2026-06-03); Dennis / Denny (atmospheric-plasma deployment-status authority — identity unconfirmed); Kevin Urban (International Zinc Association).
- Transcription method: faster-whisper, medium.en model, local CPU
- Transcribed: 2026-06-03
- Source file: `01_sources/2026-06-02_clip4-spc-panel-five-project-pitches.md`
- Notes: 37:40 audio, ~1170 segments. Transcription quality is clean through approximately the 24-minute mark, then degrades severely from the thermal-spray pitch (~24:00) through the TIC pitch (~29:00–end), producing one-word-per-timestamp fragments. Substantive content of the back-half pitches is partially recoverable but should not be used as direct-quote material without second-source verification. Cross-clip transcription artifacts include "LZ Technology" for "Elzly Technology" (consistent across clips 2 and 4), "SRP" for "NSRP" (consistent across all four clips), and "ablation"/"relation" substitution. Several technical terms are unexpanded on tape and require operator confirmation: COMPASS (NSRP project name?), TIC, QP6, ManTech S2944, NSI references to 32577 / 2138 / 8515, and the "Andoron" and "READS de-encapsulation" Apellix references. The most operationally significant FACT in the clip is Dennis's atmospheric-plasma deployment status statement (fully approved, deployed on ships at sea, down to 3 inches of submarine pressure hull) — worth carrying into both the CACI and SRF audience trip-report drafts.

### mr26-clip5-dod-corrosion-panel-2026-06-02

- Audio file: Voice_260602_130325.m4a
- Session: Department of Defense Corrosion Programs Panel (afternoon plenary) — conference opening admin + cross-service panel (Navy aviation, Marine Corps ground, Air Force, Army)
- Date / time (local): 2026-06-02 13:03–15:03 (approximate; clip starts mid-opening-admin and ends at panel close)
- Panelists / speakers: Conference opening: Dale LaValle (CEO, American Society of Naval Engineers / ASNE), Dave Zilber (MegaRust 2026 Conference Chair), John Mangano (MegaRust 2026 Vice Chair). DOD Corrosion Programs Panel: Lauren Paladino (moderator, Deputy Department of Navy Corrosion Control and Prevention Executive; operator-confirmed 2026-06-03). Panelists: Matt Chu (NAVAIR / FRC SW; operator-confirmed 2026-06-03); Andrew Sheets (Marine Corps / NSWC Carderock); Dr. Walter A. Juzukonis (Air Force AFLCMC; operator-confirmed 2026-06-03); Ty / Todd Chrisman (Army CCP via Jensen & Hughes contractor). Audience-intervention back-half Navy fill-in: Ian Shannon (Combat Air Pack / TYCOM corrosion CCC corrosion analyst; operator-confirmed 2026-06-03 — Matt Chu had to leave mid-panel). Also on Ian Shannon's team: Lt. Cdr. Matt Carbonell. Referenced (not on panel): Mark Lattner (NAVSEA SES); Mark Ingle (NAVSEA 05 coatings TWH); Chuck Babish (Air Force ACIP lead); Paul Chang (current DOD CPO director); Robert Kerwin (previous CPO director); Eric Hertzberg (former LMI cost-of-corrosion analyst); Patrick Cassidy (MegaRust 2026 Technical Program Chair, Elzly Technology); Dr. Theresa Smith (DASA Sustainment, Army); Mr. Courtney Blaustein (Deputy CCP, Army); Vice Admiral Lewis (ASNE President).
- Transcription method: faster-whisper, medium.en model, local CPU
- Transcribed: 2026-06-03
- Source file: `01_sources/2026-06-02_clip5-dod-corrosion-programs-panel.md`
- Notes: 2:00:13 audio, 3692 transcript lines. Transcription quality is broadly clean, with sub-word fragmentation in some audience Q&A sections. Significant Whisper artifacts include "Department of War" for "Department of Defense" (DOD → DOW substitution, recurring throughout); "Fleet Lighting Center" for "Fleet Readiness Center"; "Coercion" for "Corrosion" in places; "NASA" for "NAVSEA" in Dave Zilber's reference to Mark Lattner. Operator-confirmed identifications (2026-06-03) carried into this clip: AMPP (referenced in Dave Zilber's opening admin); Mark Ingle / NAVSEA 05 (cross-clip cross-reference, not directly on panel); TIC (not referenced in this clip). Operator-pending questions: Lauren's last-name spelling; Air Force panelist Walter-vs-Juan identity; CERDA PSTCP acronym expansion; identity of Mr. Laswell and the unidentified audience challenger; whether the TYCOM corrosion CCC representative was a planned fifth panelist or Q&A intervention. The most operationally significant single fact in the clip: the DOD annual cost-of-corrosion report sunset in 2020 and the LMI / Eric Hertzberg data pipeline is no longer available — Paul Chang's restart is "in the works" per Walter's account. This affects how any future CACI brief should treat cost-of-corrosion claims. The Marine Corps Mobile Service Container model (Darwin Australia + Ohio attachment) and Air Force drone-based aircraft corrosion mapping are the two strongest operational analogs in this clip for BDR-style forward-deployed damage-assessment work.

### mr26-clip6-am-composites-session-2026-06-02

- Audio file: Voice_260602_153003.m4a
- Session: Session 1 — Additive Manufacturing and Composites (Day 1 afternoon technical session, parallel track to corrosion-policy track)
- Date / time (local): 2026-06-02 15:30–16:55 (approximate)
- Speakers: Dr. Greg Sweet (Defense Research and Development Canada / DRDC, Naval Sustainment group, CFB Halifax — AM of nickel-aluminum-bronze for Royal Canadian Navy); Dr. Maureen Foley (NSWC Carderock, ISEA — In-Service Engineering Agent — for composite components and polymer AM, 25+ years; operator-confirmed 2026-06-03); James Holman (two roles: PM of the ST-1 Corrosion COP **and separately** employed by SURFMEPP — Surface Maintenance Engineering Planning Program; ST-1 and SURFMEPP are distinct organizations per operator confirmation 2026-06-03). Audience presence likely includes operator (Japan POC question for ST-1 at 01:14:26). Referenced (not present): Steve Struthers (ST-1 Knowledge Manager); Katie Buckley (ST-1 ESC); Captain Scott Tracy (ST-1 sponsor); Kate / Kate Danny (ST-1 PM, cross-coordinator with Carrier Team 1 / CT1); Deborah Melindo (JSNs / APLs work). Note: Holman's morning-meeting recap referenced "Dr. Cooley" on kick-pipe work — operator-confirmed (2026-06-03) this is actually Dr. Foley (Whisper artifact); not a separate person.
- Transcription method: faster-whisper, medium.en model, local CPU
- Transcribed: 2026-06-03
- Source file: `01_sources/2026-06-02_clip6-additive-manufacturing-composites-session.md`
- Notes: 1:23:00 audio (trimmed 2026-06-03 from original 01:25:19; post-session personal audio removed by operator request). 2326 transcript lines. Transcription quality is broadly clean across the technical sessions. Whisper artifacts include "NAP" for "NAB" (nickel-aluminum-bronze) throughout Dr. Sweet's talk, "Nazi" for "NSWC Carderock" / "Cardrock" for "Carderock", "Fole" for "Foley", "Napsio P4" for "NAVSEA P4", "MSN" for "NSN" (National Stock Number), "CERF" for "SURFMEPP" throughout James Holman's segment, "CARES T1" for "CT1 / Carrier Team 1". Operator-confirmed identifications (2026-06-03): SURFMEPP = Surface Maintenance Engineering Planning Program (Holman's home command); CT1 = Carrier Team 1 (also written CARES T1 by Whisper); SEACAT is the canonical name as-spelled (real Navy term, no further expansion needed); PMS 312 = NAVSEA Carrier program office. The audience question at 01:14:26 asking ST-1's Japan POC is almost certainly the operator (J. Anguiano) — James Holman offered to look up the name via shared drive. Items in the clip with direct SRF-JRMC adjacency: Dr. Foley's heated-wire-bend-table-to-every-RMC PCoE deployment (SRF-Japan on the active list per slide evidence); James Holman's ST-1 Pacific-theater footprint (Hawaii, Japan, San Diego) with fresh May-1-2026 contract and 80 new hires; ST-1's first ships being DDG 2.0 mods (East and West Coast).

### mr26-clip7-whats-new-in-coatings-2026-06-03

- Audio file: Voice_260603_080301.m4a
- Slides folder: slides/2026-06-03_whats-new-in-coatings/ (13 operator-captured photos)
- Session: Day-2 morning briefing — opening from ASNE Executive Officer + Vice Admiral Dave Lewis keynote (PAE acquisition reform) + Dave Zilber admin + Mark Lattner Anti-Rust/SWARM Initiative + Mark Ingle Technical Authority Pyramid and specs (009-032, 24596, 16173F, 24712B, Oxsol reformulation)
- Date / time (local): 2026-06-03 08:03–09:35
- Presenters: ASNE Executive Officer (Dale LaValle most likely); Vice Admiral Dave Lewis (ASNE President); Dave Zilber (MegaRust 2026 Conference Chair); Mark Lattner (NAVSEA 05P SES, Anti-Rust Program lead); Mark Ingle (NAVSEA 05P2, coatings TWH at apex of pyramid). Referenced (not on stage): Nate Livesey (Anti-Rust PM Acting); Bob Steele (Deputy Acting); Patrick (the Ranch?); Dr. Bazan; Jim Laudle; Josh Chapman (NCMS); Kylee Fazende (PCoE PM Acting); Howard Castle (acting non-metallic materials TWH + acting EM for corrosion); Aaron Miller (NAVSEA 05Z, just promoted); Jeff Duckworth (Philly, retired); Mr. McAnlis (new at Philly); Ted Lemieux (back at NRL); Ricky Preston Baker (Carderock); Cody Lieberman (took over for Liz Hasselbeck retired); Liz Hasselbeck (retired); Kevin Clutcher (DRPM Subs); Brandon Sparks (DRPM Subs); Gordon Culgin (contractor, teaching NVPI); Allison Jones (back as contractor after DRP, working 009-032); Deb Merlino (NSN expert); Andrew and Warren (work with Marine Corps DERPM); Chad (NAVSEA-side counterpart on the NAVAIR/16173F dispute); Carol Rossler (long-time MegaRust technical chair, passed away winter 2026, replaced by Patrick Cassidy of Elzly); Andy Vazquez (Class 8 persistent preservatives demonstration lead); CAPT Richard Duldulao (NSWC PHD Chief Engineer MIL, Day-2 keynote speaker — see clip 8; Whisper rendered as "DiIulio" in Zilber's intro, operator-confirmed 2026-06-04); Jen Mark (AMPP, corrosion control jeopardy lead, Day-2 afternoon); Matt Chu (NAVAIR, late-pick on 16173F — cross-reference to Day-1 clip 5); James Tagert (NRL, ESTCP WP21-5154 PI on Oxsol-Free — Day-1 clip 2 cross-reference).
- Transcription method: faster-whisper, medium.en model, local CPU
- Transcribed: 2026-06-04
- Source file: `01_sources/2026-06-03_clip7-whats-new-in-coatings.md`
- Notes: 1:32:21 audio, 4700 transcript lines. Transcription quality is broadly clean. Whisper artifacts include "Latner" for "Lattner" (slight); occasional name garbling on Lieberman/Hasselbeck. Operator-confirmed identifications carried into this clip: Mark Lattner (NAVSEA 05P SES); Mark Ingle (NAVSEA 05P2); SURFMEPP (separate from ST-1); CT1 / Carrier Team 1; PCoE / NSWC Carderock institutional hub. Substantive Day-2 findings: (1) Vice Admiral Lewis directly addressed the Day-1 acquisition-sustainment feedback-gap pattern with PAE-reform framing — buyer and sustainer become the same person; (2) Anti-Rust Program / SWARM Initiative is post-launch (kicked off January 2026), with 85 availabilities and 60,000 sq ft of preservation completed plus 3,000+ AM parts deployed; (3) Mark Lattner explicitly engaged the Day-1 Ian Shannon "we call it crack" workforce-civilian-ratchet observation as a managed risk; (4) Standard Item 009-032 FY-28 Change 1 published 31 March 2026 with 49 changes adopted out of 79 proposals; (5) MIL-PRF-16173F publication held from August 2025 to late May 2026 by NAVAIR-vs-NAVSEA format dispute (concretizes Day-1 clip 5 Matt Chu/Mark Ingle "huge conversation" thread); (6) Oxsol = parachlorobenzyl trifluoride (PCBTF), 2019 California Prop 65 listing is the regulatory driver, SCAQMD Rule 1106 is the enforcement vehicle, NRL via ESTCP WP21-5154 (James Tagert) is the reformulation effort — resolves the Day-1 clip 2 "Oxal/Oxyl" thread; (7) DRP-driven vacancies are structural across the pyramid, with three of four named contacts in "Acting" status; (8) Carol Rossler (long-time MegaRust technical chair) passed away winter 2026, replaced by Patrick Cassidy of Elzly Technology mid-planning.

### mr26-clip8-diiulio-material-degradation-2026-06-03

- Audio file: Voice_260603_105026.m4a
- Slides folder: slides/2026-06-03_diiulio-material-degradation/ (12 operator-captured photos)
- Session: Day-2 keynote — CAPT Richard Duldulao (NSWC Port Hueneme Division Chief Engineer, MIL) on "Material Degradation: Threat to Surface Ship Combat Operations"
- Date / time (local): 2026-06-03 10:50–11:37 (47:04 audio)
- Presenter: CAPT Richard Duldulao (NSWC PHD Chief Engineer, MIL) — operator-confirmed 2026-06-04. Whisper rendered the name as "DiIulio" in Dave Zilber's clip-7 intro and as "Doodala" / "Doodle out" / "Cap Ridge, doodle out" / "Captain Doodala" in this clip's transcript.
- Referenced: Tim Tenopir (NSWC PHD Senior Scientist, OOT — Office of Engineering and Technology); Dr. Armen Kvryan (NSWC PHD Chief Scientist, OOT, founder of fall-2026 NATO maritime corrosion event in Turkey); Robin Nussear (NSWC PHD Chief Engineer, CIV); Brendan Krum (Northrop Grumman, builds missile launchers for subs — audience Q on industry feedback loop); "Rusty" and "Andrew Rastas" (ST-1 actives, audience reference); Dave Zilber (intro readout).
- Audio note: Drive collision — there were two files in the Drive named Voice_260603_105026.m4a (one real 91 MB, one empty 0 bytes); pull-by-file-ID workaround documented in memory entry `reference_megarust_drive_phantom_files.md`.
- Transcription method: faster-whisper, medium.en model, local CPU
- Transcribed: 2026-06-04
- Source file: `01_sources/2026-06-03_clip8-diiulio-material-degradation.md`
- Notes: 47:04 audio, 908 transcript lines. Transcription quality is broadly clean; persistent Whisper artifact on Duldulao's surname across the transcript. Key findings (slides + audio combined): (1) FY25 INSURV documented ~900 deficiencies attributed directly to corrosion in combat-systems inspections, of which over 660 degraded mission capability (audio adds the 900 total; slide showed only the 660+ subset); (2) NSWC PHD is the ISEA for most surface ship combat systems and underway replenishment equipment — warfare-systems-side counterpart to NSWC Carderock's HM&E coatings work; (3) Cost data on tape: $14M per SPY-1 array replacement, $450K per FCS MK 99 director replacement, $500K per AEM/S resurfacing; (4) Named hulls with FCS director corrosion replacements: USS Wayne E. Meyer (DDG-108) and USS Cole (DDG-67); (5) "Few seized train bearings in the active fleet" detail (RAM launchers unable to slew) — on tape only, not on slide; (6) NSSMS/RAM On Ship Refurbishment Program (OSRP) — 30-year savings of $25.9M per CVN, $25.1M per LHA/LHD, $21.9M per LPD/LSD vs. Depot Overhaul; OSRP cycle is 3-6 weeks vs. OH 1 year; (7) NSWC PHD has moved away from MIL-PRF-23236 and MIL-PRF-24635 polysiloxane on combat-systems composite structures (AEM/S etc.) in favor of "85285 polysiloxane formula or polyurethane" (likely MIL-PRF-85285); (8) "Some future LPDs don't have AEM/S anymore"; (9) OOT (Office of Engineering and Technology) is NSWC PHD's named within-command advisory function — Tim Tenopir and Dr. Armen Kvryan both work in OOT; (10) Dr. Kvryan founded the fall-2026 NATO maritime corrosion event in Turkey and is on ST-1 (cross-reference to Day-1 clip 6 James Holman); (11) Thermography and fiber-optics are patent-pending NDI technologies in development at NSWC PHD; (12) Tim Tenopir's "ten rolls of duct tape" laser-weapon-prototype-funding anecdote is a second Day-2 surfacing of the proof-of-concept-vs-production-ready acquisition gap (first surfacing: Vice Admiral Lewis's clip-7 PAE-reform keynote); (13) CRADA is the named industry-Navy collaboration pathway for pre-fielding feedback (Tim Tenopir response to Brendan Krum / Northrop Grumman audience Q); (14) ST-1 is recommended as industry-engagement pathway, with Dr. Kvryan as the NSWC PHD ST-1 contact.

### mr26-clip9-robotics-drones-application-tech-2026-06-03

- Audio file: Voice_260603_130038.m4a
- Session: Day-2 afternoon Technical Track #4 — Robotics, Drones, and Advanced Application Technologies for Maritime Corrosion Management
- Date / time (local): 2026-06-03 13:00–14:45 (1:45:04 audio)
- Moderator: Nate Livesey (NAVSEA, Anti-Rust Program PM Acting per clip 7 cross-reference)
- Speakers (four; planned for three per moderator opening, Jim McCarthy substituted for Bart Dima): (1) George Samet (Southwest Research Institute / SwRI, Intelligent Systems Division) — robotics state of the art for maritime corrosion management; (2) **Jim Kunkle (Apellix)** — spray-painting drone technology as force multiplier (operator-confirmed 2026-06-04; Whisper rendered "Apellix" as "PCS" / "Pearl Coast Tech LLC" / "Pellex" / "Pelix" and surname as "Cumble" in this clip; same person as Day-1 clip 4); (3) **Jeff Apt (Edify global business and company manager)** — robotic hull inspection in wet dock using magnetic crawler with pulsed eddy current array and ultrasonic (operator-confirmed 2026-06-04; Whisper rendered "Edify" as "85 Technologies" in moderator intro and as "NFI Robotics" in Apt's self-intro); (4) Jim McCarthy (PPG Protective and Marine Coatings, Director Technical Operations U.S./Canada) — electrostatic coating application (pinch-hitting for Bart Dima).
- Transcription method: faster-whisper, medium.en model, local CPU
- Transcribed: 2026-06-04
- Source file: `01_sources/2026-06-03_clip9-robotics-drones-application-tech.md`
- Notes: 1:45:04 audio, 3770 transcript lines. Transcription quality is broadly clean. Whisper artifacts (operator-confirmed corrections 2026-06-04): "Nate Lucy" for "Nate Livesey"; "Apellix" rendered as "PCS" / "Pearl Coast Tech LLC" / "Pellex" / "Pelix"; surname rendered as "Jim Cumble" for "Jim Kunkle" (same Apellix speaker as Day-1 clip 4); "Edify" rendered as "85 Technologies" and "NFI Robotics" for Jeff Apt's actual company; "MASS-C" for likely "NAVSEA" in Kunkle's QA/QC reference (operator-disposition 2026-06-04 — "QA/QC expectations under NAVSEA standards"). Substantive findings: (1) Anti-Rust Program is actively evaluating four contractor capability categories for SWARM Team integration — Nate Livesey moderating signals program-level industry-evaluation posture; (2) Samet's "data-to-action gap" framing is the structural thread tying all four presentations — current inspection robots collect data but don't assess, plan, execute, or report; (3) Apellix is now a 3-touchpoint pattern in the trip-report (Day-1 clip 4 pitch, Day-2 clip 7 Lattner reference, Day-2 clip 9 30-minute deep dive — Jim Kunkle is the consistent Apellix speaker across all touchpoints); (4) Edify is new to the trip-report — wet-dock pre-haul-out magnetic-crawler NDI with PECA + ultrasonic, citing CBO analysis of 14 years of yard-period data showing dry-dock-overrun patterns as data foundation; (5) PPG is now a named MegaRust contact via Jim McCarthy (Director Tech Ops US/Canada); (6) Jeff Apt's wet-dock NDI use case is operationally complementary to NSWC PHD's clip-8 patent-pending thermography and fiber-optics NDI development; (7) McCarthy's electrostatic-application work sits atop the same coating chemistries Mark Ingle's spec work covers (clip 7 MIL-PRF-24635F polysiloxane); (8) SwRI's Intelligent Systems Division (Samet) is the same SwRI that has SERDP/ESTCP project history per Day-1 web research.

### mr26-clip10-swrmc-robinson-keynote-2026-06-04

- Audio file: Voice_260604_080556.m4a
- Session: Day-3 morning keynote — "Standing up SIMA San Diego"
- Date / time (local): 2026-06-04 08:05–09:01 (55:25 audio)
- Introducer: Dave Zilber (MegaRust 2026 Conference Chair)
- Speaker: John Robinson, Executive Director, Southwest Regional Maintenance Center (SWRMC). 22-year retired Navy commander; SWRMC Executive Director since May 2017; responsible for ~2,000 mil/civ at Naval Station 32nd Street and beyond.
- Q&A speakers: Andy (unidentified); John Mark Woods (local AMPP section chair); Dr. Maureen Foley (NSWC Carderock — direct cross-reference to Day-1 clip 6).
- Transcription method: faster-whisper, medium.en model, local CPU
- Transcribed: 2026-06-05
- Source file: `01_sources/2026-06-04_clip10-swrmc-robinson-keynote.md`
- Slides: `slides/2026-06-04_swrmc-keynote/` (14 photos, 08:12–08:48 local)
- Audio note: Operator paused recording ~3 seconds in the middle (per operator 2026-06-05). No specific timestamp boundary verified without waveform inspection; flagged in source file.
- Notes: 55:25 audio, 614 segments, 1238 transcript lines. Operator paused recording ~3 seconds in the middle (per operator 2026-06-05). Substantive findings: (1) SIMA San Diego (Shore Intermediate Maintenance Activity) stood up today 2026-06-04 at 1430 ceremony at Naval Station 32nd Street Bldg 3116; CNO's December 2025 mandate, NAVSEA chain through Vice Admiral James P. Downey (NAVSEA Commander) and CNRMC's Rear Admiral Daniel L. Lannaman, CO Captain Bill Albert; ~900 military personnel move to SIMA today, all SWRMC military except ~14 EDOs + 1 supply + 1 SWO XO. (2) Direct SRF-Japan operational reference: Robinson stated SWRMC "actually sending project teams for contract oversight, working with SRF Japan, which of course is the area of maintenance coming under out there to support these things" — i.e., expeditionary-maintenance container pre-staging (~50 containers, Pacific-theater battle damage repair prep, Pat McDermott driving). (3) Dr. Maureen Foley directly engaged Robinson in Q&A — Robinson confirmed "you gave us a new machine this week" — i.e., the NSWC Carderock Composite Work Cell equipment Foley described on Day-1 clip 6 was delivered to SWRMC during MegaRust week. Foley reported the machine hasn't been exercised yet; Robinson reported it was missing an arm initially but appears to have been resolved. Cross-reference for SRF-Japan delivery status. (4) Robinson rejected "additive manufacturing" framing in favor of "advanced manufacturing" = CNC + AM + reverse engineering, with reverse engineering as the Achilles' heel. Named DMG MORI (Whisper: "GMG Maury") laser-deposit machine months into commissioning. (5) Capt Kerosich (Whisper artifact, Robinson's CO at SWRMC) is being pressed weekly on AM by Vice Admiral Brendan McLane (Whisper rendered as "McClain"), Commander Naval Surface Forces. (6) Mark Lattner (Day-2 clip 7) cross-reference: Robinson chatted with Lattner that morning about a powder coating scuttle ("better than what's being delivered in new construction"). (The Bahrain diver passage at 27:40 → 27:56 — where Whisper rendered "MARMC" as "Mark" and "co-located/co-owned" as "covert" — references MARMC, not Lattner. Operator-confirmed 2026-06-05.) (7) Whisper artifacts resolved 2026-06-05: SEMA / CIMA → SIMA (operator-confirmed); "Admiral Laniman"/"Landman" → Rear Admiral Daniel L. Lannaman (web-verified); "Vice Admiral McClain" → Vice Admiral Brendan McLane (best match by role); DMG MORI (operator-confirmed). Outstanding (non-blocking): "Spermac"→SURFMEPP, "soup ship"→SUPSHIP, "Comnet Surf Pack"→COMNAVSURFPAC, "ASDA"→AMPP, "screw-in destroyers"→Spruance-class, "Captain Brozich"/"Kerosich" surname disambiguation, "ACL"/"Brad" industry partner (identity not worth chasing per operator).
