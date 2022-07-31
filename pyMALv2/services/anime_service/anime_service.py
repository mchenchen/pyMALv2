import json
from urllib.parse import urlparse, parse_qs
from typing import List

from ..base import Base
from ...auth import Authorization
from ...constants.mal_endpoints import *
from ...exceptions.AnimeNotFound import AnimeNotFound
from ...models.anime import Anime

class AnimeService(Base):
    def __init__(self, auth: Authorization):
        super().__init__(auth)

    def search(self, q: str, fields: str = None, limit: int = 100, offset: int = 0, get_all: bool = False) -> List[Anime]:
        """
        Searches for anime on MyAnimeList.

        :param get_all: Gets all the results.
        :param q: Search query
        :param fields: The fields to return
        :param limit: The limit of results to return.
        :param offset: The offset of the first result to return.
        :return: Object with the anime list.
        """
        results = []
        while True:
            r = self._request_no_auth('GET', MAL_SEARCH_ANIME_ENDPOINT, params={'q': q, 'fields': fields, 'limit': limit, 'offset': offset})
            page = json.loads(r.text)

            for anime in page['data']:
                results.append(Anime.from_dict(anime['node']))

            if not get_all:
                break

            if 'next' not in page['paging']:
                break
            else:
                parsed_url = urlparse(page['paging']['next'])
                next_url = parse_qs(parsed_url.query)
                offset = int(next_url['offset'][0])

        return results

    def get(self, anime_id: int, fields: str = None):
        """
        Get an anime by id.

        :param anime_id: The anime id.
        :param fields: The fields to return.
        :return: Object with the anime info.
        """
        r = self._request_no_auth('GET', MAL_GET_ANIME_INFO_ENDPOINT(anime_id), params={'fields': fields})

        if r.status_code == 404:
            raise AnimeNotFound('Anime with id {} not found'.format(anime_id))
        elif r.status_code != 200:
            raise Exception('MyAnimeList returned HTTP {} with message {}'.format(r.status_code, r.json['error']))

        return Anime.from_dict(json.loads(r.text))
