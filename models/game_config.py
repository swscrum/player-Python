from base_level import BaseLevel

class PathsConfig:
    gracePeriod: int    # time until groups of bits take damage
    deathRate: int      # time until groups of bits take damage

    def __init__(self, gracePeriod: int, deathRate: int):
        self.gracePeriod = gracePeriod
        self.deathRate = deathRate

class GameConfig:
    baseLevels: list    # all available base levels
    paths: PathsConfig  # settings containing paths between bases

    def __init__(self, baseLevels: list, paths: PathsConfig) -> None:
        self.baseLevels = [baseLevels]
        self.paths = paths