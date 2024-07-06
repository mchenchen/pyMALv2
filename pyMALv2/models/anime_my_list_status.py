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

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)