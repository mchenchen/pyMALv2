from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.genre import Genre
from pyMALv2.models.utils import from_union, from_int, from_none, from_str


@dataclass
class Serialization:
    id: Optional[int] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Serialization':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj['node'].get("id"))
        name = from_union([from_str, from_none], obj['node'].get("name"))
        return Serialization(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_int, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        return result
