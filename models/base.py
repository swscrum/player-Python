
from models.position import Position


class Base:
    position: Position      # position of the base
    uid: int                # uid of the base
    player: int             # uid of the owning player
    population: int         # number of bits in the base
    level: int              # level of the base
    units_until_upgrade: int  # bits needed for until the next upgrade

    @classmethod
    def fromAttributes(cls, position: Position, uid: int, player: int,  population: int, level: int, unitsUntilUpgrade: int):
        base = {
            'position': position,
            'uid': uid,
            'player': player,
            'population': population,
            'level': level,
            'units_until_upgrade': unitsUntilUpgrade
        }
        return cls(base)

    def __init__(self, base: dict):
        self.position = Position(base['position'])
        self.uid = base['uid']
        self.player = base['player']
        self.population = base['population']
        self.level = base['level']
        self.units_until_upgrade = base['units_until_upgrade']
