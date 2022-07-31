from dataclasses import dataclass
from typing import Optional, Any, TYPE_CHECKING
if TYPE_CHECKING:
    from .manga import Manga
from .utils import from_union, from_none, from_int, to_class


@dataclass
class MangaRecommendation:
    manga: Optional['Manga'] = None
    num_recommendations: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MangaRecommendation':
        from .manga import Manga  # Can't import at top of file because of circular dependency
        assert isinstance(obj, dict)
        manga = from_union([Manga.from_dict, from_none], obj.get("node"))
        num_recommendations = from_union([from_int, from_none], obj.get("num_recommendations"))
        return MangaRecommendation(manga, num_recommendations)

    def to_dict(self) -> dict:
        from .manga import Manga  # Can't import at top of file because of circular dependency
        result: dict = {}
        result["manga"] = from_union([lambda x: to_class(Manga, x), from_none], self.manga)
        result["num_recommendations"] = from_union([from_int, from_none], self.num_recommendations)
        return result
