from dataclasses import dataclass
from typing import Optional, Any

from pyMALv2.models.author import Author
from pyMALv2.models.utils import from_union, from_none, from_str, to_class


@dataclass
class Authors:
    author: Optional[Author] = None
    role: Optional[str] = None