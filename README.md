# pyMALv2
Python API wrapper for [MyAnimeList](https://myanimelist.net/), supporting MAL version 2 api.
> **Note: This is a work in progress and many endpoints have not been implemented. Expect a lot of bugs.**

## Installation
```shell
pip install pyMALv2
```
or
```shell
python setup.py install
```
## Usage
Basic Usage:
```python

from pyMALv2.auth import Authorization, OAuth
from pyMALv2.services import UserService

# Create an oauth client.
client = OAuth(
    client_id='your_client_id',
    client_secret='your_client_secret',
    redirect_uri='https://your-redirect-url.com'
)

# Start the oauth flow, starts a http server to receive authorization code.
client.start_oauth2_flow(http_server=True, port=8989)

# Create an authorization object.
auth = Authorization().load_token(
    access_token=client.tokens.access_token,
    refresh_token=client.tokens.refresh_token,
    expires_in=client.tokens.expires_in,
)

# Create service
user = UserService(auth)

# Get anime list
anime_list = user.anime_list.get()
# This returns a paginated list of the user's anime list.

```

Add/Update/Delete entry to user's anime or manga list:
```python
user = UserService(auth)
user.anime_list.entry('43608').update(...)
user.manga_list.entry('43608').delete()
```

See `examples/example1.py` for an example on storing the tokens in a file so that you don't have to keep re-authorizing everytime your script runs. If you've ever worked with the google python api, it looks very similar.

**Data returned from some functions are json objects deserialised to python objects analogous to the MALv2 API. So please refer to the MAL API for more information.**

For more information, inspect the source code or [MAL api docs](https://myanimelist.net/apiconfig/references/api/v2). Wrapper API docs are not yet available.

## Currently Implemented Endpoints
* Manga List Add/Update
  * https://myanimelist.net/apiconfig/references/api/v2#operation/manga_manga_id_my_list_status_put
* Manga List Delete
  * https://myanimelist.net/apiconfig/references/api/v2#operation/manga_manga_id_my_list_status_delete
* Get User Manga List
  * https://myanimelist.net/apiconfig/references/api/v2#operation/manga_manga_id_my_list_status_put
* Anime List Add/Update
  * https://myanimelist.net/apiconfig/references/api/v2#operation/anime_anime_id_my_list_status_put
* Anime List Delete
  * https://myanimelist.net/apiconfig/references/api/v2#operation/anime_anime_id_my_list_status_delete
* Get User Anime List
  * https://myanimelist.net/apiconfig/references/api/v2#operation/users_user_id_animelist_get
* OAuth2 Authentication
  * https://myanimelist.net/apiconfig/references/api/v2#section/Authentication

## Contributing
Contributions are welcome. Please fork the repo and submit a pull request.

## License
MIT License