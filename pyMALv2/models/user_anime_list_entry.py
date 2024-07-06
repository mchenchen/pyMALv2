import json
from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

from ..auth import Authorization
from ..constants.mal_endpoints import MAL_ANIME_LIST_ENTRY_ENDPOINT
from ..enums import AnimeListEntryStatuses
from ..services.base import Base

from .anime import Anime
from .utils import *
from .anime_my_list_status import AnimeMyListStatus


@dataclass
class UserAnimeListEntry(Base):
    anime: Optional['Anime'] = None
    list_status: Optional[AnimeMyListStatus] = None

    def __init__(self, anime, list_status, auth):
        super().__init__(auth)
        self.anime = Anime(**anime)
        self.list_status = AnimeMyListStatus(**list_status)
        
    def delete(self):
        r = self._request('DELETE', MAL_ANIME_LIST_ENTRY_ENDPOINT(self.anime.id))

        if not r.status_code == 200:
            raise Exception(f'Error deleting anime entry: {r.text}')

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
        url = MAL_ANIME_LIST_ENTRY_ENDPOINT(self.anime.id)
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
            self.list_status = AnimeMyListStatus(**r.json())
            return self
        else:
            raise Exception(f'Error updating anime list entry: {r.text}')
