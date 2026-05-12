"""URL routing and source tier classification."""

from urllib.parse import urlparse


# Domain → source tier.
# 1 = primary .mil/gov  2 = SEC/IR  3 = aggregator
# 4 = trade press        5 = think-tank  6 = blog/social
DOMAIN_TIER_MAP = {
    # Tier 1 — .mil and primary .gov
    "pacom.mil": 1,
    "dvidshub.net": 1,
    "dvids.net": 1,
    "sam.gov": 1,
    "usaspending.gov": 1,
    "comptroller.war.gov": 1,
    "comptroller.defense.gov": 1,
    "gao.gov": 1,
    "congress.gov": 1,
    "crs.congress.gov": 1,
    "defense.gov": 1,
    "diu.mil": 1,
    "spaceforce.mil": 1,
    "army.mil": 1,
    "navy.mil": 1,
    "af.mil": 1,
    "marines.mil": 1,
    "socom.mil": 1,
    "stratcom.mil": 1,
    "centcom.mil": 1,
    "eucom.mil": 1,
    "southcom.mil": 1,
    "northcom.mil": 1,
    "africom.mil": 1,
    "cybercom.mil": 1,
    "transcom.mil": 1,
    "dla.mil": 1,
    "darpa.mil": 1,
    # Tier 2 — SEC filings and official IR
    "sec.gov": 2,
    # Tier 3 — aggregators
    "highergov.com": 3,
    "govtribe.com": 3,
    "orangeslices.ai": 3,
    # Tier 4 — trade press
    "breakingdefense.com": 4,
    "defensenews.com": 4,
    "defensescoop.com": 4,
    "insidedefense.com": 4,
    "executivegov.com": 4,
    "govconwire.com": 4,
    "fedscoop.com": 4,
    "c4isrnet.com": 4,
    "nationaldefensemagazine.org": 4,
    "defensedaily.com": 4,
    "executivebiz.com": 4,
    # Tier 5 — think tanks
    "csis.org": 5,
    "rand.org": 5,
    "cnas.org": 5,
    "hudson.org": 5,
    "aei.org": 5,
}


def get_source_tier(domain: str) -> int:
    """Return the source tier for a domain.

    Any .mil or .gov domain not explicitly listed defaults to tier 1.
    Unknown domains default to tier 4 with a warning printed to stdout.
    """
    clean = _clean_domain(domain)
    if clean in DOMAIN_TIER_MAP:
        return DOMAIN_TIER_MAP[clean]
    if clean.endswith(".mil") or clean.endswith(".gov"):
        return 1
    print(f"WARN: Domain '{clean}' not in DOMAIN_TIER_MAP — defaulting to tier 4. "
          f"Add it to lib/routing.py if this is a known recurring source.")
    return 4


def sanitize_domain(domain: str) -> str:
    """Return a filename-safe domain string: strip www., replace dots with hyphens."""
    return _clean_domain(domain).replace(".", "-")


def _clean_domain(domain: str) -> str:
    domain = domain.lower()
    if domain.startswith("www."):
        domain = domain[4:]
    return domain


def route(url: str, type_override: str = "auto"):
    """Return the fetcher class appropriate for the URL.

    type_override values: auto | article | pdf | youtube
    """
    from lib.fetchers.web import WebFetcher
    from lib.fetchers.pdf import PDFFetcher
    from lib.fetchers.youtube import YouTubeFetcher

    if type_override == "youtube":
        return YouTubeFetcher
    if type_override == "pdf":
        return PDFFetcher
    if type_override in ("article", "web"):
        return WebFetcher

    # Auto-detect from URL
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    path = parsed.path.lower()

    if "youtube.com" in host or "youtu.be" in host:
        return YouTubeFetcher
    if path.endswith(".pdf"):
        return PDFFetcher

    return WebFetcher
