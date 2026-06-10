# Marine Design and Engineering Services IDIQ (PSNS & IMF) — Decision Log

Every decision: date, decision, by whom, rationale, what changed.

---

### 2026-06-11 — Opportunity opened; grill-me alignment completed before scaffolding

**By:** operator (uploaded the three solicitation documents and directed "scaffold a new folder and get rolling"); alignment run via the **grill-me** skill (`_meta/grill-me.md`) before any folder was created.

**Rationale:** operator brought a live PSNS & IMF Sources Sought (Notice 3059-9900,
Marine Design and Engineering Services IDIQ) and wants both a capability-fit read and
help shaping the 25 July RFI response. Grill-me was run because this produces a
durable artifact in the vault.

**Alignment captured (grill-me):**

- **Folder ID:** `MDES-PSNS` — operator's choice (MDES = Marine Design & Engineering Services; customer = PSNS & IMF).
- **Customer:** PSNS & IMF Code 200 (Engineering Department).
- **Gate:** identify. **Status:** research. **Posture:** undecided — research the fit before committing to prime vs. sub/teaming.
- **Hypothesis (operator-confirmed, open):** there may be a credible CACI role — more likely sub/teaming than prime — in PSNS's marine-design / submarine-modernization engineering work, and it is worth a 25 July RFI response to find out.
- **Focus (both tracks):** (1) research the CACI fit and the competitive/teaming landscape; (2) feed a 25 July Sources Sought response that answers the actual questionnaire.
- **Standing rule (operator-directed):** keep the hypothesis and any draft response **continuously aligned to the Sources Sought PWS, RFI questionnaire, and Q&A documents** in `01_sources/`. Recorded as the "Alignment anchor" callout at the top of the research file.
- **Falsifiers to test early:** (a) CACI lacks submarine-modernization design past performance and cannot team to get it; (b) work is wired to the three incumbents or the small-business set-aside swallows the lane; (c) the Kitsap County 30-day office requirement is an unclearable barrier.
- **Submarine-PP approach:** public USAspending pass first cut, with the explicit operator caveat that **no public hit ≠ no internal past performance** — operator closes the gap internally.
- **Sensitivity:** shareable (documents are public SAM.gov postings); CUI watch the moment work touches anything beyond the public materials (submarine modernization can become sensitive).
- **auto_find:** true — light-touch, directed source support (not the broad discovery crawler); operator holds begin/pause.
- **Cross-links:** capability book ship-design / NAVSEA past performance; operator's Pacific-Navy / PSNS world.

**What changed:** folder `opportunities/MDES-PSNS/` initialized from blank templates;
the three solicitation documents ingested into `01_sources/` (PWS, RFI questionnaire,
Q&A #1) with originals preserved under `01_sources/originals/`; research file seeded
with FACTs cited to those sources (incumbents Tridentis / Gryphon Marine / Huntington Ingalls Industries; the
Kitsap County office requirement; SSN/SSBN scope; the up-to-five-award structure;
25 July / October timeline). Gate-1 (identify) research begun.

**Next:** USAspending past-performance pass for CACI marine-design / submarine-
modernization (NAICS 541330) work + incumbent/teaming award scan; flag results for
operator internal-PP check. Run the named-entity audits between scaffolding and the
first source pass.

---

### 2026-06-11 — Gate upgraded: identify → pursue, prime posture

**By:** operator ("Let's upgrade").

**Rationale:** same-day research knocked down the two hardest barriers on public
evidence. (1) Submarine-modernization credibility — CACI holds analogous past
performance at **Portsmouth Naval Shipyard** (the East-Coast submarine overhaul
yard, peer to PSNS): engineering + **planning** support to SHAPEC and the Deep
Submergence Systems Program for submarine maintenance/repair, >$83M on SeaPort-NxG
[s.2026-06-11-caci-pns-task-order]. (2) The Kitsap County local-presence requirement
— CACI has an existing **Silverdale, WA (Kitsap County) office**
[s.2026-06-11-caci-jobs-silverdale]. CACI also holds general NAICS 541330
engineering-services past performance and runs a naval-architecture / marine-
engineering practice [s.2026-06-11-caci-ship-engineering].

**What changed:** gate identify → **pursue**; recommendation tbd → **pursue-prime**;
posture undecided → **prime**. Research file §6–§7 and index updated. Status stays
*research* until RFI-response drafting begins.

**Residual gaps (do not block the upgrade; close before the RFI response):**
(a) term-level PWS past performance (SIDs / TWDs / ship checks) — confirm from
internal PP; (b) Portsmouth past performance is analogous, not PSNS-specific;
(c) incumbent contract values not yet pulled. Methodology note: a web-search summary
overstated CACI's public capability page; only directly-fetched content is cited
(§9).

**Next:** USAspending PIID lookups on the three incumbent contracts
(N4523A-19-D-1301/1302/1303) for award values; internal-PP confirmation; begin
shaping the 25 July RFI response against the questionnaire.

---

### 2026-06-11 — Incumbent values pulled; v0.1 RFI response + exec summary drafted

**By:** operator directed drafting ("I want RFI response and exec summary drafted")
with a readability constraint (plain English, self-contained, no reference list);
Claude pulled the data and drafted. Light grill-me run before drafting (per
`_meta/grill-me.md`) settled two parameters: RFI = **narrative answers only** (company
data fields handled separately by the operator), exec summary audience = **CACI
internal leadership**.

**Incumbent intel (FACT — USAspending, N4523A line, WA, 2018–2026
[s.2026-06-11-usaspending-n4523a-incumbents]):** Huntington Ingalls ~$20.6M (11 task
orders, via HII Fleet Support Group), Tridentis ~$13.7M (26, most active), Gryphon
Marine ~$0.34M (2, inactive since 2020). Read: two live incumbents, not three; work is
a steady book of ~$0.5–2M engineering task orders; 3→5 award expansion is a real
opening. Written into §5.

**Drafts created:** `_exec-summary-v0.1.md` (~1 page, pursue-prime case for CACI
leadership) and `_rfi-response-v0.1.md` (narrative answers to questionnaire Q2, Q3, Q4,
Q10, Q11; Q12–16 framed for operator fill). Both deliberately citation-free in the
prose per the readability instruction; sourcing stays in the research file. No CACI-
specific facts fabricated — every company-specific blank (and the unverified term-level
shipcheck/SID/TWD past performance) is marked `[NEEDS: …]` for the operator.

**What changed:** status research → **drafting**. next_action handed to operator:
populate the company data fields and the Q12–16 verified past performance, then review
the drafts.

**Standing caveat carried into the drafts:** the customer-facing past-performance
answers must not assert shipcheck/SID/TWD experience CACI cannot substantiate — the
confirmed Portsmouth work is analogous, and the exact-term match is unverified until
the operator's internal check.

---
