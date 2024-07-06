import json
from typing import List, TYPE_CHECKING

from ..base import Base
from ...auth import Authorization
from ...constants.mal_endpoints import MAL_GET_ANIME_LIST_ENDPOINT, MAL_ANIME_LIST_ENTRY_ENDPOINT
from urllib.parse import urlparse, parse_qs

from ...exceptions.AnimeNotFound import AnimeNotFound
from ...models.anime_my_list_status import AnimeMyListStatus
from ...models.user_anime_list_entry import UserAnimeListEntry
from ...models.anime import Anime


class UserAnimeList(Base):
    def __init__(self, auth: Authorization):
        super().__init__(auth)
        self.entries = self._get_list()

    def get(self) -> List['UserAnimeListEntry']:
        """
        Returns a list of all anime entries on the user's anime list.

        :return: A list of anime objects.
        """
        return self.entries

    def update(self, anime: 'Anime', status: str = None, is_rewatching: bool = None, score: int = None,
               num_watched_episodes: int = None, priority: int = None, num_times_rewatched: int = None,
               rewatch_value: int = None, tags: str = None, comments: str = None):
        """
        Adds or updates an anime entry on the user's anime list.

        :param anime: An anime object with at least an id.
        :param status: The watch status of the anime.
        :param is_rewatching: Is currently rewatching the anime.
        :param score: The user's score for the anime.
        :param num_watched_episodes: The number of watched episodes.
        :param priority: The priority of the anime.
        :param num_times_rewatched: The number of times the user has rewatched the anime.
        :param rewatch_value: The rewatch value of the anime.
        :param tags: Tags for this record.
        :param comments: Comments for this record.
        :return:
        """
        self._request('PATCH', MAL_ANIME_LIST_ENTRY_ENDPOINT(anime.id), data={
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
        self.entries = self._get_list()

    def delete(self, id: int):
        """
        Deletes an anime entry on the user's anime list.

        :param id: The id of the anime to delete.
        :return: None
        """
        self.entry(id).delete()
        self.entries = self._get_list()

    def entry(self, id: int) -> 'UserAnimeListEntry':
        """
        Returns an anime entry on the user's anime list.

        :param id: The id of the anime to get.
        :return: A UserAnimeListEntry object.
        """
        for entry in self.entries:
            if entry.anime.id == id:
                return entry

        raise AnimeNotFound(f'Anime with id {id} not found on the user\'s anime list.')

    def _get_list(self) -> List['UserAnimeListEntry']:
        """
        Gets the user's anime list from MAL.

        :return: A list of UserAnimeListEntry objects.
        """
        offset = 0
        results = []
        while True:
            r = self._request('GET', MAL_GET_ANIME_LIST_ENDPOINT(),
                              params={'limit': 1000, 'fields': 'list_status', offset: offset})
            page = json.loads(r.text)

            for entry in page['data']:
                results.append(UserAnimeListEntry(auth=self.auth, anime=entry["node"], list_status=entry['list_status']))

            if 'next' not in page['paging']:
                break
            else:
                parsed_url = urlparse(page['paging']['next'])
                next_url = parse_qs(parsed_url.query)
                offset = int(next_url['offset'][0])

        return results
