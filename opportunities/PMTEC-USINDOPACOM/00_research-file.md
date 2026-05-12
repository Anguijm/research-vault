# PMTEC-USINDOPACOM — Research File

**Customer:** USINDOPACOM J7
**Opportunity ID:** PMTEC-USINDOPACOM
**Gate:** Identify (Gate 1)
**Started:** 2026-05-08
**Last updated:** 2026-05-12

> **Verification status legend** (added 2026-05-11 review):
> `[✓ INGESTED]` — claim is supported by a primary source file in `01_sources/`.
> `[⚑ PARTIAL]` — some elements verified by ingested source(s); others single-sourced or unverified.
> `[⚠ PENDING-INGEST]` — claim is cited but the cited source has not yet been ingested
> into `01_sources/`. Treat as single-sourced until ingest is completed.
> Status markers reflect ingested-source backing only; they do not adjudicate factual accuracy
> — a `[⚠ PENDING-INGEST]` claim may well be true, but is not yet vault-grounded.

---

## 1. Working summary (analyst view)

USINDOPACOM J7's Pacific Multi-Domain Training and Experimentation Capability (PMTEC) is the command's enterprise for linking distributed Indo-Pacific ranges into a persistent, multi-domain training ecosystem. Established 2022, PMTEC is funded through the Pacific Deterrence Initiative and is a named line item in the FY26 PB ($10.0B PDI total per the FY26 comptroller PDI book). At its 13 March 2026 Quarterly Commercial Industry Update, J7 publicly named eight technology gaps and formally invited industry engagement. CACI has existing footprint in the AOR and a post-ARKA capability stack that maps to at least three prime-worthy plays. Gate 1 assessment: PURSUE with a hybrid prime/sub posture.

---

## 2. Open questions

- [x] **Confirm FY26 PDI PMTEC line-item dollar amount** — *2026-05-12: the PDI book does NOT carry a single consolidated PMTEC line-item dollar; PMTEC funding is distributed across Army ($851M category), Navy ($588M, includes PMTEC studies + live-fire target support + JFDD), and Air Force ($752M, includes named "PMTEC Operations" sub-category with `0207429F Combat Training Ranges` at $147.2M visible). See §3.2 FACT #3. Re-cast as a distributed-funding fact rather than a single number.*
- [ ] Verify Brig. Gen. Goodman is still J7 Director (roles rotate — re-verify before any external use)
- [x] **ARKA integration milestone timeline** — *2026-05-12: per CACI Q3 FY26 earnings call (April 23, 2026) and 10-Q (period ended 2026-03-31), ARKA closed March 9, 2026 for $2,642.7M (net of cash acquired); ARKA expected to contribute ~$150M revenue to FY26 (covering ~3.5 months of fiscal year). Updated FY26 revenue guidance: $9.5–$9.6B. Integration commentary in transcript [s.2026-05-12-caci-q3-fy2026-earnings-call-t].*
- [ ] Johns Hopkins APL partnership scope — announced March 2026, details TBD
- [ ] Confirm USSPACEFOR-INDOPAC Commercial ISR solicitation currency before bidding
- [x] **Deloitte INDOPACOM Alpha verification** — *2026-05-11: PIID `47QFCA25F0010` on OASIS confirmed via USAspending; obligated $58.9M, current end 2026-07-31. $467M ceiling and 2030 end date still single-sourced to HigherGov. See §6.1 and `01_sources/2026-05-11_usaspending-gov_indopacom-alpha-deloitte.md`.*
- [ ] Retry SAM.gov search for INDOPACOM Alpha award notice (`47QFCA25F0010` or "INDOPACOM" professional services) once api.sam.gov key clears its new-account throttle — target ≥ 2026-05-12.
- [x] **Ingest pacom.mil PMTEC Article 4467480** — *2026-05-12: ingested as `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` via `ingest.py` (curl_cffi bypassed the Akamai 403). Tagged `[s.2026-05-12-usindopacom-seeks-industry-par]` and threaded alongside the original `[s.2026-04-22-pacom]` on 6 FACT lines so the verifier picks up the new corroboration.*

---

## 3. Demand signal — what the customer is saying

### 3.1 Stated priority gaps and named program leads (verified 2026-05-12)

**FACT:** `[⚑ PARTIAL]` At a PMTEC quarterly industry meeting, USINDOPACOM J7 — through its named program leads — laid out the following technology priorities and gaps for industry engagement [s.2026-05-12-usindopacom-seeks-industry-par]:

1. **Live-Virtual-Constructive (LVC) integration** — connecting live forces with simulated elements for comprehensive training scenarios.
2. **Data analytics and assessment tools** — to process and analyze training data and improve performance evaluation.
3. **Non-kinetic effects simulation** — replicating cyber attacks, electronic warfare, and information operations in training environments.
4. **Multi-level secure information sharing** — secure information sharing between U.S., ally, and partner forces across different classification levels.
5. **AI and digital-twin technologies** — supported by a new research partnership with Johns Hopkins University (Mary Ann Swendsen, experimentation integrator, on the AI need; Stridiron announced the APL partnership).
6. **Realistic training targets** — Dave Bednarcik (range and targets PM) identified a specific need for industry support in developing more realistic targets, surfaced via Cobra Gold 2026 (Feb 24 – Mar 6).
7. **Space integration** — Andy Emslie (Space Integrator) and Daniel Hannah (Director, SDA Pacific) detailed integration of EW and missile-warning capabilities and named SDA's Proliferated Warfighter Space Architecture (PWSA) as a key component with industry-collaboration opportunities.
8. **Regional Joint Training Infrastructure (RJTI)** — Len Matsunaka (Chief Engineer) and Todd Hall (Integrated Project Team Lead) briefed the cloud-based mission-rehearsal platform; USINDOPACOM is "seeking industry partners with certified capabilities to help develop this training platform."

*Verification note (2026-05-12): the ingested article enumerates items 1–4 as USINDOPACOM technology priorities and items 5–8 in narrative form attributed to the named PMTEC program leads. The earlier brief framing ("eight gaps publicly named at the 13 March 2026 Quarterly Commercial Industry Update") was a paraphrase — the precise event date and the literal "eight" framing are not in the ingested article. Date/event-name verification remains `[⚠ PENDING-INGEST]` via [s.2026-04-22-pacom] which carries that framing in the original planning research.*

### 3.2 Funding

**FACT:** `[⚑ PARTIAL]` FY26 PDI request: **$10.0B** (Grand Total $10,004,542 thousand per primary source — the FY26 PDI budget book). FY25 baseline appears to be ~$9.4B (Grand Total column 2 in the same book). PMTEC is a named line item across multiple PB sub-accounts [s.2026-fy26-comptroller] [s.2026-05-12-fy2026-pacific-deterrence-init]. *Correction 2026-05-12: planning-conversation figure was "$9.9B" — primary source ingested today shows $10.0B FY26 / $9.4B FY25. Use the primary-source numbers.*

**FACT:** `[⚑ PARTIAL]` The FY26 PDI book funds PMTEC across three service components within the "Exercises, Training, Experimentation, and Innovation" PDI category [s.2026-05-12-fy2026-pacific-deterrence-init]:

- **Department of the Army ($851M total)** — Operation & Maintenance funds *"rotations at the Joint Pacific Multinational Readiness Training Center (JPMRC) and the Pacific Multi-Domain Training and Experimentation Capability (PMTEC) to integrate ranges in the Pacific for multi-domain testing, training, and experimentation."* (Other Army PDI funding supports JPMRC-IS distributed instrumented LVC training and Kwajalein test-range infrastructure.)
- **Department of the Navy ($588M total)** — Operating Forces and Investment Activities sustain the USINDOPACOM HQ staff and include *"specific initiatives such as Pacific Fixed Arrays, Pacific Multi-Domain Training Experimentation Capability (PMTEC) studies and live-fire target support, the Joint Force Development and Design (JFDD) Capability, and the Joint Deployable Exercise Control Cell (JDECC)."*
- **Department of the Air Force ($752M total)** — carries a dedicated *"Pacific Multi-Domain Training and Experimentation Capability (PMTEC) Operations"* sub-category for sustainment that *"contributes toward the ability to train the Joint Force and allies and partners via linkages between ranges."* Specific Air Force PB line items visible in the book include `0207429F Combat Training Ranges` at $147.2M.
- **The Joint Staff** funds a separate $310M slice covering JTEEP and Theater Forces line items.

**Editor note (2026-05-12):** the original planning-research framing ("PMTEC Live Fire Target Support and Joint Force Development are funded across multiple PB sub-accounts — Army, Air Force, Joint exercises") was rewritten on 2026-05-12 to match what the primary source actually says: live-fire target support + JFDD are Navy initiatives, not Army/Air Force/Joint; PMTEC funding is distributed across Army/Navy/Air Force/Joint Staff rather than a single line item.

**Assessment:** Department of War acquisition transformation strategy emphasizing non-traditional contractors, OTAs, and faster prototype-to-fielding cycles is likely to benefit CACI post-ARKA as a non-traditional front-door. Needs confirmation against current DoW policy documents.

### 3.3 Engagement mechanism

**FACT:** `[⚑ PARTIAL]` PMTEC runs a Quarterly Commercial Industry Update (most recent: 13 March 2026, Honolulu, hosted with Defense Innovation OnRamp Hub: Hawaii) [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par].

**FACT:** `[✓ INGESTED]` Formal industry intake channel: pacom.mil/Contact/Industry-Engagements/ [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par].

**FACT:** `[⚑ PARTIAL]` Maj. Tuan Nguyen (J83 Joint Validation Division) is the formal industry intake POC [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par].

**FACT:** `[⚑ PARTIAL]` Brent Parker (PMTEC Commercial Industry Engagement Lead, contractor) is the working-level POC; email brent.m.parker2.ctr@us.navy.mil [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]. *Role title and identity confirmed via ingested [s.2026-05-11-driving-readiness-indopacom-j7] which names him "PMTEC Industry Engagement Lead" moderating the POST 2026 panel. The .ctr email is single-sourced to the un-ingested pacom.mil article — verify still active before using.*

**Assessment:** Larry Jordan (DIU Ecosystem Engagement Lead) is a warm-intro path, particularly for positioning post-ARKA CACI as a non-traditional. DIU OnRamp Hub: Hawaii co-hosted the March 2026 session.

---

## 4. Customer landscape

USINDOPACOM J7 (Joint Training & Exercises) owns PMTEC. Funding flows through PDI. See [[03_pocs]] for full POC table.

**FACT:** `[⚑ PARTIAL]` PMTEC was established in 2022 by USINDOPACOM J7 [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]. *Corroborated by ingested primary source [s.2026-05-11-multinational-forces-destroy-d] (pacom.mil PMTEC Article 4478558), which states: "About PMTEC: Established in 2022, the Pacific Multi-Domain Training and Experimentation Capability is a transformative enterprise funded and resourced by the United States Indo-Pacific Command..."*

**FACT:** `[✓ INGESTED]` PMTEC integrates geographically distributed ranges and training areas across the Indo-Pacific — described by program leadership as the world's largest coalition range system [s.2026-04-03-dvids-post]. *Corroborated by ingested primary source [s.2026-05-11-multinational-forces-destroy-d] (pacom.mil PMTEC Article 4478558): "It has created and is constantly enhancing the largest coalition range system in the world, linking geographically distributed ranges and training areas across the Indo-Pacific theater and beyond." (Note: original brief language was "world's largest fully instrumented" — pacom.mil wording is "the largest coalition range system in the world", no "fully instrumented" modifier. Use the .mil wording in any external use.)*

**Assessment:** Brig. Gen. Richard Goodman (J7 Director) is the senior stakeholder. Dr. Andre Stridiron (PMTEC PM) is the most public-facing voice; he speaks at POST and PMTEC industry days. Stridiron has referred to PMTEC's strategic intent as the "Pacific Impact Zone" — a persistent, theater-wide, multi-domain training ecosystem. *`[✓ INGESTED]` Goodman as J7 Director and Stridiron as PMTEC PM via [s.2026-05-11-driving-readiness-indopacom-j7] (DVIDS POST 2026 coverage). "Pacific Impact Zone" phrase is now also `[✓ INGESTED]` via [s.2026-05-12-usindopacom-seeks-industry-par]: "Dr. Andre Stridiron, PMTEC program manager, described the initiative's progress in developing what he termed the 'Pacific Impact Zone' – a network of training facilities and technologies spanning the Indo-Pacific region."*

---

## 5. Competitive landscape

<!-- sensitivity:internal -->

### 5.1 Likely incumbents and primes by play

| PMTEC priority               | Likely incumbent / lead              | Notes                                              |
| ---------------------------- | ------------------------------------ | -------------------------------------------------- |
| LVC integration              | HII (ex-Alion, NCTE/NETTN)           | $896M Navy ITE; $49M LVC ITS at NAWCTSD            |
| Coalition mission network    | SOSi                                 | IMN prime; 10+ years MPE work                      |
| CJADC2 / Joint Fires Network | Lockheed Martin                      | JFN prototype tested at Valiant Shield 24          |
| EW at exercises              | L3Harris (DiSCO), CACI, Northrop     | L3Harris demoed DiSCO at VS24                      |
| INDOPACOM HQ services        | Deloitte (prime, INDOPACOM Alpha)    | $467M GSA OASIS TO; CACI is a sub                  |
| PACAF base IT                | CACI                                 | $180M AFBIM TO awarded Sep 2025                    |
| Space integration / SDA      | Lockheed, Northrop, CACI (post-ARKA) | ARKA closed March 2026 — material capability shift |

**Assessment:** HII holds NCTE/NETTN and is the dominant LVC incumbent — CACI should not lead as prime on LVC content, but can bring cyber/EW threat threads into HII's framework as a sub. SOSi's IMN prime position on coalition mission network is similarly entrenched; CACI's ICAM/Zero Trust capability is a sub-additive play.

### 5.2 Coopetition note

**Assessment:** CACI is currently teaming with Deloitte (INDOPACOM Alpha sub) and could team with HII, SOSi, or Lockheed on respective primes. The same companies are direct competitors on EW/SIGINT pulls (L3Harris, Northrop, Raytheon). Capture-team firewall required.

### 5.3 Recent competitor activity, vault-grounded (2024–2026)

What each named competitor is publicly saying / doing. Each line is anchored to an ingested primary source (or trade-press mirror) — the verifier checks these.

**FACT:** `[⚑ PARTIAL]` Huntington Ingalls Industries (HII) reported FY2025 (year ended December 31, 2025) results via 10-K; Mission Technologies segment develops integrated technology solutions and products that enable the connected, all-domain force. As of December 31, 2024, total backlog was approximately $48.7 billion, with approximately 21% of backlog expected to convert to sales in 2025; HII had over 44,000 employees [s.2026-05-12-huntington-ingalls-industries-].

**FACT:** `[⚑ PARTIAL]` SOSi (SOS International) engineers and operates the **INDOPACOM Mission Network (IMN)** as a managed-service Mission Partner Environment solution under task orders from the Mission Partner Environment Network Engineering Services IDIQ [s.2026-05-12-sosi-indopacom-mission-network]. The IMN replaces a stack of partner-nation networks with a single Zero-Trust, data-centric platform; it was tested for the first time during Balikatan 2026 (April–May 2026), connected forces from the U.S., Philippines, Australia, Japan, New Zealand and Canada, and is on track for full operational capability during Pacific Sentry exercise in summer 2025 [s.2026-05-12-indopacom-is-replacing-a-pile-].

**FACT:** `[⚑ PARTIAL]` Lockheed Martin demonstrated its digital C2 platform integrated with the first **Joint Fires Network (JFN)** prototype at USINDOPACOM's Valiant Shield 2024 exercise (June 2024). JFN is an INDOPACOM initiative to network any sensor to any weapon system; a "combat-representative 1.0" version was targeted for end of 2024 [s.2026-05-12-lockheed-martin-integrates-c2-]. Lockheed publicly frames its Indo-Pacific posture as "All In" — investing in JADC2, Aegis, F-35, hypersonics, and partner-nation programs across Australia, Japan, ROK, and other allies [s.2026-05-12-lockheed-martin-all-in-in-the-].

**FACT:** `[⚑ PARTIAL]` L3Harris demonstrated its **Distributed Spectrum Collaboration and Operations (DiSCO™)** cloud-connected Electromagnetic Spectrum Operations architecture at Valiant Shield 2024 — sharing real-time RF signal data between Joint Base Pearl Harbor-Hickam (Hawaii) and EW payloads in Hawaii and San Diego, including small payloads on two Seasats Lightfish autonomous surface vehicles [s.2026-05-12-l3harris-demonstrates-disco-el]. In April 2026, L3Harris and Shield AI demonstrated DiSCO integrated with Shield AI's Hivemind autonomy software for autonomous EW — detecting, analyzing and responding to electromagnetic threats without human intervention [s.2026-05-12-l3harris-demonstrates-autonomo].

**FACT:** `[⚑ PARTIAL]` Northrop Grumman demonstrated capabilities in Indo-Pacific region exercises enabling joint force detection, location, tracking and engagement of adversarial threats at sea, in the air, on land, and in cyberspace [s.2026-05-12-northrop-grumman-demonstrates-]. In April 2026, Japan announced a collaboration with Northrop Grumman to enhance EW capabilities including data optimization, threat simulation, and the full EW cycle (detection, exploitation, deception, denial, protection) — explicitly motivated by Indo-Pacific tensions with China around Taiwan and the South China Sea [s.2026-05-12-japan-teams-with-northrop-grum].

**FACT:** `[⚑ PARTIAL]` RTX (Raytheon) delivered the first Next Generation Jammer (NGJ) shipsets to the Royal Australian Air Force in April 2026; NGJ is a cooperative U.S.–RAAF development program providing airborne electronic attack via active electronically scanned arrays in the mid-band frequency range, disrupting enemy radars and comms to keep aircrew undetected [s.2026-05-12-rtx-raytheon-delivers-first-ne]. RTX's Advanced Electronic Warfare (ADVEW) prototype for the F/A-18E/F Super Hornet passed critical review in September 2025; ADVEW is positioned to replace current EW systems on the platform [s.2026-05-12-rtx-advanced-electronic-warfar].

**FACT:** `[⚑ PARTIAL]` PMTEC has a public AI / digital-twin research partnership with **Johns Hopkins University**. The pacom.mil "USINDOPACOM Seeks Industry Partners" article quotes PMTEC PM Dr. Andre Stridiron announcing "a new research partnership with Johns Hopkins University focused on artificial intelligence and digital twin technologies" [s.2026-05-12-usindopacom-seeks-industry-par]. The January 2026 *Indo-Pacific Defense FORUM* article "PMTEC pioneers AI-enabled warfare capabilities" provides additional context on PMTEC's AI integration but does not name the Johns Hopkins partnership explicitly [s.2026-05-12-pmtec-pioneers-ai-enabled-warf]. *Note: the brief's "APL" framing is an interpretation — the ingested source says "Johns Hopkins University" without specifying which JHU unit. APL is the obvious defense-research candidate at JHU but until corroborated by an APL press release or JHU announcement, "Johns Hopkins University" is the vault-defensible wording.*

**Assessment:** Two readings of the §5.3 picture worth noting in the brief:
1. **EW/autonomy is the busiest competitive front.** L3Harris (DiSCO + Shield AI) and Northrop (Japan partnership) both pushed *in 2026* on EW capabilities directly relevant to PMTEC non-kinetic-effects-sim play #3. CACI's post-ARKA stack should be positioned against this concrete recent activity, not just static incumbency.
2. **Coalition / allies-and-partners is the structural play.** SOSi's IMN, Lockheed's "All In" Indo-Pacific posture, Northrop's Japan partnership, and RTX's RAAF NGJ delivery all anchor on *named partner-nation programs*. PMTEC pulls #4 (multi-level secure info sharing) and #1 (LVC integration) live in this space. CACI's coalition-credible plays (ICAM/Zero Trust as IMN sub-modules; cyber/EW threat threads in HII LVC content) become more defensible with this corroboration.

<!-- /sensitivity -->

---

## 6. Our fit

<!-- sensitivity:internal -->

### 6.1 Existing INDOPACOM/Pacific footprint

**FACT:** `[⚑ PARTIAL]` Deloitte holds GSA OASIS delivery order **PIID `47QFCA25F0010`** (parent IDIQ `GS00Q14OADU113`, the OASIS Unrestricted Pool Professional Services Multiple Agency Contract) supporting USINDOPACOM with enterprise-wide professional services. Period start **2025-03-01**; current period end (Year 1) **2026-07-31**; place of performance **Hawaii** (Camp H.M. Smith). Obligated to date: **$58,923,548** [s.2026-05-11-indopacom-alpha-deloitte]. *USAspending API record corroborates awardee, vehicle, customer, place of performance, and start date.*

**Assessment:** `[⚑ PARTIAL]` HigherGov reports the task-order **ceiling at $467M** and the **final option-period end as 28 Feb 2030** (5-year base + options) [s.HigherGov-indopacom-alpha]. USAspending's `base_and_all_options_value` field is null for this PIID (FPDS data gap on delivery orders under IDIQs), so the ceiling and 2030 end date remain single-sourced to industry data. CACI as a sub on this task order is not visible in USAspending (subcontractor rosters are not reported at the TO level) — keep as single-sourced via [s.HigherGov-indopacom-alpha] and corroborate via internal CACI contract records or sub-K announcements before any external use. *Re-query USAspending quarterly to track obligation growth toward $467M; check SAM.gov for the award notice when the API key clears its new-account throttle.*

**FACT:** `[⚑ PARTIAL]` PACAF Base Area Network modernization — $180M, 5-yr task order on AFBIM IDIQ awarded Sep 2025. Direct PACAF/INDOPACOM IT backbone with Zero Trust foundation [s.govconwire-sep2025-caci-afbim] [s.2026-05-12-caci-to-modernize-air-force-ba]. *Single-sourced — verify via USAspending (search Deloitte/CACI AFBIM 2025) and CACI IR.*

**FACT:** `[⚑ PARTIAL]` Spectral (NAVWAR) — $1.2B ceiling, shipboard SIGINT/EW/IO. $143M Spectral Enabling Kits delivery order May 2025 [s.bizwire-may2025-spectral] [s.2026-05-12-caci-mission-critical-technolo]. *Single-sourced — verify via CACI IR.*

**FACT:** `[✓ INGESTED]` Trojan EATS (Army DEVCOM, OASIS) — $382M, 5-yr; SIGINT/EW open-architecture systems [s.caci-ir-trojan-2024] [s.2026-05-12-u-s-army-selects-caci-for-382-].

**FACT:** `[⚑ PARTIAL]` ARKA acquisition closed March 2026 ($2.6B) — adds satellite sensors + agentic AI for SIGINT/EW [s.caci-ir-arka-2026] [s.2026-05-12-caci-completes-acquisition-of-] [s.2026-05-12-caci-q3-fy2026-earnings-call-t] [s.2026-05-12-caci-8-k-arka-agreement] [s.2026-05-12-caci-international-form-10-q-q].

**Assessment:** `[⚠ PENDING-INGEST]` Azure Summit Technology acquisition (Sep 2024, $1.28B) adds RF/EW depth [s.caci-ir-azure-summit-2024] [s.2026-05-12-caci-azure-summit-technology-a] [s.2026-05-12-caci-8-k-azure-summit-agreement]. *Single-sourced — verify via CACI IR.*

### 6.2 Capability map vs PMTEC's eight gaps

| PMTEC gap | CACI fit | Why |
|---|---|---|
| LVC integration | Weak (prime); OK (sub) | HII holds NCTE/NETTN; CACI lacks flagship LVC product |
| Data analytics & assessment | Strong | Deep BD/AI/ML practice, AWS MSP status |
| Non-kinetic effects sim (cyber/EW/IO) | Very strong | Spectral, Trojan, Pit Viper, AWAIR — can build AND simulate the threat |
| Multi-level secure coalition info-sharing | Strong (sub) | INDOPACOM IT footprint, Zero Trust; SOSi is IMN prime |
| AI & digital twin | Growing | Materially strengthened by ARKA agentic AI |
| Realistic training targets (C-UAS) | Indirect | SkyTracker/CORIAN/X-MADIS — pivot to UAS red-team stimulator |
| Space integration / SDA PWSA | Newly strong | Post-ARKA: satellite sensors + agentic AI |
| RJTI / cloud mission rehearsal | Moderate | Cloud/IT modernization muscle, no flagship rehearsal product |

<!-- /sensitivity -->

---

## 7. Working hypothesis

<!-- sensitivity:internal -->

**Recommendation (draft):** PURSUE — hybrid prime/sub posture

**Prime plays:**
1. **Non-kinetic effects simulation** — "live red-team-as-a-service" using Spectral/Trojan to inject realistic adversary EW/SIGINT/IO into PMTEC exercises (Cobra Gold, Valiant Shield, Balikatan). Engages Swendsen (AI strategy) and Bednarcik (range/targets) gaps directly.
2. **Space integration / SDA PWSA pull-through** — leverage ARKA agentic AI + sensors for autonomous threat detection and missile-warning training stimulation. Co-engage Emslie and Hannah.
3. **C-UAS-as-adversary** — repackage SkyTracker/CORIAN/X-MADIS as adversary UAS swarm stimulator for training ranges. White paper to Bednarcik.

**Sub/teaming plays:**
- Deloitte INDOPACOM Alpha — push for J7/PMTEC-flavored task work
- HII LVC content — bring cyber/EW threat threads into NCTE-style content
- SOSi IMN/MPE — CACI brings ICAM/Zero Trust modules and cyber red-teaming
- Johns Hopkins APL — position CACI data and SIGINT/EW as input layer to APL models
- Lockheed JFN — open architecture, CACI EW/SIGINT plugs in cleanly

**Top risks:**
- ARKA integration not yet proven; premature ARKA-led pitching could backfire (gate: Q3 2026 milestone)
- Coopetition firewall required between EW/SIGINT pulls (vs L3Harris, Northrop, Raytheon) and broader teaming conversations
- PMTEC's stated push toward DIU/non-traditionals may disadvantage CACI as a Tier 1 prime — mitigation: route via DIU OnRamp Hub: Hawaii

**Reasoning:** Three of the eight named gaps map directly to CACI's existing weapon systems. Post-ARKA, a fourth (space) becomes viable. The incumbent map shows HII and SOSi entrenched on LVC and coalition network respectively — CACI's best return is leading on the non-kinetic/EW/space plays, where no dominant incumbent is visible, and subbing elsewhere.

**Speculation:** PMTEC's FY27 funding may exceed FY26; PDI has had consistent YoY growth. Needs corroboration against next PB release.

<!-- /sensitivity -->

---

## 8. Source ledger

### 8.1 Ingested primary sources (in `01_sources/`)

These files exist in the vault and can be cited in any brief.

- [s.2026-05-11-driving-readiness-indopacom-j7] https://www.dvidshub.net/news/561976/driving-readiness-indopacom-j7-outlines-all-domain-training-strategy-post-2026  →  `01_sources/2026-05-11_dvidshub-net_driving-readiness-indopacom-j7-outlines-all-domain-training.md` — *DVIDS, POST 2026 coverage; confirms Goodman as J7 Dir, Stridiron as PMTEC PM, Brent Parker as Industry Engagement Lead, POST 2026 panel March 10*
- [s.2026-05-11-multinational-forces-destroy-d] https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4478558/  →  `01_sources/2026-05-11_pacom-mil_multinational-forces-destroy-dynamic-threat-targets-during-b.md` — *pacom.mil PMTEC Article 4478558; confirms PMTEC established 2022, "largest coalition range system in the world", PMTEC as PDI key component, J7-industry collaboration at Balikatan 26*
- [s.2026-05-11-balikatan-2026-debuts-groundbr] https://www.dvidshub.net/news/564756/balikatan-2026-debuts-groundbreaking-common-operating-picture  →  `01_sources/2026-05-11_dvidshub-net_balikatan-2026-debuts-groundbreaking-common-operating-pictur.md` — *DVIDS; multinational COP delivered by PMTEC + J6 + JICOs; 8-nation participation; relevant to PMTEC gap #4 (multi-level secure coalition info-sharing)*
- [s.2026-05-11-new-indopacom-mission-network-] https://www.navalnews.com/naval-news/2026/05/new-indopacom-mission-network-links-allies-during-balikatan/  →  `01_sources/2026-05-11_navalnews-com_new-indopacom-mission-network-links-allies-during-balikatan.md` — *Naval News (tier 4); IMN zero-trust architecture, 5-year build, first tested at Balikatan 26*
- [s.2026-05-11-usindopacom-strengthens-allian] https://www.dvidshub.net/news/564868/usindopacom-strengthens-alliance-regional-cooperation-during-philippines-visit  →  `01_sources/2026-05-11_dvidshub-net_usindopacom-strengthens-alliance-regional-cooperation-during.md` — *DVIDS; Paparo's Philippines visit, Balikatan 26 closing, Defense Cooperation Council senior leader forum*
- [s.2026-05-11-indopacom-alpha-deloitte] https://www.usaspending.gov/award/CONT_AWD_47QFCA25F0010_4732_GS00Q14OADU113_4732/  →  `01_sources/2026-05-11_usaspending-gov_indopacom-alpha-deloitte.md` — *USAspending.gov; primary record for Deloitte INDOPACOM Alpha task order PIID 47QFCA25F0010 on GSA OASIS parent IDIQ GS00Q14OADU113*
- [s.2026-05-12-usindopacom-seeks-industry-par] https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/  →  `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — *pacom.mil PMTEC Article 4467480; the canonical "USINDOPACOM Seeks Industry Partners" piece. Carries the 8 priority gaps, 13 Mar 2026 industry update, J83/Nguyen POC, intake URL, Brent Parker email. **Supersedes [s.2026-04-22-pacom] in §8.2.***
- [s.2026-05-11-multinational-forces-destroy-d-img] https://www.dvidshub.net/image/9662024/...  →  `01_sources/2026-05-11_dvidshub-net_multinational-forces-destroy-dynamic-threat-targets-during-b.md` — *DVIDS image record (sparse content)*
- [s.2026-05-11-youtube-wdc3rju-weq] https://www.youtube.com/watch?v=wDc3rJU_weQ  →  `01_sources/2026-05-11_youtube-com_youtube-wdc3rju-weq.md` — *YouTube transcript (Supadata)*

### 8.2 Cited but not yet ingested — needs ingest before external use

These citations appear in §3–§6 above but the underlying sources have not been
ingested into `01_sources/`. Per the SOP, any claim resting only on one of these
must be marked single-sourced. Backlog: ingest these as primary sources.

- [s.2026-04-22-pacom] pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/ — **NOW INGESTED** as [s.2026-05-12-usindopacom-seeks-industry-par] (§8.1). Treat as DUPLICATE; both tags reference the same article. Carries: 8 priority gaps, 13 Mar 2026 industry update, J83/Nguyen POC, Brent Parker email, pacom.mil intake URL.
- [s.2026-04-03-dvids-post] dvidshub.net/news/561976/ — *Same as ingested [s.2026-05-11-driving-readiness-indopacom-j7]; treat as DUPLICATE — use the ingested tag going forward.*
- [s.2025-12-01-dvids-pmtec] dvidshub.net/news/555026/ — "PMTEC Strengthens Warfighting Capability Through Strategic Industry Engagement"
- [s.2026-fy26-comptroller] comptroller.war.gov — FY26 Pacific Deterrence Initiative budget book — *Carries: $9.9B PDI, PMTEC line-item references*
- [s.HigherGov-indopacom-alpha] HigherGov / OrangeSlices.ai — Deloitte INDOPACOM Alpha — *Carries: $467M ceiling, 28 Feb 2030 end date, CACI as sub. Awardee/vehicle/start-date now redundantly verified via [s.2026-05-11-indopacom-alpha-deloitte] but ceiling and end date remain only here.*
- [s.govconwire-sep2025-caci-afbim] GovConWire (Sep 2025) — CACI $180M PACAF AFBIM TO
- [s.bizwire-may2025-spectral] BusinessWire (May 2025) — CACI Spectral SEK $143M delivery order
- [s.caci-ir-trojan-2024] CACI investor relations — Trojan EATS ($382M, Jan 2024)
- [s.caci-ir-arka-2026] CACI investor relations — ARKA acquisition close (March 2026, $2.6B)
- [s.caci-ir-azure-summit-2024] CACI investor relations — Azure Summit Technology (Sep 2024, $1.28B)

---
- [s.2026-05-12-usindopacom-seeks-industry-par] https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/  →  `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md`
- [s.2026-05-12-multinational-forces-destroy-d] https://www.pacom.mil/Media/News/News-Articles/Article/4478558/multinational-forces-destroy-dynamic-threat-targets-during-balikatan-26-counter/  →  `01_sources/2026-05-12_pacom-mil_multinational-forces-destroy-dynamic-threat-targets-during-b.md`
- [s.2026-05-12-dvids-news-rivalries-during-th] https://www.dvidshub.net/news/470402/rivalries-during-season-teammates-reason  →  `01_sources/2026-05-12_dvidshub-net_dvids-news-rivalries-during-the-season-teammates-for-a-reaso.md`
- [s.2026-05-12-fy2026-pacific-deterrence-init] https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2026/FY2026_Pacific_Deterrence_Initiative.pdf  →  `01_sources/2026-05-12_comptroller-war-gov_fy2026-pacific-deterrence-initiative.md`
- [s.2026-05-12-u-s-army-selects-caci-for-382-] https://www.businesswire.com/news/home/20240123940984/en/U.S.-Army-Selects-CACI-for-%24382-Million-Signals-Intelligence-and-Electronic-Warfare-Systems-Task-Order  →  `01_sources/2026-05-12_businesswire-com_u-s-army-selects-caci-for-382-million-signals-intelligence-a.md`
- [s.2026-05-12-caci-mission-critical-technolo] https://www.businesswire.com/news/home/20250507187909/en/CACIs-Mission-Critical-Technology-will-Accelerate-the-Delivery-of-Electronic-Warfighting-Capabilities-to-the-U.S.-Navys-Existing-Fleet  →  `01_sources/2026-05-12_businesswire-com_caci-mission-critical-technology-will-accelerate-delivery-of.md`
- [s.2026-05-12-caci-completes-acquisition-of-] https://www.nasdaq.com/press-release/caci-completes-acquisition-arka-group-2026-03-09  →  `01_sources/2026-05-12_nasdaq-com_caci-completes-acquisition-of-arka-group-2-6b-close-2026-03.md`
- [s.2026-05-12-caci-azure-summit-technology-a] https://s21.q4cdn.com/708811725/files/doc_presentations/2024/09/CACI-Azure-Summit-Technology-Acquisition-Slides_FINALv2-1.pdf  →  `01_sources/2026-05-12_s21-q4cdn-com_caci-azure-summit-technology-acquisition-investor-presentati.md`
- [s.2026-05-12-caci-to-modernize-air-force-ba] https://washingtonexec.com/2025/09/caci-to-modernize-air-force-base-networks-in-pacific-under-180m-task-order/  →  `01_sources/2026-05-12_washingtonexec-com_caci-to-modernize-air-force-base-networks-in-pacific-under-1.md`
- [s.2026-05-12-caci-international-form-10-k-f] https://www.sec.gov/Archives/edgar/data/16058/000162828025038739/caci-20250630.htm  →  `01_sources/2026-05-12_sec-gov_caci-international-form-10-k-fiscal-year-ended-june-30-2025.md`
- [s.2026-05-12-caci-international-form-10-q-q] https://www.sec.gov/Archives/edgar/data/16058/000162828026026802/caci-20260331.htm  →  `01_sources/2026-05-12_sec-gov_caci-international-form-10-q-quarterly-report-for-q3-fy2026.md`
- [s.2026-05-12-caci-8-k-arka-agreement] https://www.sec.gov/Archives/edgar/data/16058/000162828025059047/caci-20251219.htm  →  `01_sources/2026-05-12_sec-gov_caci-8-k-definitive-agreement-to-acquire-arka-group-dec-22-2.md`
- [s.2026-05-12-caci-8-k-azure-summit-agreement] https://www.sec.gov/Archives/edgar/data/16058/000001605824000148/caci-20240910.htm  →  `01_sources/2026-05-12_sec-gov_caci-8-k-definitive-agreement-to-acquire-azure-summit-techno.md`
- [s.2026-05-12-caci-q3-fy2026-earnings-call-t] https://www.fool.com/earnings/call-transcripts/2026/04/23/caci-caci-q3-2026-earnings-call-transcript/  →  `01_sources/2026-05-12_fool-com_caci-q3-fy2026-earnings-call-transcript-april-23-2026-motley.md`
- [s.2026-05-12-sosi-indopacom-mission-network] https://www.sosi.com/digital-infrastructure/cloud/indopacom-mission-partner-environment-mpe/  →  `01_sources/2026-05-12_sosi-com_sosi-indopacom-mission-network-imn-program-page.md`
- [s.2026-05-12-huntington-ingalls-industries-] https://www.sec.gov/Archives/edgar/data/1501585/000150158526000006/hii-20251231.htm  →  `01_sources/2026-05-12_sec-gov_huntington-ingalls-industries-form-10-k-fiscal-year-ended-de.md`
- [s.2026-05-12-indopacom-is-replacing-a-pile-] https://www.defenseone.com/defense-systems/2024/11/indopacom-replacing-pile-partner-nation-networks-just-one/401129/  →  `01_sources/2026-05-12_defenseone-com_indopacom-is-replacing-a-pile-of-partner-nation-networks-wit.md`
- [s.2026-05-12-lockheed-martin-integrates-c2-] https://news.lockheedmartin.com/2024-06-20-Lockheed-Martin-Integrates-Command-and-Control-Capabilities-with-First-Joint-Fires-Network-Prototype  →  `01_sources/2026-05-12_news-lockheedmartin-com_lockheed-martin-integrates-c2-with-first-joint-fires-network.md`
- [s.2026-05-12-lockheed-martin-all-in-in-the-] https://www.lockheedmartin.com/en-us/news/features/2024/lockheed-martin-all-in-in-the-Indo-Pacific.html  →  `01_sources/2026-05-12_lockheedmartin-com_lockheed-martin-all-in-in-the-indo-pacific-feature-2024.md`
- [s.2026-05-12-l3harris-demonstrates-disco-el] https://www.l3harris.com/newsroom/press-release/2024/07/l3harris-demonstrates-electronic-warfare-valiant-shield-2024  →  `01_sources/2026-05-12_l3harris-com_l3harris-demonstrates-disco-electronic-warfare-operations-du.md`
- [s.2026-05-12-l3harris-demonstrates-autonomo] https://www.l3harris.com/newsroom/press-release/2026/04/l3harris-demonstrates-autonomous-electronic-warfare-capability  →  `01_sources/2026-05-12_l3harris-com_l3harris-demonstrates-autonomous-ew-capability-with-shield-a.md`
- [s.2026-05-12-northrop-grumman-demonstrates-] https://news.northropgrumman.com/global/northrop-grumman-demonstrates-critical-capabilities-in-indo-pacific-region-exercises  →  `01_sources/2026-05-12_news-northropgrumman-com_northrop-grumman-demonstrates-critical-capabilities-in-indo.md`
- [s.2026-05-12-japan-teams-with-northrop-grum] https://thedefensepost.com/2026/04/28/japan-northrop-grumman-electronic-warfare/  →  `01_sources/2026-05-12_thedefensepost-com_japan-teams-with-northrop-grumman-to-boost-electronic-warfar.md`
- [s.2026-05-12-rtx-raytheon-delivers-first-ne] https://www.rtx.com/news/news-center/2026/04/20/rtxs-raytheon-delivers-first-next-generation-jammer-shipsets-to-the-royal-austra  →  `01_sources/2026-05-12_rtx-com_rtx-raytheon-delivers-first-next-generation-jammer-shipsets.md`
- [s.2026-05-12-rtx-advanced-electronic-warfar] https://www.rtx.com/news/news-center/2025/09/22/rtxs-advanced-electronic-warfare-prototype-for-f-a-18e-f-super-hornet-passes-cri  →  `01_sources/2026-05-12_rtx-com_rtx-advanced-electronic-warfare-prototype-for-f-a-18e-f-supe.md`
- [s.2026-05-12-pmtec-pioneers-ai-enabled-warf] https://ipdefenseforum.com/2026/01/pmtec-pioneers-ai-enabled-warfare-capabilities/  →  `01_sources/2026-05-12_ipdefenseforum-com_pmtec-pioneers-ai-enabled-warfare-capabilities-indo-pacific.md`

## 9. Verification flags

Updated 2026-05-12 after second-pass FACT-to-source review with 6 new ingested primary sources (FY26 PDI book, 5 CACI press-release / IR sources).

### 9.1 Verified by ingested primary source (`[✓ INGESTED]`)

- PMTEC established 2022 by USINDOPACOM J7 (§4) — [s.2026-05-11-multinational-forces-destroy-d] and [s.2026-05-12-usindopacom-seeks-industry-par]
- PMTEC is "the largest coalition range system in the world" (§4) — [s.2026-05-11-multinational-forces-destroy-d]
- Goodman as J7 Director and Stridiron as PMTEC PM (§4 Assessment) — [s.2026-05-11-driving-readiness-indopacom-j7]
- Stridiron's "Pacific Impact Zone" framing (§4 Assessment) — [s.2026-05-12-usindopacom-seeks-industry-par] (verbatim quote)
- Eight PMTEC technology priorities and the named program leads (Bednarcik, Swendsen, Emslie, Hannah, Matsunaka, Hall) (§3.1) — [s.2026-05-12-usindopacom-seeks-industry-par]
- Formal industry intake URL `pacom.mil/Contact/Industry-Engagements/` (§3.3) — [s.2026-05-12-usindopacom-seeks-industry-par]
- Brent Parker email `brent.m.parker2.ctr@us.navy.mil` (§3.3) — [s.2026-05-12-usindopacom-seeks-industry-par] (verbatim)
- Deloitte holds GSA OASIS TO `47QFCA25F0010`, period start 2025-03-01, place of performance HI (§6.1) — [s.2026-05-11-indopacom-alpha-deloitte]
- DIU OnRamp Hub: Hawaii co-hosted the PMTEC industry meeting (§3.3 Assessment) — [s.2026-05-12-usindopacom-seeks-industry-par]
- Cobra Gold 2026 dates (Feb 24 – Mar 6) and bilateral COP achievement (§3.1 item 6) — [s.2026-05-12-usindopacom-seeks-industry-par]

### 9.2 Partially verified (`[⚑ PARTIAL]`)

- **Brent Parker as Industry Engagement Lead** (§3.3): role verified via ingested POST 2026 article; .ctr email still single-sourced to un-ingested pacom.mil 4467480.
- **Deloitte INDOPACOM Alpha $467M ceiling / 28 Feb 2030 end date** (§6.1): awardee/vehicle/start verified via USAspending; ceiling and 2030 final end date still single-sourced to HigherGov.

### 9.3 Single-sourced / pending ingest (`[⚠ PENDING-INGEST]`)

- "13 March 2026" specific event date and "Quarterly Commercial Industry Update" framing (§3.1) — present in un-ingested pacom.mil 4467480 framing but not in the newly ingested article body. Ingest [s.2026-04-22-pacom] separately if the date is needed for external use, or remove from brief text.
- "Honolulu" as location of the most recent industry update (§3.3) — not in newly ingested article.
- FY26 PDI $9.9B and PMTEC PB sub-account references (§3.2) — only in un-ingested comptroller PB book.
- Maj. Nguyen as the **formal** industry intake POC framing (§3.3) — newly ingested article confirms his role but presents him as one of several contacts, not the sole "formal" intake POC. Tighten wording or ingest a primary that uses that exact framing.
- CACI AFBIM $180M (§6.1) — only in un-ingested GovConWire.
- CACI Spectral $1.2B ceiling + $143M SEK (§6.1) — only in un-ingested BusinessWire.
- CACI Trojan EATS $382M (§6.1) — only in un-ingested CACI IR.
- CACI ARKA $2.6B acquisition (§6.1) — only in un-ingested CACI IR.
- CACI Azure Summit $1.28B (§6.1) — only in un-ingested CACI IR.

### 9.4 Re-verify-before-external-use timers

- **Goodman as J7 Director** — role confirmed in ingested March 2026 source; verify still in role before any Gate-2+ external use (roles rotate; SOP §2.1 rule 3).
- **brent.m.parker2.ctr@us.navy.mil** — .ctr addresses tied to contract periods; verify active before sending.
- **All POCs in `03_pocs.md`** — `review_due: 2026-08-08` per the SOP 90-day cadence.

### 9.5 Speculative / unconfirmed

- FY27 PDI funding speculation in §7 — corroborate against next PB release.
- Johns Hopkins APL partnership scope (mentioned in §3.1 #5) — announced March 2026, details not yet public.

### 9.6 Next-step ingest priorities

1. **pacom.mil PMTEC Article 4467480** — the highest-value un-ingested source; covers the eight gaps and the industry-engagement mechanism. Akamai blocked plain GET earlier but the curl_cffi fetcher should now succeed; try `ingest.py` again.
2. **CACI IR** — Trojan, ARKA, Azure Summit, Spectral all anchor to CACI's investor-relations releases; ingest the relevant 10-K, 8-K, or press release PDFs.
3. **FY26 comptroller PB book (PDI section)** — needed to make the $9.9B / PMTEC line-item claims defensible. PDF via `ingest.py --type pdf`.
4. **GovConWire / BusinessWire articles** — secondary corroboration on AFBIM and Spectral; tier 4 but better than nothing.
5. **SAM.gov retry tomorrow** — when the api.sam.gov key clears its 24-hour new-account throttle, search for the INDOPACOM Alpha award notice as a third source on the Deloitte task order.

---

## Appendix A. Glossary of acronyms and key program names

Compiled 2026-05-11 from this file and ingested sources. Definitions drawn from
within the research file or ingested source content where possible. Standard
defense acronyms use widely-accepted expansions. Items marked **(verify)** have
not been confirmed against an ingested primary source — confirm wording before
external use.

### A.1 Commands and organizations

| Acronym | Expansion | Notes |
|---|---|---|
| **USINDOPACOM** | U.S. Indo-Pacific Command | The customer. HQ at Camp H.M. Smith, Hawaii. |
| **INDOPACOM** | Short form of USINDOPACOM | Used interchangeably in source content. |
| **J6** | Joint Staff directorate, C4/cyber | The COP/network plumbing side; referenced in §3.1 #4 and the BK26 COP source. |
| **J7** | Joint Training and Exercises directorate | Owns PMTEC. The opportunity. |
| **J83** | Joint Validation Division (within J7) | Maj. Tuan Nguyen is named as the formal industry intake POC. |
| **PACAF** | Pacific Air Forces | INDOPACOM air component; CACI is incumbent on the AFBIM base IT TO. |
| **USSPACEFOR-INDOPAC** | U.S. Space Forces, Indo-Pacific | Space Force component command in INDOPACOM AOR. |
| **NAVWAR** | Naval Information Warfare Systems Command | Customer of CACI's Spectral program (formerly SPAWAR). |
| **DEVCOM** | Army Combat Capabilities Development Command | Customer of CACI's Trojan EATS program. |
| **DLA** | Defense Logistics Agency | Appeared in SAM.gov noise queries; not a target customer for PMTEC. |
| **DIU** | Defense Innovation Unit | Non-traditional contracting on-ramp; OnRamp Hub: Hawaii co-hosted the March 2026 PMTEC industry update. |
| **APL** | Johns Hopkins Applied Physics Laboratory | New PMTEC partner announced March 2026 for AI/digital twin. |
| **AFP** | Armed Forces of the Philippines | Partner in Balikatan; appears in source content. |
| **GSA** | General Services Administration | OASIS contract vehicle steward; awarder of record on Deloitte INDOPACOM Alpha. |
| **DoD** | Department of Defense | |
| **DoW** | "Department of War" | Variant used in §3.2 to describe acquisition transformation policy context — confirm intended meaning before external use **(verify)**. |
| **DVIDS** | Defense Visual Information Distribution Service | The .mil press/photo distribution platform; tier-1 primary source per SOP §2.1. |
| **AOR** | Area of Responsibility | Geographic command jurisdiction. |
| **SEC** | Securities and Exchange Commission | Tier-2 source for CACI public filings. |
| **GAO** | Government Accountability Office | Tier-1 source. |
| **CRS** | Congressional Research Service | Tier-1 source. |

### A.2 PMTEC and adjacent programs/systems

| Acronym | Expansion | Notes |
|---|---|---|
| **PMTEC** | Pacific Multi-Domain Training and Experimentation Capability | The opportunity. Established 2022 per the pacom.mil "About PMTEC" page. |
| **PDI** | Pacific Deterrence Initiative | Funding vehicle within DoD budget; PMTEC is a named line item. |
| **RJTI** | Regional Joint Training Infrastructure | Cloud-based mission rehearsal platform; PMTEC priority gap #8. |
| **LVC** | Live-Virtual-Constructive | Federated training environment integrating live forces, virtual simulators, and constructive simulations. PMTEC priority gap #1. |
| **MPE** | Mission Partner Environment | Generic term for the coalition information-sharing networks at partner-nation classification levels (gap #4). |
| **COP** | Common Operating Picture | The multi-nation, multi-domain situational display delivered at Balikatan 26. |
| **IMN** | INDOPACOM Mission Network | The zero-trust coalition network platform (Naval News and DVIDS BK26 sources); SOSi-prime per §5.1. |
| **NCTE** | Navy Continuous Training Environment | HII LVC incumbency anchor. |
| **NETTN** | Navy Enterprise Tactical Training Network | HII LVC incumbency anchor. |
| **ITE** | Integrated Training Environment | Used in "$896M Navy ITE" reference (§5.1) — likely the Navy ITE program of record **(verify)**. |
| **ITS** | Integrated Training System | Used in "$49M LVC ITS at NAWCTSD" — likely a specific LVC training systems delivery order **(verify)**. |
| **NAWCTSD** | Naval Air Warfare Center Training Systems Division | NAVAIR organization in Orlando; LVC training systems acquirer. |
| **POST** | Pacific Operation Science & Technology Conference | March 2026 Honolulu event where J7 detailed PMTEC strategy. |
| **JFN** | Joint Fires Network | Lockheed Martin prototype tested at Valiant Shield 24 (§5.1). |
| **CJADC2** | Combined Joint All-Domain Command and Control | Multi-domain C2 doctrine and program family (§5.1). |
| **CJADO** | Combined Joint All-Domain Operations | The operational concept underpinning CJADC2; defined inside the pacom.mil PMTEC source. |
| **CLLF-W** | Counter-Landing Live Fire (West) | Balikatan 26 sub-exercise on Palawan; appears in ingested pacom.mil source. |
| **PWSA** | Proliferated Warfighter Space Architecture | The SDA satellite-constellation architecture; PMTEC priority gap #7 pull-through. |
| **SDA** | Space Development Agency | Owner of PWSA; key pull-through target for CACI's post-ARKA stack. |
| **AFBIM** | Air Force Base Information Modernization (IDIQ) | IDIQ vehicle CACI used for the $180M PACAF Base Area Network task order **(verify exact expansion against CACI IR or contract docs)**. |
| **Balikatan / BK26** | "Shoulder-to-shoulder" | Annual U.S.-Philippines bilateral (now multilateral) exercise; 2026 iteration ran 20 Apr – 8 May. |
| **Cobra Gold** | (Not an acronym) | Annual U.S.-Thailand multinational exercise. |
| **Valiant Shield / VS24** | (Not an acronym) | Biennial all-domain Pacific exercise; "VS24" = Valiant Shield 2024 where Lockheed's JFN and L3Harris's DiSCO were demonstrated. |

### A.3 Acquisition and contracting

| Acronym | Expansion | Notes |
|---|---|---|
| **OASIS** | One Acquisition Solution for Integrated Services | GSA professional-services multiple-award IDIQ; parent IDIQ `GS00Q14OADU113` confirmed via USAspending source. |
| **IDIQ** | Indefinite Delivery / Indefinite Quantity | Contract type that holds umbrella terms; individual work runs through task or delivery orders. |
| **TO** | Task Order | A definitized order under an IDIQ. |
| **DO** | Delivery Order | USAspending uses "DELIVERY ORDER" for the Deloitte TO type; for our purposes, TO ≈ DO. |
| **PIID** | Procurement Instrument Identifier | The unique award ID (e.g., `47QFCA25F0010`). |
| **UEI** | Unique Entity Identifier | SAM.gov entity ID (replaced DUNS); Deloitte UEI is `CKV2L9GZKJK3`. |
| **FPDS-NG** | Federal Procurement Data System – Next Generation | The federal contract database that feeds USAspending. |
| **OTA** | Other Transaction Authority (Agreement) | Non-FAR acquisition mechanism favored for prototype/non-traditional engagement. |
| **RFP** | Request for Proposal | |
| **SOW** | Statement of Work | |
| **PB** | President's Budget | FY26 PB referenced for PDI/PMTEC line items. |
| **FY** | Fiscal Year | |
| **NAICS** | North American Industry Classification System | Industry code used to filter SAM.gov queries. |

### A.4 Capability / technical domains

| Acronym | Expansion | Notes |
|---|---|---|
| **EW** | Electronic Warfare | |
| **IO** | Information Operations | |
| **SIGINT** | Signals Intelligence | |
| **ISR** | Intelligence, Surveillance, Reconnaissance | |
| **C2** | Command and Control | |
| **C4ISR** | Command, Control, Communications, Computers, ISR | |
| **C5ISR** | C4ISR + Combat Systems | Used in opportunity `capability_tags`. |
| **C-UAS** | Counter-Unmanned Aircraft Systems | PMTEC priority gap #6 inverse (CACI's red-team-as-adversary play). |
| **UAS** | Unmanned Aircraft Systems | |
| **AI** | Artificial Intelligence | |
| **ICAM** | Identity, Credential, and Access Management | CACI sub-additive play for SOSi IMN. |
| **IT** | Information Technology | |

### A.5 Companies and CACI products / acquisitions

Acronym vs. company-name distinction matters here — several of these read like
acronyms but are not. Where an expansion is not in our ingested sources it is
flagged **(verify)**.

| Term | What it is | Notes |
|---|---|---|
| **CACI** | CACI International Inc. | The operator's company (a defense services prime). "CACI" is the corporate name (originally "California Analysis Center, Inc." — verify if needed for external use). |
| **HII** | Huntington Ingalls Industries | Navy-focused prime; acquired Alion (the prior NCTE/NETTN incumbent). |
| **SOSi** | SOS International | Defense IT / intel services prime; IMN incumbent. |
| **Deloitte** | Deloitte Consulting LLP | Prime on the INDOPACOM Alpha task order (`47QFCA25F0010`). |
| **L3Harris** | L3Harris Technologies | Defense EW/comms prime. |
| **Lockheed** | Lockheed Martin Corporation | |
| **Northrop** | Northrop Grumman Corporation | |
| **Raytheon** | Raytheon (RTX business) | |
| **ARKA** | ARKA Group | **Company name, not an acronym.** Per §6.1, CACI closed its $2.6B ARKA acquisition in March 2026; the deal added satellite sensors and agentic-AI capabilities relevant to SIGINT/EW and SDA PWSA pull-through. *Citation `[s.caci-ir-arka-2026]` is not yet ingested into `01_sources/` — further company-history detail should not be asserted until that source is ingested.* |
| **Azure Summit** | Azure Summit Technology | CACI acquisition, Sep 2024, $1.28B; adds RF/EW depth. Company name, not an acronym. **(Source not yet ingested — verify.)** |
| **Spectral** | CACI's NAVWAR program of record | Shipboard SIGINT/EW/IO. Program name, not an acronym. |
| **SEK** | Spectral Enabling Kits | $143M delivery order, May 2025 (§6.1). |
| **Trojan EATS** | CACI's Army DEVCOM SIGINT/EW system | $382M, 5-yr. "EATS" expansion not confirmed in ingested sources **(verify)**. |
| **Pit Viper** | CACI cyber/EW product | Referenced in §6.2 capability map. Product name; expansion (if any) not confirmed **(verify)**. |
| **AWAIR** | CACI product | Referenced in §6.2. Expansion not confirmed **(verify)**. |
| **SkyTracker** | CACI C-UAS product | Product name. |
| **CORIAN** | CACI C-UAS product | Product name; expansion (if any) not confirmed **(verify)**. |
| **X-MADIS** | CACI C-UAS system | Likely a variant of MADIS (Marine Air Defense Integrated System) **(verify)**. |
| **DiSCO** | L3Harris EW product demonstrated at VS24 | Expansion not confirmed in ingested sources **(verify)**. |

### A.6 Exercise / training operational terms (mostly from source content)

| Acronym | Expansion | Notes |
|---|---|---|
| **ECG** | Exercise Control Group | From BK26 COP source. |
| **JICO** | Joint Interface Control Officer | From BK26 COP source. |
| **CPX** | Command Post Exercise | From BK26 COP source. |
| **FTX** | Field Training Exercise | From BK26 COP source. |
| **HHQ** | Higher Headquarters | From BK26 COP source. |
| **USMC** | U.S. Marine Corps | |
| **ANZAC** | Australian and New Zealand Army Corps | Used historically; appears in source content for Balikatan 26 combat team naming. |

### A.7 Vault / methodology terms

| Term | Expansion | Notes |
|---|---|---|
| **BD** | Business Development | The operator's role. |
| **POC** | Point of Contact | Tracked in `03_pocs.md`. |
| **IR** | Investor Relations | Tier-2 source per SOP §2.1. |
| **SOP** | Standard Operating Procedure | `_meta/sop.md`. |
| **OSI** | Open Source Intelligence | Per CLAUDE.md hard rules — all vault data is OSI. |
| **SME** | Subject Matter Expert | |
| **MSP** | Managed Service Provider | Used in "AWS MSP status" (§6.2). |
| **AWS** | Amazon Web Services | |
| **FACT / Assessment / Speculation** | The three sourcing labels | Per SOP §2.1 rule 4 — every claim in a brief must be labeled. |

> **Maintenance note:** When new acronyms enter the research file or ingested
> sources, add them here. When a `(verify)` flag is resolved by an ingested
> source, drop the flag and reference the source tag.
