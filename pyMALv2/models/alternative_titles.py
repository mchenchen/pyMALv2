from dataclasses import dataclass
from typing import Optional, List, Any

from pyMALv2.models.utils import from_list, from_str, from_none, from_union


@dataclass
class AlternativeTitles:
    synonyms: Optional[List[str]] = None
    en: Optional[str] = None
    ja: Optional[str] = None