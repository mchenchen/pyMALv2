from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.utils import from_str, from_none, from_union, is_type


@dataclass
class Status:
    watching: Optional[int] = None
    completed: Optional[int] = None
    on_hold: Optional[int] = None
    dropped: Optional[int] = None
    plan_to_watch: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Status':
        assert isinstance(obj, dict)
        watching = from_union([from_none, lambda x: int(from_str(x))], obj.get("watching"))
        completed = from_union([from_none, lambda x: int(from_str(x))], obj.get("completed"))
        on_hold = from_union([from_none, lambda x: int(from_str(x))], obj.get("on_hold"))
        dropped = from_union([from_none, lambda x: int(from_str(x))], obj.get("dropped"))
        plan_to_watch = from_union([from_none, lambda x: int(from_str(x))], obj.get("plan_to_watch"))
        return Status(watching, completed, on_hold, dropped, plan_to_watch)

    def to_dict(self) -> dict:
        result: dict = {}
        result["watching"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.watching)
        result["completed"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.completed)
        result["on_hold"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.on_hold)
        result["dropped"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.dropped)
        result["plan_to_watch"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.plan_to_watch)
        return result
