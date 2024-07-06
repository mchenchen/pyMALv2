from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.utils import from_str, from_none, from_union, from_int


@dataclass
class StartSeason:
    year: Optional[int] = None
    season: Optional[str] = None
