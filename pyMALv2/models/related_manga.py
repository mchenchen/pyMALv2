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