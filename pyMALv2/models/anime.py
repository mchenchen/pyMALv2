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

    @staticmethod
    def from_dict(obj: Any) -> 'Anime':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        main_picture = from_union([Picture.from_dict, from_none], obj.get("main_picture"))
        alternative_titles = from_union([AlternativeTitles.from_dict, from_none], obj.get("alternative_titles"))
        start_date = from_union([from_datetime, from_none], obj.get("start_date"))
        end_date = from_union([from_datetime, from_none], obj.get("end_date"))
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
        my_list_status = from_union([AnimeMyListStatus.from_dict, from_none], obj.get("my_list_status"))
        num_episodes = from_union([from_int, from_none], obj.get("num_episodes"))
        start_season = from_union([StartSeason.from_dict, from_none], obj.get("start_season"))
        broadcast = from_union([Broadcast.from_dict, from_none], obj.get("broadcast"))
        source = from_union([from_str, from_none], obj.get("source"))
        average_episode_duration = from_union([from_int, from_none], obj.get("average_episode_duration"))
        rating = from_union([from_str, from_none], obj.get("rating"))
        pictures = from_union([lambda x: from_list(Picture.from_dict, x), from_none], obj.get("pictures"))
        background = from_union([from_str, from_none], obj.get("background"))
        related_anime = from_union([lambda x: from_list(RelatedAnime.from_dict, x), from_none], obj.get("related_anime"))
        related_manga = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("related_manga"))
        recommendations = from_union([lambda x: from_list(AnimeRecommendation.from_dict, x), from_none], obj.get("recommendations"))
        studios = from_union([lambda x: from_list(Genre.from_dict, x), from_none], obj.get("studios"))
        statistics = from_union([Statistics.from_dict, from_none], obj.get("statistics"))
        return Anime(id, title, main_picture, alternative_titles, start_date, end_date, synopsis, mean, rank, popularity, num_list_users, num_scoring_users, nsfw, created_at, updated_at, media_type, status, genres, my_list_status, num_episodes, start_season, broadcast, source, average_episode_duration, rating, pictures, background, related_anime, related_manga, recommendations, studios, statistics)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_int, from_none], self.id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["main_picture"] = from_union([lambda x: to_class(Picture, x), from_none], self.main_picture)
        result["alternative_titles"] = from_union([lambda x: to_class(AlternativeTitles, x), from_none], self.alternative_titles)
        result["start_date"] = from_union([lambda x: x.isoformat(), from_none], self.start_date)
        result["end_date"] = from_union([lambda x: x.isoformat(), from_none], self.end_date)
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
        result["my_list_status"] = from_union([lambda x: to_class(AnimeMyListStatus, x), from_none], self.my_list_status)
        result["num_episodes"] = from_union([from_int, from_none], self.num_episodes)
        result["start_season"] = from_union([lambda x: to_class(StartSeason, x), from_none], self.start_season)
        result["broadcast"] = from_union([lambda x: to_class(Broadcast, x), from_none], self.broadcast)
        result["source"] = from_union([from_str, from_none], self.source)
        result["average_episode_duration"] = from_union([from_int, from_none], self.average_episode_duration)
        result["rating"] = from_union([from_str, from_none], self.rating)
        result["pictures"] = from_union([lambda x: from_list(lambda x: to_class(Picture, x), x), from_none], self.pictures)
        result["background"] = from_union([from_str, from_none], self.background)
        result["related_anime"] = from_union([lambda x: from_list(lambda x: to_class(RelatedAnime, x), x), from_none], self.related_anime)
        result["related_manga"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.related_manga)
        result["recommendations"] = from_union([lambda x: from_list(lambda x: to_class(AnimeRecommendation, x), x),
                                                from_none], self.recommendations)
        result["studios"] = from_union([lambda x: from_list(lambda x: to_class(Genre, x), x), from_none], self.studios)
        result["statistics"] = from_union([lambda x: to_class(Statistics, x), from_none], self.statistics)
        return result


def anime_from_dict(s: Any) -> Anime:
    return Anime.from_dict(s)


def anime_to_dict(x: Anime) -> Any:
    return to_class(Anime, x)
