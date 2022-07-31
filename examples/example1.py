import os

from pyMALv2.auth import Authorization, OAuth
from pyMALv2.enums import AnimeListEntryStatuses, MangaListEntryStatuses
from pyMALv2.models.anime import Anime
from pyMALv2.services import UserService, MangaService
from pyMALv2.services.anime_service.anime_service import AnimeService

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

user = UserService(auth)
anime = AnimeService(auth)
manga = MangaService(auth)

search_anime = anime.search('One Piece', limit=100, get_all=True)
print(search_anime)
search_manga = manga.search('Demon Slayer', limit=100, get_all=True)
print(search_manga)

get_anime = anime.get(44524, fields='id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics')
print(get_anime)

get_manga = manga.get(2, fields='id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_volumes,num_chapters,authors{first_name,last_name},pictures,background,related_anime,related_manga,recommendations,serialization{name}')
print(get_manga)
anime_list = user.anime_list.get()
print(anime_list)
manga_list = user.manga_list.get()
print(manga_list)

# add an entry to the anime list
user.anime_list.update(Anime(id=21), status='completed', num_watched_episodes=10)

# add an entry to the manga list
user.manga_list.delete(13)
