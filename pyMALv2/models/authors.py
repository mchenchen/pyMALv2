from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.author import Author
from pyMALv2.models.utils import from_union, from_none, from_str, to_class


@dataclass
class Authors:
    author: Optional[Author] = None
    role: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Authors':
        assert isinstance(obj, dict)
        author = from_union([Author.from_dict, from_none], obj.get("node"))
        role = from_union([from_str, from_none], obj.get("role"))
        return Authors(author, role)

    def to_dict(self) -> dict:
        result: dict = {}
        result["author"] = from_union([lambda x: to_class(Author, x), from_none], self.author)
        result["role"] = from_union([from_str, from_none], self.role)
        return result
