from dataclasses import dataclass
from typing import Optional, List, Any

from pyMALv2.models.utils import from_list, from_str, from_none, from_union


@dataclass
class AlternativeTitles:
    synonyms: Optional[List[str]] = None
    en: Optional[str] = None
    ja: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AlternativeTitles':
        assert isinstance(obj, dict)
        synonyms = from_union([lambda x: from_list(from_str, x), from_none], obj.get("synonyms"))
        en = from_union([from_str, from_none], obj.get("en"))
        ja = from_union([from_str, from_none], obj.get("ja"))
        return AlternativeTitles(synonyms, en, ja)

    def to_dict(self) -> dict:
        result: dict = {}
        result["synonyms"] = from_union([lambda x: from_list(from_str, x), from_none], self.synonyms)
        result["en"] = from_union([from_str, from_none], self.en)
        result["ja"] = from_union([from_str, from_none], self.ja)
        return result
