from dataclasses import dataclass
from typing import Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .anime import Anime
from .utils import from_none, from_union, from_int, to_class


@dataclass
class AnimeRecommendation:
    anime: Optional['Anime'] = None
    num_recommendations: Optional[int] = None
