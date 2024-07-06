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

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
