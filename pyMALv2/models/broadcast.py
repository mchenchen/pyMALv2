from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.utils import from_str, from_none, from_union


@dataclass
class Broadcast:
    day_of_the_week: Optional[str] = None
    start_time: Optional[str] = None