# Pending-decision documents

Operator-facing decision menus that block progress on a brief or a research direction. Each file is dated and lists the open decisions with A/B/C-style options.

These are not the same as the canonical decision log at `../05_decision-log.md`. The decision log is append-only history. The files in this directory are forward-looking menus: "here are five questions blocking the next brief version, pick one option per question." Once a question is resolved, the answer gets recorded in the decision log and the question gets crossed off here.

Filename convention: `YYYY-MM-DD.md`, or `YYYY-MM-DD-context.md` if there are multiple pending-decision documents on the same day with different scopes.

When every question in a pending-decisions file is resolved, the file either gets deleted (if the resolutions are fully captured in the decision log) or moved to `_resolved/` (if the historical context of the menu is worth preserving). Either move is recorded in the decision log.
