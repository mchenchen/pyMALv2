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

    @staticmethod
    def from_dict(obj: Any) -> 'Manga':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        main_picture = from_union([Picture.from_dict, from_none], obj.get("main_picture"))
        alternative_titles = from_union([AlternativeTitles.from_dict, from_none], obj.get("alternative_titles"))
        start_date = from_union([from_datetime, from_none], obj.get("start_date"))
        synopsis = from_union([from_str, from_none], obj.get("synopsis"))
        mean = from_union([from_float, from_none], obj.get("mean"))
        rank = from_union([from_int, from_none], obj.get("rank"))
        popularity = from_union([from_int, from_none], obj.get("popularity"))
        num_list_users = from_union([from_int, from_none], obj.get("num_list_users"))
        num_scoring_users = from_union([from_int, from_none], obj.get("num_scoring_users"))
        nsfw = from_union([from_str, from_none], obj.get("nsfw"))
        created_at = from_union([from_datetime, from_none], obj.get("created_at"))
        updated_at = from_union([from_datetime, from_none], obj.get("updated_at"))
        media_type = from_union([from_str, from_none], obj.get("media_type"))
        status = from_union([from_str, from_none], obj.get("status"))
        genres = from_union([lambda x: from_list(Genre.from_dict, x), from_none], obj.get("genres"))
        my_list_status = from_union([MangaMyListStatus.from_dict, from_none], obj.get("my_list_status"))
        num_volumes = from_union([from_int, from_none], obj.get("num_volumes"))
        num_chapters = from_union([from_int, from_none], obj.get("num_chapters"))
        authors = from_union([lambda x: from_list(Author.from_dict, x), from_none], obj.get("authors"))
        pictures = from_union([lambda x: from_list(Picture.from_dict, x), from_none], obj.get("pictures"))
        background = from_union([from_str, from_none], obj.get("background"))
        related_anime = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("related_anime"))
        related_manga = from_union([lambda x: from_list(RelatedManga.from_dict, x), from_none], obj.get("related_manga"))
        recommendations = from_union([lambda x: from_list(MangaRecommendation.from_dict, x), from_none], obj.get("recommendations"))
        serialization = from_union([lambda x: from_list(Serialization.from_dict, x), from_none], obj.get("serialization"))
        return Manga(id, title, main_picture, alternative_titles, start_date, synopsis, mean, rank, popularity, num_list_users, num_scoring_users, nsfw, created_at, updated_at, media_type, status, genres, my_list_status, num_volumes, num_chapters, authors, pictures, background, related_anime, related_manga, recommendations, serialization)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_int, from_none], self.id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["main_picture"] = from_union([lambda x: to_class(Picture, x), from_none], self.main_picture)
        result["alternative_titles"] = from_union([lambda x: to_class(AlternativeTitles, x), from_none], self.alternative_titles)
        result["start_date"] = from_union([lambda x: x.isoformat(), from_none], self.start_date)
        result["synopsis"] = from_union([from_str, from_none], self.synopsis)
        result["mean"] = from_union([to_float, from_none], self.mean)
        result["rank"] = from_union([from_int, from_none], self.rank)
        result["popularity"] = from_union([from_int, from_none], self.popularity)
        result["num_list_users"] = from_union([from_int, from_none], self.num_list_users)
        result["num_scoring_users"] = from_union([from_int, from_none], self.num_scoring_users)
        result["nsfw"] = from_union([from_str, from_none], self.nsfw)
        result["created_at"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        result["updated_at"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        result["media_type"] = from_union([from_str, from_none], self.media_type)
        result["status"] = from_union([from_str, from_none], self.status)
        result["genres"] = from_union([lambda x: from_list(lambda x: to_class(Genre, x), x), from_none], self.genres)
        result["my_list_status"] = from_union([lambda x: to_class(MangaMyListStatus, x), from_none], self.my_list_status)
        result["num_volumes"] = from_union([from_int, from_none], self.num_volumes)
        result["num_chapters"] = from_union([from_int, from_none], self.num_chapters)
        result["authors"] = from_union([lambda x: from_list(lambda x: to_class(Author, x), x), from_none], self.authors)
        result["pictures"] = from_union([lambda x: from_list(lambda x: to_class(Picture, x), x), from_none], self.pictures)
        result["background"] = from_union([from_str, from_none], self.background)
        result["related_anime"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.related_anime)
        result["related_manga"] = from_union([lambda x: from_list(lambda x: to_class(RelatedManga, x), x), from_none], self.related_manga)
        result["recommendations"] = from_union([lambda x: from_list(lambda x: to_class(MangaRecommendation, x), x), from_none], self.recommendations)
        result["serialization"] = from_union([lambda x: from_list(lambda x: to_class(Serialization, x), x), from_none], self.serialization)
        return result


def manga_from_dict(s: Any) -> Manga:
    return Manga.from_dict(s)


def manga_to_dict(x: Manga) -> Any:
    return to_class(Manga, x)
