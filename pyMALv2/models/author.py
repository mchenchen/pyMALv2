from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.utils import from_union, from_int, from_none, from_str


@dataclass
class Author:
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Author':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        first_name = from_union([from_str, from_none], obj.get("first_name"))
        last_name = from_union([from_str, from_none], obj.get("last_name"))
        return Author(id, first_name, last_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_int, from_none], self.id)
        result["first_name"] = from_union([from_str, from_none], self.first_name)
        result["last_name"] = from_union([from_str, from_none], self.last_name)
        return result
