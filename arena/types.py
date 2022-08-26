from enum import Enum


class KnightStatus(str, Enum):
    LIVE = "live"
    DEAD = "dead"
    DROWNED = "drowned"


class ItemTypes(str, Enum):
    AXE = "axe"
    DAGGER = "dagger"
    HELMET = "helmet"
    MAGIC_STAFF = "magic_staff"


class KnightMoves(str, Enum):
    N = "N"
    E = "E"
    S = "S"
    W = "W"


class Knights(str, Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"
