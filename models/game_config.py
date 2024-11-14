from models.base_level import BaseLevel

class PathConfig:
    def __init__(self, grace_period: int, death_rate: int):
        self.grace_period = grace_period
        self.death_rate = death_rate

class GameConfig:
    def __init__(self, base_levels: list[BaseLevel], paths: PathConfig):
        self.base_levels: list[BaseLevel] = base_levels
        self.paths: PathConfig = paths
