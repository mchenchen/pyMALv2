from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.utils import from_str, from_none, from_union


@dataclass
class Picture:
    medium: Optional[str] = None
    large: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Picture':
        assert isinstance(obj, dict)
        medium = from_union([from_str, from_none], obj.get("medium"))
        large = from_union([from_str, from_none], obj.get("large"))
        return Picture(medium, large)

    def to_dict(self) -> dict:
        result: dict = {}
        result["medium"] = from_union([from_str, from_none], self.medium)
        result["large"] = from_union([from_str, from_none], self.large)
        return result
