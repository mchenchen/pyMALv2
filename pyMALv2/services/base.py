from ..auth import Authorization
import requests

class Base():
    def __init__(self, auth: Authorization):
        self.auth = auth

    def _request(self, method: str, endpoint: str, params: dict = None, data: dict = None):
        """
        Make a request to the API.
        """
        if not self.auth.is_valid():
            self.auth.refresh()
        headers = {
            'Authorization': 'Bearer {}'.format(self.auth.access_token),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request(method, endpoint, headers=headers, params=params, data=data)
        if response.status_code == 401:
            self.auth.refresh()
            headers = {
                'Authorization': 'Bearer {}'.format(self.auth.access_token),
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            response = requests.request(method, endpoint, headers=headers, params=params, data=data)
        return response

    def _request_no_auth(self, method: str, endpoint: str, params: dict = None, data: dict = None):
        headers = {
            'X-MAL-CLIENT-ID': '{}'.format(self.auth.client_id),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        return requests.request(method, endpoint, headers=headers, params=params, data=data)



