import json
import requests

from ..exceptions import AuthorizationFailed
from ..constants.mal_endpoints import *

class Authorization():
    access_token = None
    refresh_token = None
    expires_in = None
    client_id = None
    client_secret = None

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
            self.client_id = data['client_id']
            self.client_secret = data['client_secret']

    def load_token(self, access_token, refresh_token, expires_in, client_id, client_secret):
        """
        Load token from parameters.

        :param client_secret: The client secret.
        :param client_id: The client id.
        :param access_token: The access token.
        :param refresh_token: The refresh token.
        :param expires_in: The token expiration time (seconds).
        :return:
        """
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_in = expires_in
        self.client_id = client_id
        self.client_secret = client_secret

    def check_tokens(self) -> bool:
        if self.access_token is None or self.refresh_token is None or self.expires_in is None:
            return False
        else:
            return True

    def is_valid(self) -> bool:
        """
        Check if the token is valid.

        :return: True if the token is valid, False otherwise.
        """

        if not self.check_tokens():
            return False

        r = requests.get(MAL_GET_USER_INFO_ENDPOINT(),
                         headers={'Authorization': 'Bearer ' + self.access_token})
        if r.status_code == 200:
            return True
        else:
            return False

    def is_expired(self) -> bool:
        """
        Check if the access token is expired.

        :return: True if the access token is expired, False otherwise
        """

        if not self.check_tokens():
            return False

        return self.expires_in < 60


    def refresh(self):
        """
        Refresh the access token using the refresh token.

        :return: None
        :raises: AuthorizationFailed if the refresh token is invalid
        """

        if not self.check_tokens():
            return False

        r = requests.post(MAL_TOKEN_ENDPOINT,
                          data={'grant_type': 'refresh_token', 'refresh_token': self.refresh_token})
        if r.status_code == 200:
            data = r.json()
            self.access_token = data['access_token']
            self.refresh_token = data['refresh_token']
        else:
            raise AuthorizationFailed('Failed to obtain new access token')
