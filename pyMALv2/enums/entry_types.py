from enum import Enum


class ListEntryTypes(Enum):
    ANIME = 'anime'
    MANGA = 'manga'


class AnimeListEntryStatuses(str, Enum):
    WATCHING = 'watching'
    COMPLETED = 'completed'
    ON_HOLD = 'on_hold'
    DROPPED = 'dropped'
    PLANNED = 'planned'


class MangaListEntryStatuses(str, Enum):
    READING = 'reading'
    COMPLETED = 'completed'
    ON_HOLD = 'on_hold'
    DROPPED = 'dropped'
    PLANNED = 'plan_to_read'
