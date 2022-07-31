from dataclasses import dataclass
from typing import Optional, Any, TYPE_CHECKING
if TYPE_CHECKING:
    from .anime import Anime
from .utils import from_str, from_none, from_union, to_class


@dataclass
class RelatedAnime:
    anime: Optional['Anime'] = None
    relation_type: Optional[str] = None
    relation_type_formatted: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RelatedAnime':
        from .anime import Anime  # Can't import at top of file because of circular dependency
        assert isinstance(obj, dict)
        anime = from_union([Anime.from_dict, from_none], obj.get("node"))
        relation_type = from_union([from_str, from_none], obj.get("relation_type"))
        relation_type_formatted = from_union([from_str, from_none], obj.get("relation_type_formatted"))
        return RelatedAnime(anime, relation_type, relation_type_formatted)

    def to_dict(self) -> dict:
        from .anime import Anime  # Can't import at top of file because of circular dependency
        result: dict = {}
        result["anime"] = from_union([lambda x: to_class(Anime, x), from_none], self.anime)
        result["relation_type"] = from_union([from_str, from_none], self.relation_type)
        result["relation_type_formatted"] = from_union([from_str, from_none], self.relation_type_formatted)
        return result
