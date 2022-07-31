import os

from pyMALv2.auth import Authorization, OAuth

auth = Authorization()

if os.path.exists('token.json'):
    auth.load_token_from_json('token.json')

oauth_client = OAuth()
oauth_client.from_json_file('credentials.json')

if not auth or not auth.is_valid():
    if auth and auth.is_expired() and auth.refresh_token:
        auth.refresh()
    else:
        oauth_client.start_oauth2_flow(http_server=True, port=8989)
        with open('token.json', 'w') as f:
            f.write(oauth_client.tokens_as_json())
            f.close()
        auth.load_token_from_json('token.json')
