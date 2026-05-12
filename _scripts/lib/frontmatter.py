"""YAML frontmatter builder for source files."""


def _yaml_str(value) -> str:
    """Quote strings that contain YAML-special characters."""
    if value is None or value == "":
        return '""'
    value = str(value)
    special = set(':#{}&*?|>!\'",%@`\n')
    if any(c in value for c in special):
        escaped = value.replace('"', '\\"')
        return f'"{escaped}"'
    return value


def build_frontmatter(
    opportunity: str,
    title: str,
    url: str,
    publisher: str,
    publication_date: str,
    captured: str,
    source_tier: int,
    content_type: str,
) -> str:
    """Return a YAML frontmatter string for a source file."""

    lines = [
        "---",
        f"type: source",
        f"opportunity: {opportunity}",
        f"title: {_yaml_str(title)}",
        f"url: {url}",
        f"publisher: {publisher}",
        f"publication_date: {publication_date or ''}",
        f"captured: {captured}",
        f"captured_by: ingest.py",
        f"source_tier: {source_tier}",
        f"content_type: {content_type}",
        f"key_quotes_extracted: false",
        f"verified: {captured}",
        "---",
    ]
    return "\n".join(lines) + "\n"


def build_sam_frontmatter(opportunity: str, captured: str, candidate: dict) -> str:
    """Return YAML frontmatter for a SAM.gov notice source file.

    Embeds full notice metadata under sam_* keys plus the attachment list
    (each with ingested=false until operator ingests via ingest.py).
    """
    title = candidate.get("title", "")
    url = candidate.get("url", "")
    posted = candidate.get("posted_date", "")
    deadline = candidate.get("response_deadline", "")
    notice_type = candidate.get("notice_type", "")
    set_aside = candidate.get("set_aside") or "None"
    naics = candidate.get("naics") or []
    department = candidate.get("department", "")
    subtier = candidate.get("subtier", "")
    office = candidate.get("office", "")
    notice_id = candidate.get("notice_id", "")
    solnum = candidate.get("solicitation_number", "")
    active = candidate.get("active", "")

    naics_yaml = "[" + ", ".join(_yaml_str(n) for n in naics) + "]" if naics else "[]"

    lines = [
        "---",
        "type: source",
        f"opportunity: {opportunity}",
        f"title: {_yaml_str(title)}",
        f"url: {url}",
        "publisher: sam.gov",
        f"publication_date: {posted}",
        f"captured: {captured}",
        "captured_by: find_sources.py",
        "source_tier: 1",
        "content_type: sam_gov_notice",
        f"sam_notice_id: {notice_id}",
        f"sam_notice_type: {_yaml_str(notice_type)}",
        f"sam_solicitation_number: {_yaml_str(solnum)}",
        f"sam_active: {_yaml_str(active)}",
        f"sam_response_deadline: {deadline}",
        f"sam_set_aside: {_yaml_str(set_aside)}",
        f"sam_naics: {naics_yaml}",
        f"sam_department: {_yaml_str(department)}",
        f"sam_subtier: {_yaml_str(subtier)}",
        f"sam_office: {_yaml_str(office)}",
    ]

    attachments = candidate.get("attachments") or []
    if attachments:
        lines.append("sam_attachments:")
        for a in attachments:
            lines.append(f"  - name: {_yaml_str(a.get('name', 'attachment'))}")
            lines.append(f"    url: {a.get('url', '')}")
            lines.append(f"    ingested: false")
    else:
        lines.append("sam_attachments: []")

    lines += [
        "key_quotes_extracted: false",
        f"verified: {captured}",
        "---",
    ]
    return "\n".join(lines) + "\n"


def build_usaspending_frontmatter(opportunity: str, captured: str,
                                  detail: dict, candidate: dict) -> str:
    """Return YAML frontmatter for an approved USAspending award source file."""
    rcpt = detail.get("recipient") or {}
    aw = detail.get("awarding_agency") or {}
    fa = detail.get("funding_agency") or {}
    pop = detail.get("place_of_performance") or {}
    parent = detail.get("parent_award") or {}

    piid = detail.get("piid") or candidate.get("award_id", "")
    generated_id = candidate.get("generated_id", "")
    title = (detail.get("description") or candidate.get("title", piid))[:140]
    url = f"https://www.usaspending.gov/award/{generated_id}/" if generated_id else ""

    obligation = detail.get("total_obligation") or 0
    ceiling = detail.get("base_and_all_options_value")
    start = detail.get("period_of_performance_start_date") or candidate.get("start_date", "")
    end = detail.get("period_of_performance_current_end_date") or candidate.get("end_date", "")

    lines = [
        "---",
        "type: source",
        f"opportunity: {opportunity}",
        f"title: {_yaml_str(title)}",
        f"url: {url}",
        "publisher: usaspending.gov",
        f"publication_date: {start}",
        f"captured: {captured}",
        "captured_by: find_sources.py",
        "source_tier: 1",
        "content_type: contract_record",
        f"piid: {_yaml_str(piid)}",
        f"generated_id: {_yaml_str(generated_id)}",
        f"recipient_name: {_yaml_str(rcpt.get('recipient_name', ''))}",
        f"recipient_uei: {_yaml_str(rcpt.get('recipient_uei', ''))}",
        f"award_type: {_yaml_str(detail.get('type_description', ''))}",
        f"award_category: {_yaml_str(detail.get('category', ''))}",
        f"total_obligation: {obligation if isinstance(obligation, (int, float)) else 0}",
        f"base_and_all_options_value: {ceiling if isinstance(ceiling, (int, float)) else 'null'}",
        f"period_start: {start}",
        f"period_current_end: {end}",
        f"place_of_performance_state: {_yaml_str(pop.get('state_code', ''))}",
        f"place_of_performance_city: {_yaml_str(pop.get('city_name', ''))}",
        f"awarding_agency: {_yaml_str(aw.get('toptier_agency', {}).get('name', ''))}",
        f"awarding_subtier: {_yaml_str(aw.get('subtier_agency', {}).get('name', ''))}",
        f"funding_agency: {_yaml_str(fa.get('toptier_agency', {}).get('name', ''))}",
        f"funding_subtier: {_yaml_str(fa.get('subtier_agency', {}).get('name', ''))}",
        f"parent_award_piid: {_yaml_str(parent.get('piid', ''))}",
        "key_quotes_extracted: false",
        f"verified: {captured}",
        "---",
    ]
    return "\n".join(lines) + "\n"
