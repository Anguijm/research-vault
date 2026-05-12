from abc import ABC, abstractmethod


class BaseFetcher(ABC):
    """All fetchers must implement fetch() and return a result dict.

    Required keys:
        title (str)         — source title
        content (str)       — cleaned text content in markdown
        content_type (str)  — article | press_release | speech | transcript | pdf | youtube | other

    Optional keys:
        publication_date (str)  — ISO date YYYY-MM-DD, or empty string
        warnings (list[str])    — non-fatal warnings to surface to operator
    """

    def __init__(self, debug: bool = False) -> None:
        self.debug = debug

    @abstractmethod
    def fetch(self, url: str) -> dict:
        ...
