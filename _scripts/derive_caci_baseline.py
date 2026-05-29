#!/usr/bin/env python3
"""
derive_caci_baseline.py — Populate the Layer 1 (retrospective CACI baseline)
section of `_meta/caci-discovery-config.yaml` from a USAspending pass on the
configured CACI entities.

For each CACI entity:
  - Query USAspending for contract awards.
  - Aggregate by NAICS code, Product Service Code (PSC), and awarding
    sub-agency.
  - Pull top parent IDV PIIDs (the contracting vehicles CACI has won under).

Writes the aggregated results back into `baseline_caci_footprint` in the YAML
config. Operator does NOT hand-edit Layer 1 — this script owns it.

Usage:
    python derive_caci_baseline.py            # full run, writes config
    python derive_caci_baseline.py --dry-run  # show output, don't write
"""

import argparse
import sys
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path

import yaml
from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
load_dotenv(SCRIPT_DIR / ".env")

from lib import usaspending as usa

CONFIG_PATH = VAULT_ROOT / "_meta" / "caci-discovery-config.yaml"

# Per-entity award fetch limits. USAspending pages at 100/page; we sample
# the top awards by amount per entity. 200 awards per entity is a reasonable
# balance between coverage and runtime.
AWARDS_PER_ENTITY = 200

# Cumulative aggregation thresholds: keep entries that show up in at least
# 2% of CACI awards. Filters out one-off NAICS codes that don't represent
# the actual footprint.
KEEP_THRESHOLD_PCT = 0.02


def _load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


def _save_config(cfg: dict) -> None:
    CONFIG_PATH.write_text(
        yaml.dump(cfg, sort_keys=False, allow_unicode=True, default_flow_style=False, width=120),
        encoding="utf-8",
    )


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _fetch_entity_awards(entity_name: str) -> list[dict]:
    """Fetch top contract awards for a CACI entity from USAspending."""
    filters = {
        "award_type_codes": ["A", "B", "C", "D"],
        "recipient_search_text": [entity_name],
        "time_period": [{"start_date": "2014-01-01", "end_date": date.today().isoformat()}],
    }
    try:
        results = usa.execute_query(filters, max_candidates=min(AWARDS_PER_ENTITY, 100))
    except Exception as e:
        print(f"    ERROR fetching {entity_name}: {e}")
        return []
    return results


def _aggregate(awards: list[dict]) -> dict:
    """Build aggregated NAICS / PSC / agency / parent-PIID distributions from a
    set of award detail records (one fetch_award_by_id per award).
    """
    naics_counter = Counter()
    psc_counter = Counter()
    awarder_counter = Counter()
    funder_counter = Counter()
    parent_piid_counter = Counter()

    for i, award in enumerate(awards, 1):
        gid = award.get("generated_id")
        if not gid:
            continue
        try:
            detail = usa.fetch_award_by_id(gid)
        except Exception:
            continue
        if not detail:
            continue

        latest = detail.get("latest_transaction_contract_data") or {}
        naics = latest.get("naics") or latest.get("naics_code") or ""
        naics_desc = latest.get("naics_description") or ""
        psc = latest.get("product_or_service_code") or ""
        psc_desc = latest.get("product_or_service_description") or ""
        aw = detail.get("awarding_agency") or {}
        fa = detail.get("funding_agency") or {}
        parent = (detail.get("parent_award") or {}).get("piid") or ""

        if naics:
            naics_counter[f"{naics} — {naics_desc}".strip(" —")] += 1
        if psc:
            psc_counter[f"{psc} — {psc_desc}".strip(" —")] += 1
        sub_agency = (aw.get("subtier_agency") or {}).get("name", "")
        if sub_agency:
            awarder_counter[sub_agency] += 1
        funder_sub = (fa.get("subtier_agency") or {}).get("name", "")
        if funder_sub:
            funder_counter[funder_sub] += 1
        if parent:
            parent_piid_counter[parent] += 1

    return {
        "naics": naics_counter,
        "psc": psc_counter,
        "awarder": awarder_counter,
        "funder": funder_counter,
        "parent_piid": parent_piid_counter,
    }


def _keep_top(counter: Counter, total_awards: int) -> list[dict]:
    """Filter a Counter to entries that meet KEEP_THRESHOLD_PCT, return as
    sorted list of dicts."""
    min_count = max(1, int(total_awards * KEEP_THRESHOLD_PCT))
    items = [
        {"label": label, "award_count": count, "share_pct": round(count / total_awards * 100, 1)}
        for label, count in counter.most_common()
        if count >= min_count
    ]
    return items


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="Show output but don't write the YAML.")
    args = ap.parse_args()

    cfg = _load_config()
    entities = cfg.get("baseline_caci_footprint", {}).get("caci_entities", [])
    if not entities:
        print("ERROR: no caci_entities listed in baseline_caci_footprint. Aborting.")
        sys.exit(1)

    print(f"Fetching USAspending data for {len(entities)} CACI entities...")
    all_awards = []
    for entity in entities:
        print(f"  → {entity}")
        awards = _fetch_entity_awards(entity)
        print(f"    {len(awards)} awards")
        all_awards.extend(awards)
    print(f"Total awards across entities: {len(all_awards)}")

    if not all_awards:
        print("ERROR: no awards returned. Aborting.")
        sys.exit(1)

    print("Aggregating detail (this calls fetch_award_by_id per award)...")
    aggregated = _aggregate(all_awards)
    total = len(all_awards)

    customer_orgs = _keep_top(aggregated["awarder"], total) + _keep_top(aggregated["funder"], total)
    # dedup by label
    seen_labels = set()
    customer_orgs_dedup = []
    for c in customer_orgs:
        if c["label"] not in seen_labels:
            customer_orgs_dedup.append(c)
            seen_labels.add(c["label"])

    naics_top = _keep_top(aggregated["naics"], total)
    psc_top = _keep_top(aggregated["psc"], total)
    work_types = naics_top + psc_top
    vehicles = _keep_top(aggregated["parent_piid"], total)

    cfg["baseline_caci_footprint"]["last_derived_utc"] = _utc_now()
    cfg["baseline_caci_footprint"]["customer_orgs"] = customer_orgs_dedup
    cfg["baseline_caci_footprint"]["work_types"] = work_types
    cfg["baseline_caci_footprint"]["vehicles"] = vehicles
    cfg["last_full_update_utc"] = _utc_now()

    print()
    print(f"Layer 1 — customer_orgs: {len(customer_orgs_dedup)} entries")
    for c in customer_orgs_dedup[:10]:
        print(f"  {c['share_pct']:5.1f}%  {c['label'][:80]}")
    print()
    print(f"Layer 1 — work_types (NAICS + PSC): {len(work_types)} entries")
    for c in work_types[:10]:
        print(f"  {c['share_pct']:5.1f}%  {c['label'][:80]}")
    print()
    print(f"Layer 1 — vehicles (parent IDV PIIDs): {len(vehicles)} entries")
    for c in vehicles[:10]:
        print(f"  {c['share_pct']:5.1f}%  {c['label']}")

    if args.dry_run:
        print("\n(dry-run: not writing config)")
        return

    _save_config(cfg)
    print(f"\n✓ Wrote {CONFIG_PATH.relative_to(VAULT_ROOT)}")


if __name__ == "__main__":
    main()
