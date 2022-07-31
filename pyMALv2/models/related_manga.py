from dataclasses import dataclass
from typing import Optional, Any, TYPE_CHECKING
if TYPE_CHECKING:
    from .manga import Manga
from .utils import from_union, from_none, from_str, to_class


@dataclass
class RelatedManga:
    manga: Optional['Manga'] = None
    relation_type: Optional[str] = None
    relation_type_formatted: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RelatedManga':
        from .manga import Manga  # Can't import at top of file because of circular dependency
        assert isinstance(obj, dict)
        manga = from_union([Manga.from_dict, from_none], obj.get("node"))
        relation_type = from_union([from_str, from_none], obj.get("relation_type"))
        relation_type_formatted = from_union([from_str, from_none], obj.get("relation_type_formatted"))
        return RelatedManga(manga, relation_type, relation_type_formatted)

    def to_dict(self) -> dict:
        from .manga import Manga  # Can't import at top of file because of circular dependency
        result: dict = {}
        result["manga"] = from_union([lambda x: to_class(Manga, x), from_none], self.manga)
        result["relation_type"] = from_union([from_str, from_none], self.relation_type)
        result["relation_type_formatted"] = from_union([from_str, from_none], self.relation_type_formatted)
        return result
