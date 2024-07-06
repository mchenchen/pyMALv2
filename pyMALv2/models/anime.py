from dataclasses import dataclass
from typing import Optional, List, Any
from datetime import datetime

from .alternative_titles import AlternativeTitles
from .broadcast import Broadcast
from .genre import Genre
from .anime_my_list_status import AnimeMyListStatus
from .picture import Picture
from .anime_recommendation import AnimeRecommendation
from .related_anime import RelatedAnime
from .start_season import StartSeason
from .statistics import Statistics
from .utils import from_list, from_str, from_none, from_union, from_int, from_datetime, to_class, \
    from_float, to_float


@dataclass
class Anime:
    id: Optional[int] = None
    title: Optional[str] = None
    main_picture: Optional[Picture] = None
    alternative_titles: Optional[AlternativeTitles] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    synopsis: Optional[str] = None
    mean: Optional[float] = None
    rank: Optional[int] = None
    popularity: Optional[int] = None
    num_list_users: Optional[int] = None
    num_scoring_users: Optional[int] = None
    nsfw: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    media_type: Optional[str] = None
    status: Optional[str] = None
    genres: Optional[List[Genre]] = None
    my_list_status: Optional[AnimeMyListStatus] = None
    num_episodes: Optional[int] = None
    start_season: Optional[StartSeason] = None
    broadcast: Optional[Broadcast] = None
    source: Optional[str] = None
    average_episode_duration: Optional[int] = None
    rating: Optional[str] = None
    pictures: Optional[List[Picture]] = None
    background: Optional[str] = None
    related_anime: Optional[List[RelatedAnime]] = None
    related_manga: Optional[List[Any]] = None
    recommendations: Optional[List[AnimeRecommendation]] = None
    studios: Optional[List[Genre]] = None
    statistics: Optional[Statistics] = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'main_picture':
                value = Picture(**value)
            setattr(self, key, value)