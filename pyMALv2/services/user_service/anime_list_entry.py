import json
from types import SimpleNamespace

from ..list_base import ListBase
from ...auth import Authorization
from ...enums import AnimeListEntryStatuses
from ...constants.mal_endpoints import *


class AnimeListEntry(ListBase):

    def __init__(self, auth: Authorization, entry_id: int):
        super().__init__(auth)
        self.entry_id = entry_id

    def delete(self):
        self._delete_list_entry(manga=False, anime_id=self.entry_id)

    def update(
            self,
            status: AnimeListEntryStatuses = None,
            is_rewatching: bool = None,
            score: int = None,
            num_watched_episodes: int = None,
            priority: int = None,
            num_times_rewatched: int = None,
            rewatch_value: int = None,
            tags: str = None,
            comments: str = None,
    ):
        """
        Update an anime list entry.
        """
        url = MAL_ANIME_LIST_ENTRY_ENDPOINT(self.entry_id)
        r = self._request('PATCH', url, data={
            'status': status,
            'is_rewatching': is_rewatching,
            'score': score,
            'num_watched_episodes': num_watched_episodes,
            'priority': priority,
            'num_times_rewatched': num_times_rewatched,
            'rewatch_value': rewatch_value,
            'tags': tags,
            'comments': comments,
        })

        if r.status_code == 200:
            return json.loads(r.text, object_hook=lambda d: SimpleNamespace(**d))
        else:
            raise Exception(f'Error updating anime list entry: {r.text}')

