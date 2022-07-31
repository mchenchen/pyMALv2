class AnimeNotFound(Exception):
    message = 'MyAnimeList returned a HTTP 404 error. Please check the anime ID.'
