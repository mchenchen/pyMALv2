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