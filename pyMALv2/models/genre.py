from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.utils import from_str, from_none, from_union, from_int


@dataclass
class Genre:
    id: Optional[int] = None
    name: Optional[str] = None
