from dataclasses import dataclass
from typing import Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .anime import Anime
from .utils import from_none, from_union, from_int, to_class


@dataclass
class AnimeRecommendation:
    anime: Optional['Anime'] = None
    num_recommendations: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AnimeRecommendation':
        from .anime import Anime  # Can't import at top of file because of circular dependency
        assert isinstance(obj, dict)
        anime = from_union([Anime.from_dict, from_none], obj.get("node"))
        num_recommendations = from_union([from_int, from_none], obj.get("num_recommendations"))
        return AnimeRecommendation(anime, num_recommendations)

    def to_dict(self) -> dict:
        from .anime import Anime  # Can't import at top of file because of circular dependency
        result: dict = {}
        result["anime"] = from_union([lambda x: to_class(Anime, x), from_none], self.anime)
        result["num_recommendations"] = from_union([from_int, from_none], self.num_recommendations)
        return result
