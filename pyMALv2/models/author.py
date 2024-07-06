from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.utils import from_union, from_int, from_none, from_str


@dataclass
class Author:
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None