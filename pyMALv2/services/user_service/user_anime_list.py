from ...auth import Authorization
from ..list_base import ListBase
from .anime_list_entry import AnimeListEntry

class UserAnimeList(ListBase):
    def __init__(self, auth: Authorization):
        super().__init__(auth)

    def entry(self, entry_id: int):
        return AnimeListEntry(self.auth, entry_id)

    def get(self, status: str = None, sort: str = None,
            limit: int = 100, offset: int = 0,
            next_url: str = None):
        return self._get_list(manga=False, status=status, sort=sort, limit=limit, offset=offset, next_url=next_url)
