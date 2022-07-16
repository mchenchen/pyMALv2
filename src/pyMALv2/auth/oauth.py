import json
import secrets
import urllib.parse

from http.server import HTTPServer, BaseHTTPRequestHandler

import requests

from ..exceptions import InvalidAuthorizationCodeError, AuthorizationFailed
from ..constants.mal_endpoints import *


def _get_new_code_verifier() -> str:
    token = secrets.token_urlsafe(100)
    return token[:128]


class RequestHandler(BaseHTTPRequestHandler):

    def __init__(self):
        self.auth_code = None

    def __call__(self, *args, **kwargs):
        """Handle a request."""
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.auth_code = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)['code'][0]


class OAuth():
    tokens = None

    def __init__(self, client_id: str = None, client_secret: str = None, redirect_uri: str = None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def start_oauth2_flow(self, http_server: bool = False, port: int = 8989):
        """
        Start the OAuth2 flow.

        :param http_server: If True, start a local HTTP server to receive the authorization code.
        :param port: The port to use for the HTTP server.
        :return:
        """
        code_verifier = _get_new_code_verifier()
        if http_server:
            authorization_code = self._receive_oauth_token(code_verifier, port)
        else:
            authorization_code = self._input_oauth_token(code_verifier)

        self.tokens = self._get_user_tokens(authorization_code, code_verifier)

    def _input_oauth_token(self, code_verifier: str):
        """
        Get the authorization code from the user.

        :param code_verifier: The code verifier.
        :return: The authorization code.
        """
        print('Please open the following URL in your browser:' + self._get_oauth2_url(code_verifier))
        return input('Please visit the URL and paste the authorization code here:')

    def _receive_oauth_token(self, code_verifier: str, port: int = 8989):
        """
        Use a local HTTP server to receive the authorization code.

        :param code_verifier: The code verifier.
        :param port: The HTTP server port.
        :return: The authorization code.
        """
        request_handler = RequestHandler()
        httpd = HTTPServer(('localhost', port), request_handler)
        print("Please open the following URL in your browser:" + self._get_oauth2_url(code_verifier))
        print("Waiting for code...")
        httpd.handle_request()
        return request_handler.auth_code

    def tokens_as_json(self):
        """
        Get the tokens as a JSON string.

        :return: The tokens as a JSON string.
        """
        return json.dumps(self.tokens)

    def _get_user_tokens(self, authorization_code: str, code_verifier: str):
        """
        Use the authorization code to get the user tokens.

        :param authorization_code: The authorization code.
        :param code_verifier: The code verifier.
        :return: The user tokens as json dict.
        """
        body = {
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'code_verifier': code_verifier,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }

        if self.redirect_uri is not None:
            body['redirect_uri'] = self.redirect_uri

        r = requests.post(MAL_TOKEN_ENDPOINT, data=body)
        if r.status_code == 200:
            return r.json()
        elif r.status_code == 401 or r.status_code == 403:
            raise InvalidAuthorizationCodeError(r.text)
        else:
            raise AuthorizationFailed(r.text)

    def _get_oauth2_url(self, code_challenge: str):
        params = {
            'response_type': 'code',
            'client_id': self.client_id,
            'code_challenge': code_challenge,
        }

        if self.redirect_uri is not None:
            params['redirect_uri'] = self.redirect_uri

        return MAL_OAUTH_ENDPOINT + '?' + urllib.parse.urlencode(params)

    def from_json_file(self, file_path: str):
        with open(file_path, 'r') as f:
            self.tokens = json.load(f)

