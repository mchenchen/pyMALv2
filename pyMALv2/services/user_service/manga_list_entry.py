import json
from types import SimpleNamespace

from ..list_base import ListBase
from ...auth import Authorization
from ...enums import MangaListEntryStatuses
from ...constants.mal_endpoints import *

class MangaListEntry(ListBase):
    def __init__(self, auth: Authorization, entry_id: int):
        super().__init__(auth)
        self.entry_id = entry_id

    def delete(self):
        self._delete_list_entry(manga=True, manga_id=self.entry_id)

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
        url = MAL_MANGA_LIST_ENTRY_ENDPOINT(self.entry_id)
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
            return json.loads(r.text, object_hook=lambda d: SimpleNamespace(**d))
        else:
            raise Exception(f'Error updating manga list entry: {r.text}')
