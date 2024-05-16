from models.base_level import BaseLevel

class PathsConfig:
    gracePeriod: int    # time until groups of bits take damage
    deathRate: int      # time until groups of bits take damage

    @classmethod
    def fromAttributes(cls, gracePeriod: int, deathRate: int):
        pathsconfig = {
            'gracePeriod': gracePeriod,
            'deathRate': deathRate
        }
        return cls(pathsconfig)

    def __init__(self, pathsconfig: dict):
        self.gracePeriod = pathsconfig['gracePeriod']
        self.deathRate = pathsconfig['deathRate']

class GameConfig:
    baseLevels: list[BaseLevel]    # all available base levels
    paths: PathsConfig  # settings containing paths between bases

    @classmethod
    def fromAttributes(cls, baseLevels: list[BaseLevel], paths: PathsConfig):
        gameconfig = {
            'baseLevels': baseLevels,
            'paths': paths
        }
        return cls(gameconfig)

    def __init__(self, gameconfig: dict) -> None:
        self.baseLevels = gameconfig['baseLevels']
        self.paths = gameconfig['paths']
