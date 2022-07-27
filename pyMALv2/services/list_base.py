import json
from types import SimpleNamespace

from .base import Base
from ..auth import Authorization
from ..constants.mal_endpoints import *


class ListBase(Base):
    def __init__(self, auth: Authorization):
        super().__init__(auth)

    def _get_list(self, manga: bool = False, username: str = '@me', status: str = None, sort: str = None,
                  limit: int = 100, offset: int = 0,
                  next_url: str = None):
        """
        Get the user's anime or manga list. Defaults to the user's anime list.

        :param manga: If True, get the user's manga list.
        :param username: The username of the user.
        :param status: The statuses to return.
        :param sort: The sort order.
        :param limit: The maximum number of items to return.
        :param offset: The offset of the first item to return.
        :param next_url: The next paging url.
        :return:
        """
        if next_url:
            r = self._request('GET', next_url)
        else:
            if manga:
                url = MAL_GET_MANGA_LIST_ENDPOINT(username)
            else:
                url = MAL_GET_ANIME_LIST_ENDPOINT(username)

            r = self._request('GET', url,
                              params={'status': status, 'sort': sort, 'limit': limit, 'offset': offset,
                                      'next': next_url})

        return json.loads(r.text, object_hook=lambda d: SimpleNamespace(**d))

    def _delete_list_entry(self, manga: bool = False, anime_id: int = None, manga_id: int = None):
        """
        Delete an anime or manga entry from the user's list.

        :param manga: If True, delete the manga entry.
        :param anime_id: The anime id.
        :param manga_id: The manga id.
        :return:
        """
        if not manga and not anime_id:
            raise ValueError('Anime id is required.')
        if manga and not manga_id:
            raise ValueError('Manga id is required.')

        if manga:
            url = MAL_MANGA_LIST_ENTRY_ENDPOINT(manga_id)
        else:
            url = MAL_ANIME_LIST_ENTRY_ENDPOINT(anime_id)

        r = self._request('DELETE', url)

        if not r.status_code == 200:
            raise Exception(f'Error deleting anime or manga entry: {r.text}')

    def _get_list_entry(self, manga: bool = False, anime_id: int = None, manga_id: int = None):
        raise NotImplementedError()
