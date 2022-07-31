import json
from typing import List
from urllib.parse import urlparse, parse_qs

from pyMALv2.exceptions.MangaNotFound import MangaNotFound
from pyMALv2.models.manga import Manga
from pyMALv2.services.base import Base
from pyMALv2.auth import Authorization
from pyMALv2.constants.mal_endpoints import *

class MangaService(Base):
    def __init__(self, auth: Authorization):
        super().__init__(auth)

    def search(self, q: str, fields: str = None, limit: int = 100, offset: int = 0, get_all: bool = False) -> List[Manga]:
        """
        Searches for manga on MyAnimeList.

        :param get_all: Gets all the results.
        :param q: Search query
        :param fields: The fields to return
        :param limit: The limit of results to return.
        :param offset: The offset of the first result to return.
        :return: Object with the anime list.
        """
        results = []
        while True:
            r = self._request_no_auth('GET', MAL_SEARCH_MANGA_ENDPOINT,
                                      params={'q': q, 'fields': fields, 'limit': limit, 'offset': offset})
            page = json.loads(r.text)

            for manga in page['data']:
                results.append(Manga.from_dict(manga['node']))

            if not get_all:
                break

            if 'next' not in page['paging']:
                break
            else:
                parsed_url = urlparse(page['paging']['next'])
                next_url = parse_qs(parsed_url.query)
                offset = int(next_url['offset'][0])

        return results

    def get(self, manga_id: int, fields: str = None):
        """
        Get an manga by id.

        :param manga_id: The manga id.
        :param fields: The fields to return.
        :return: Object with the anime info.
        """
        r = self._request_no_auth('GET', MAL_GET_MANGA_INFO_ENDPOINT(manga_id), params={'fields': fields})

        if r.status_code == 404:
            raise MangaNotFound('Manga with id {} not found'.format(manga_id))
        elif r.status_code != 200:
            raise Exception('MyAnimeList returned HTTP {} with message {}'.format(r.status_code, r.json['error']))

        return Manga.from_dict(json.loads(r.text))

