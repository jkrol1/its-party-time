from enum import Enum, IntEnum


class EventPermission(IntEnum):
    CONTRIBUTE = 1
    MODERATE = 2
    DELETE_EVENT = 4


class Role(Enum):
    USER = [EventPermission.CONTRIBUTE]
    MODERATOR = [EventPermission.CONTRIBUTE, EventPermission.MODERATE]
    ADMIN = [EventPermission.CONTRIBUTE, EventPermission.MODERATE, EventPermission.DELETE_EVENT]
