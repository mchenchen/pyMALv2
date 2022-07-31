from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.utils import from_str, from_none, from_union, from_int


@dataclass
class Genre:
    id: Optional[int] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Genre':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return Genre(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_int, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        return result
