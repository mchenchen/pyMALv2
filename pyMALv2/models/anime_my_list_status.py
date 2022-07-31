from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any

from pyMALv2.models.utils import from_str, from_none, from_union, from_int, from_bool, from_datetime


@dataclass
class AnimeMyListStatus:
    status: Optional[str] = None
    score: Optional[int] = None
    num_episodes_watched: Optional[int] = None
    is_rewatching: Optional[bool] = None
    updated_at: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AnimeMyListStatus':
        assert isinstance(obj, dict)
        status = from_union([from_str, from_none], obj.get("status"))
        score = from_union([from_int, from_none], obj.get("score"))
        num_episodes_watched = from_union([from_int, from_none], obj.get("num_episodes_watched"))
        is_rewatching = from_union([from_bool, from_none], obj.get("is_rewatching"))
        updated_at = from_union([from_datetime, from_none], obj.get("updated_at"))
        return AnimeMyListStatus(status, score, num_episodes_watched, is_rewatching, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["status"] = from_union([from_str, from_none], self.status)
        result["score"] = from_union([from_int, from_none], self.score)
        result["num_episodes_watched"] = from_union([from_int, from_none], self.num_episodes_watched)
        result["is_rewatching"] = from_union([from_bool, from_none], self.is_rewatching)
        result["updated_at"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        return result
