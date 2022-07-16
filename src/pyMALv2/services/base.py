from src.pyMALv2.auth import Authorization
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

