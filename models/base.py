from models.position import Position

class Base:
    def __init__(self, uid: int, name: str, player: int, population: int, level: int, units_until_upgrade: int, position: Position):
        self.uid = uid
        self.name = name
        self.player = player
        self.population = population
        self.level = level
        self.units_until_upgrade = units_until_upgrade
        self.position = position
