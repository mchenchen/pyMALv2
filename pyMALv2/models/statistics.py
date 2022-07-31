from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.utils import from_none, from_union, from_int, to_class
from pyMALv2.models.status import Status


@dataclass
class Statistics:
    status: Optional[Status] = None
    num_list_users: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Statistics':
        assert isinstance(obj, dict)
        status = from_union([Status.from_dict, from_none], obj.get("status"))
        num_list_users = from_union([from_int, from_none], obj.get("num_list_users"))
        return Statistics(status, num_list_users)

    def to_dict(self) -> dict:
        result: dict = {}
        result["status"] = from_union([lambda x: to_class(Status, x), from_none], self.status)
        result["num_list_users"] = from_union([from_int, from_none], self.num_list_users)
        return result
