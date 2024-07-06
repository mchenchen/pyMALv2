from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.utils import from_str, from_none, from_union, is_type


@dataclass
class Status:
    watching: Optional[int] = None
    completed: Optional[int] = None
    on_hold: Optional[int] = None
    dropped: Optional[int] = None
    plan_to_watch: Optional[int] = None
