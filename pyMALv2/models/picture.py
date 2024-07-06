from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.utils import from_str, from_none, from_union


@dataclass
class Picture:
    medium: Optional[str] = None
    large: Optional[str] = None