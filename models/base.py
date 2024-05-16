
from models.position import Position


class Base:
    position: Position      # position of the base
    uid: int                # uid of the base
    player: int             # uid of the owning player
    population: int         # number of bits in the base
    level: int              # level of the base
    unitsUntilUpgrade: int  # bits needed for until the next upgrade

    def __init__(self, position: Position, uid: int, player: int,  population: int, level: int, unitsUntilUpgrade: int):
        self.position = position
        self.uid = uid
        self.player = player
        self.population = population
        self.level = level
        self.unitsUntilUpgrade = unitsUntilUpgrade
