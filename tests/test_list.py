import os

import pytest

from auth import auth
from pyMALv2.models.anime import Anime
from pyMALv2.models.manga import Manga

from pyMALv2.services import UserService

user = UserService(auth)


def test_get_user_anime_list():
    """
    TEST: Get the user's anime list.

    :return:
    """
    anime_list = user.anime_list.get()

    assert anime_list[0].anime is not None and anime_list[0].list_status is not None


def test_get_user_manga_list():
    """
    TEST: Get the user's manga list.

    :return:
    """
    manga_list = user.manga_list.get()

    assert manga_list[0].manga is not None and manga_list[0].list_status is not None


def test_add_to_anime_list():
    """
    TEST: Add an anime to the user's anime list.

    :return:
    """
    user.anime_list.update(Anime(id=21),
                           status='on_hold',
                           num_watched_episodes=1,
                           score=10,
                           num_times_rewatched=1,
                           rewatch_value=5,
                           priority=1,
                           tags='test, test2',
                           comments='Test comment')

    assert user.anime_list.entry(21).list_status.status == 'on_hold'


@pytest.mark.depends(on=['test_add_to_anime_list'])
def test_update_anime_entry():
    """
    TEST: Update an anime entry on the user's anime list.

    :return:
    """
    user.anime_list.update(Anime(id=21), status='completed', num_watched_episodes=10)

    assert user.anime_list.entry(21).list_status.status == 'completed' and user.anime_list.entry(
        21).list_status.num_episodes_watched == 10


@pytest.mark.depends(on=['test_add_to_anime_list', 'test_update_anime_entry'])
def test_delete_anime_record():
    """
    TEST: Delete an anime record from the user's anime list.

    :return:
    """
    user.anime_list.delete(21)

    for entry in user.anime_list.get():
        if entry.anime.id == 21:
            assert False
    assert True


def test_add_to_manga_list():
    """
    TEST: Add a manga to the user's manga list.

    :return:
    """
    user.manga_list.update(Manga(id=13),
                           status='on_hold',
                           num_chapters_read=1,
                           score=10,
                           num_times_reread=1,
                           reread_value=5,
                           tags='test, test2',
                           comments='Test comment')

    assert user.manga_list.entry(13).list_status.status == 'on_hold'


@pytest.mark.depends(on=['test_add_to_manga_list'])
def test_update_manga_entry():
    """
    TEST: Update a manga entry on the user's manga list.

    :return:
    """
    user.manga_list.update(Manga(id=13), status='completed', num_chapters_read=10)

    assert user.manga_list.entry(13).list_status.status == 'completed' and user.manga_list.entry(
        13).list_status.num_chapters_read == 10


@pytest.mark.depends(on=['test_add_to_manga_list', 'test_update_manga_entry'])
def test_delete_manga_entry():
    """
    TEST: Delete a manga entry from the user's manga list.

    :return:
    """
    user.manga_list.delete(13)

    for entry in user.manga_list.get():
        if entry.manga.id == 13:
            assert False
    assert True
