---
type: source-ledger
study: world-class-planning
classification: internal
created: 2026-06-23
---

# Source ledger

The grounding documents for this study, all **Distribution Statement A** (approved for public
release; unlimited distribution), so OSI-clean. They live in the operator's Google Drive folder
**`AIM NG`** (folder ID `1ux5NHt1txSvgCDej4jr64L3J6qDiiMeQ`).

To re-pull and re-extract text locally:
`~/.local/whisper-venv/bin/gdown --folder "https://drive.google.com/drive/folders/1ux5NHt1txSvgCDej4jr64L3J6qDiiMeQ" -O /tmp/aim-ng`
then `pdftotext -layout` each PDF.

| Document | What it is |
|----------|-----------|
| NAVSHIPREPFACINST 4700.1F — Availability Management Manual | SRF-JRMC's own availability-management instruction (392 pp). Defines the availability types (CNO, CMAV, WOO, emergent), the work-screening/brokering process, deferral, drydock dependency. The policy backbone for the screen. |
| AIM-NG Chapter 01A — Overview | The AIM-NG process framework; Critical Chain / Theory of Constraints basis; the Standard Work Catalog idea. |
| AIM-NG Chapter 02A — OFS (Organizing for Success) | Team formation/roles. Little estimating content. |
| AIM-NG Chapter 03A — FPL (Financial Planning) | The budget/estimate-maturity ladder (W/X/Y/Z; FRE = ±15% at A-1 month); mandatory-vs-deferrable criteria. |
| AIM-NG Chapter 04A — EPL (Execution Planning) | Builds the Key Event / network backbone; the duration-build rule (longest path of sequenced tasks, not a man-hour sum); buffers defined. |
| AIM-NG Chapter 05A — TPL (Technical Planning) | Where per-work-item labor and CU-Phase duration estimates are computed. |
| AIM-NG Chapter 06A — EPR (Execution Priorities) | The scheduling engine; Critical Chain, buffer sizing/consumption, calendars, float colors. |
| AIM-NG Chapter 07A — EXS (Execution Support) | Job Readiness Cell; material/tool staging; partial release; time-sensitive isolation. |
| AIM-NG Chapter 08A — EXE (Execution) | Doing the work; the "finish what you start" rule; Status-in-Future (interrupt/resume); Cycle Time defined. |
| AIM-NG Chapter 09A — RSA (Resource Allocation) | Resource leveling against Project Workforce Available; the ±20% load band. |
| AIM-NG Chapter 10A — PMC (Performance Measurement & Control) | The earned-value data dictionary; QAC/AQWP, Cost/Schedule Performance, PfCw; the Reference Availability Model. |
| AIM-NG Chapter 11A — PCO (Project Close-Out) | Departure Report return-cost loop; HIT Kit historical store; deferral/incomplete-work disposition. |
| C200 Process Guide (Rev 3) | SRF-JRMC Code 200 (Engineering & Planning) process guide (232 pp). The planning shop's own process: estimate classes (Class F ±40%, Class C ±15%), work breakdown, CU-Phase purity rules, the EM/CM/CMAV breakdown examples. |

## Operator's Qlik work artifacts (2026-06-23, in the same Drive folder)

Four files the operator added — their own AIM/Qlik environment and a build session with Gemini.
Distilled into [the data & tooling note](03_build/data-fields-and-tooling.md); **the raw files are
NOT copied into this git-backed vault** (it pushes to GitHub, and these are live internal AIM
data-model artifacts — a classification/handling call the operator should make before they go
off-machine). They remain in the Drive `AIM NG` folder.

| File | What it is |
|------|-----------|
| KATS data pull load script.txt | The production QlikView load script (the real AIM QVD table/field model, project filter A53, Yokosuka). |
| QLIK Data Dictionary.xlsx | 1,181-field data dictionary (QVD field → source field → definition). The authoritative field reference; shows the published AIM layer **masks NNPI** (`IF NUC_FLAG_CD='Y' THEN 'NNPI Data'`). |
| QLIK data.txt | Field lists of the published `AIM_*.qvd` layer + the operator's MRQT material-readiness dashboard script (Benchmark/Active cohorting). |
| WCP attempt.txt | The operator's conversation with Gemini building the multiplier in Qlik (~3,450 lines). Method held; session blocked on the missing actual-labor field (it's in the COST schema, not AIM). |
