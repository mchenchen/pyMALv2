import json
from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

from ..auth import Authorization
from ..constants.mal_endpoints import MAL_MANGA_LIST_ENTRY_ENDPOINT
from ..enums import MangaListEntryStatuses
from ..services.base import Base

if TYPE_CHECKING:
    from .manga import Manga
from .utils import *
from .manga_my_list_status import MangaMyListStatus


@dataclass
class UserMangaListEntry(Base):
    manga: Optional['Manga'] = None
    list_status: Optional[MangaMyListStatus] = None

    def __init__(self, manga, list_status, auth):
        super().__init__(auth)
        self.manga = manga
        self.list_status = list_status

    @staticmethod
    def from_dict(obj: Any, auth: Authorization) -> 'UserMangaListEntry':
        from .manga import Manga  # Can't import at top of file because of circular dependency
        assert isinstance(obj, dict)
        manga = from_union([Manga.from_dict, from_none], obj.get("node"))
        list_status = from_union([MangaMyListStatus.from_dict, from_none], obj.get("list_status"))
        return UserMangaListEntry(manga, list_status, auth)

    def to_dict(self) -> dict:
        from .manga import Manga  # Can't import at top of file because of circular dependency
        result: dict = {}
        result["manga"] = from_union([lambda x: to_class(Manga, x), from_none], self.anime)
        result["list_status"] = from_union([lambda x: to_class(MangaMyListStatus, x), from_none], self.list_status)
        return result

    def delete(self):
        r = self._request('DELETE', MAL_MANGA_LIST_ENTRY_ENDPOINT(self.manga.id))

        if not r.status_code == 200:
            raise Exception(f'Error deleting manga entry: {r.text}')

    def update(
            self,
            status: MangaListEntryStatuses = None,
            is_rereading: bool = None,
            score: int = None,
            num_volumes_read: int = None,
            num_chapters_read: int = None,
            priority: int = None,
            num_times_rewatched: int = None,
            reread_value: int = None,
            tags: str = None,
            comments: str = None,
    ):
        """
        Update an anime list entry.
        """
        url = MAL_MANGA_LIST_ENTRY_ENDPOINT(self.manga.id)
        r = self._request('PATCH', url, data={
            'status': status,
            'is_rereading': is_rereading,
            'score': score,
            'num_volumes_read': num_volumes_read,
            'num_chapters_read': num_chapters_read,
            'priority': priority,
            'num_times_rewatched': num_times_rewatched,
            'rewatch_value': reread_value,
            'tags': tags,
            'comments': comments,
        })

        if r.status_code == 200:
            self.list_status = MangaMyListStatus.from_dict(json.loads(r.text))
            return self
        else:
            raise Exception(f'Error updating manga list entry: {r.text}')
