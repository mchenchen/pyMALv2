from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.utils import from_str, from_none, from_union, from_int


@dataclass
class StartSeason:
    year: Optional[int] = None
    season: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StartSeason':
        assert isinstance(obj, dict)
        year = from_union([from_int, from_none], obj.get("year"))
        season = from_union([from_str, from_none], obj.get("season"))
        return StartSeason(year, season)

    def to_dict(self) -> dict:
        result: dict = {}
        result["year"] = from_union([from_int, from_none], self.year)
        result["season"] = from_union([from_str, from_none], self.season)
        return result
