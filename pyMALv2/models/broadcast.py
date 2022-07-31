from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.utils import from_str, from_none, from_union


@dataclass
class Broadcast:
    day_of_the_week: Optional[str] = None
    start_time: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Broadcast':
        assert isinstance(obj, dict)
        day_of_the_week = from_union([from_str, from_none], obj.get("day_of_the_week"))
        start_time = from_union([from_str, from_none], obj.get("start_time"))
        return Broadcast(day_of_the_week, start_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["day_of_the_week"] = from_union([from_str, from_none], self.day_of_the_week)
        result["start_time"] = from_union([from_str, from_none], self.start_time)
        return result
