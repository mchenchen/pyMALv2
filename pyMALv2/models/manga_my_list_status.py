from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any

from pyMALv2.models.utils import from_union, from_str, from_none, from_bool, from_int, from_datetime


@dataclass
class MangaMyListStatus:
    status: Optional[str] = None
    is_rereading: Optional[bool] = None
    num_volumes_read: Optional[int] = None
    num_chapters_read: Optional[int] = None
    score: Optional[int] = None
    updated_at: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MangaMyListStatus':
        assert isinstance(obj, dict)
        status = from_union([from_str, from_none], obj.get("status"))
        is_rereading = from_union([from_bool, from_none], obj.get("is_rereading"))
        num_volumes_read = from_union([from_int, from_none], obj.get("num_volumes_read"))
        num_chapters_read = from_union([from_int, from_none], obj.get("num_chapters_read"))
        score = from_union([from_int, from_none], obj.get("score"))
        updated_at = from_union([from_datetime, from_none], obj.get("updated_at"))
        return MangaMyListStatus(status, is_rereading, num_volumes_read, num_chapters_read, score, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["status"] = from_union([from_str, from_none], self.status)
        result["is_rereading"] = from_union([from_bool, from_none], self.is_rereading)
        result["num_volumes_read"] = from_union([from_int, from_none], self.num_volumes_read)
        result["num_chapters_read"] = from_union([from_int, from_none], self.num_chapters_read)
        result["score"] = from_union([from_int, from_none], self.score)
        result["updated_at"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        return result
