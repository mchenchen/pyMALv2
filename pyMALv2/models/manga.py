# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = manga_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional

from .author import Author
from .manga_my_list_status import MangaMyListStatus
from .manga_recommendation import MangaRecommendation
from .related_manga import RelatedManga
from .serialization import Serialization
from .utils import *
from .alternative_titles import AlternativeTitles
from .genre import Genre
from .picture import Picture


@dataclass
class Manga:
    id: Optional[int] = None
    title: Optional[str] = None
    main_picture: Optional[Picture] = None
    alternative_titles: Optional[AlternativeTitles] = None
    start_date: Optional[datetime] = None
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
    my_list_status: Optional[MangaMyListStatus] = None
    num_volumes: Optional[int] = None
    num_chapters: Optional[int] = None
    authors: Optional[List[Author]] = None
    pictures: Optional[List[Picture]] = None
    background: Optional[str] = None
    related_anime: Optional[List[Any]] = None
    related_manga: Optional[List[RelatedManga]] = None
    recommendations: Optional[List[MangaRecommendation]] = None
    serialization: Optional[List[Serialization]] = None
