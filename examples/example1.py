import os

from src.pyMALv2.auth import Authorization, OAuth
from src.pyMALv2.enums import MangaListEntryStatuses, AnimeListEntryStatuses
from src.pyMALv2.services import UserService

auth = None

if os.path.exists('token.json'):
    auth = Authorization()
    auth.load_token_from_json('token.json')

oauth_client = OAuth().from_json_file('credentials.json')

if not auth or not auth.is_valid():
    if auth and auth.is_expired() and auth.refresh_token:
        auth.refresh()
    else:
        oauth_client.start_oauth2_flow(http_server=True, port=8989)
        with open('token.json', 'w') as f:
            f.write(oauth_client.tokens_as_json())

user = UserService(auth)

anime_list = user.anime_list.get()
manga_list = user.manga_list.get()

# add an entry to the anime list
user.anime_list.entry('48895').update(status=AnimeListEntryStatuses.COMPLETED)

# add an entry to the manga list
user.manga_list.entry('1706').delete()

print(user)
