from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.utils import from_none, from_union, from_int, to_class
from pyMALv2.models.status import Status


@dataclass
class Statistics:
    status: Optional[Status] = None
    num_list_users: Optional[int] = None