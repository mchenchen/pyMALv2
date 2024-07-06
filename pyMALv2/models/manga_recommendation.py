from dataclasses import dataclass
from typing import Optional, Any, TYPE_CHECKING
if TYPE_CHECKING:
    from .manga import Manga
from .utils import from_union, from_none, from_int, to_class


@dataclass
class MangaRecommendation:
    manga: Optional['Manga'] = None
    num_recommendations: Optional[int] = None