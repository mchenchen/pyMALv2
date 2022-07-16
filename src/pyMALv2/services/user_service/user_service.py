import json

from src.pyMALv2.auth import Authorization
from src.pyMALv2.services.base import Base
from src.pyMALv2.constants.mal_endpoints import *
from .user_anime_list import UserAnimeList
from .user_manga_list import UserMangaList
from types import SimpleNamespace


class UserService(Base):
    def __init__(self, auth: Authorization):
        super().__init__(auth)

    def get_current_user_info(self, fields: list = None):
        """
        Get the user's info.

        :param fields: The fields to return.
        :return: Object with the user's info.
        """
        r = self._request('GET', MAL_GET_USER_INFO_ENDPOINT(), params={'fields': ','.join(fields)})
        return json.loads(r.text, object_hook=lambda d: SimpleNamespace(**d))

    @property
    def anime_list(self):
        return UserAnimeList(self.auth)

    @property
    def manga_list(self):
        return UserMangaList(self.auth)

