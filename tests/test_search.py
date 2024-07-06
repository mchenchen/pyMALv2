import pytest

from auth import auth
from pyMALv2.services.anime_service.anime_service import AnimeService
from pyMALv2.services.manga_service.manga_service import MangaService
from pprint import pprint

anime = AnimeService(auth)
manga = MangaService(auth)


def test_search_anime():
    results = anime.search(
        q='naruto',
        limit=10
    )

    pprint(results)

    # check if result with id 1735 is in the results
    assert any(result.id == 1735 for result in results)

def test_search_manga():
    results = manga.search(
        q='horimiya',
        limit=10
    )

    pprint(results)

    # check if result with id 42451 is in the results
    assert any(result.id == 42451 for result in results)