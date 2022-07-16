MAL_TOKEN_ENDPOINT = "https://myanimelist.net/v1/oauth2/token"
MAL_OAUTH_ENDPOINT = "https://myanimelist.net/v1/oauth2/authorize"


def MAL_GET_USER_INFO_ENDPOINT(username: str = '@me') -> str:
    return f"https://api.myanimelist.net/v2/users/{username}"


def MAL_GET_ANIME_LIST_ENDPOINT(username: str = '@me') -> str:
    return f"https://api.myanimelist.net/v2/users/{username}/animelist"


def MAL_GET_MANGA_LIST_ENDPOINT(username: str = '@me') -> str:
    return f"https://api.myanimelist.net/v2/users/{username}/mangalist"


def MAL_MANGA_LIST_ENTRY_ENDPOINT(manga_id: int) -> str:
    return f"https://api.myanimelist.net/v2/manga/{manga_id}/my_list_status"

def MAL_ANIME_LIST_ENTRY_ENDPOINT(anime_id: int) -> str:
    return f"https://api.myanimelist.net/v2/anime/{anime_id}/my_list_status"
