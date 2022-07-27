import json
import requests

from ..exceptions import AuthorizationFailed
from ..constants.mal_endpoints import *

def check_token(func):
    def wrapper(self, *args, **kwargs):
        if self.access_token is None or self.refresh_token is None or self.expires_in is None:
            raise Exception('No access token or refresh token or expires in')
        return func(self, *args, **kwargs)

    return wrapper


class Authorization():
    access_token = None
    refresh_token = None
    expires_in = None

    def load_token_from_json(self, json_file):
        """
        Load token from json file.

        :param json_file: The json file containing the token.
        :return: None
        """
        with open(json_file) as f:
            data = json.load(f)
            self.access_token = data['access_token']
            self.refresh_token = data['refresh_token']
            self.expires_in = data['expires_in']

    def load_token(self, access_token, refresh_token, expires_in):
        """
        Load token from parameters.

        :param access_token: The access token.
        :param refresh_token: The refresh token.
        :param expires_in: The token expiration time (seconds).
        :return:
        """
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_in = expires_in

    @check_token
    def is_valid(self) -> bool:
        """
        Check if the token is valid.

        :return: True if the token is valid, False otherwise.
        """
        r = requests.get(MAL_GET_USER_INFO_ENDPOINT(),
                         headers={'Authorization': 'Bearer ' + self.access_token})
        if r.status_code == 200:
            return True
        else:
            return False

    @check_token
    def is_expired(self) -> bool:
        """
        Check if the access token is expired.

        :return: True if the access token is expired, False otherwise
        """
        return self.expires_in < 60

    @check_token
    def refresh(self):
        """
        Refresh the access token using the refresh token.

        :return: None
        :raises: AuthorizationFailed if the refresh token is invalid
        """
        r = requests.post(MAL_TOKEN_ENDPOINT,
                          data={'grant_type': 'refresh_token', 'refresh_token': self.refresh_token})
        if r.status_code == 200:
            data = r.json()
            self.access_token = data['access_token']
            self.refresh_token = data['refresh_token']
        else:
            raise AuthorizationFailed('Failed to obtain new access token')
