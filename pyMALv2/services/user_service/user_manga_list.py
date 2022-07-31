import json

from ..base import Base
from ...auth import Authorization
from typing import List, TYPE_CHECKING
from urllib.parse import urlparse, parse_qs

from ...constants.mal_endpoints import MAL_GET_ANIME_LIST_ENDPOINT, MAL_MANGA_LIST_ENTRY_ENDPOINT, \
    MAL_GET_MANGA_LIST_ENDPOINT
from ...models.user_manga_list_entry import UserMangaListEntry
from ...models.manga import Manga
from ...models.manga_my_list_status import MangaMyListStatus


class UserMangaList(Base):
    def __init__(self, auth: Authorization):
        super().__init__(auth)
        self.entries = self._get_list()

    def entry(self, id: int):
        """
        Returns the manga entry with the given id.

        :param id: The manga id.
        :return: A UserMangaListEntry object.
        """
        for entry in self.entries:
            if entry.manga.id == id:
                return entry

    def update(self, manga: 'Manga', status: str = None, is_reading: bool = None, score: int = None,
            num_volumes_read: int = None, num_chapters_read: int = None, priority: int = None,
            num_times_reread: int = None, reread_value: int = None, tags: str = None, comments: str = None):
        """
        Adds or updates a manga entry on the user's manga list.

        :param manga: A manga object with at least an id.
        :param status: The read status of the manga.
        :param is_reading: Is currently reading the manga.
        :param score: The user's score for the manga.
        :param num_volumes_read: The number of volumes read.
        :param num_chapters_read:  The number of chapters read.
        :param priority: The priority of the manga.
        :param num_times_reread: The number of times the user has reread the manga.
        :param reread_value: The reread value of the manga.
        :param tags: Tags for this record.
        :param comments: Comments for this record.
        :return:
        """
        self._request('PATCH', MAL_MANGA_LIST_ENTRY_ENDPOINT(manga.id), data={
            'status': status,
            'is_reading': is_reading,
            'score': score,
            'num_volumes_read': num_volumes_read,
            'num_chapters_read': num_chapters_read,
            'priority': priority,
            'num_times_reread': num_times_reread,
            'reread_value': reread_value,
            'tags': tags,
            'comments': comments,
        })
        self.entries = self._get_list()

    def get(self):
        """
        Returns the user's manga list.

        :return: A list of UserMangaListEntry objects.
        """
        return self.entries

    def delete(self, id: int):
        """
        Deletes the manga entry with the given id.

        :param id: The manga id.
        :return: None
        """
        self.entry(id).delete()
        self.entries = self._get_list()

    def _get_list(self) -> List['UserMangaListEntry']:
        """
        Gets the user's manga list from MAL

        :return: A list of UserMangaListEntry objects.
        """
        offset = 0
        results = []
        while True:
            r = self._request('GET', MAL_GET_MANGA_LIST_ENDPOINT(),
                              params={'limit': 1000, 'fields': 'list_status', offset: offset})
            page = json.loads(r.text)

            for entry in page['data']:
                results.append(UserMangaListEntry.from_dict(entry, self.auth))

            if 'next' not in page['paging']:
                break
            else:
                parsed_url = urlparse(page['paging']['next'])
                next_url = parse_qs(parsed_url.query)
                offset = int(next_url['offset'][0])

        return results
