from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.genre import Genre
from pyMALv2.models.utils import from_union, from_int, from_none, from_str


@dataclass
class Serialization:
    id: Optional[int] = None
    name: Optional[str] = None
