class BaseLevel:
    def __init__(self, max_population: int, upgrade_cost: int, spawn_rate: int):
        self.max_population: int = max_population
        self.upgrade_cost: int = upgrade_cost
        self.spawn_rate: int = spawn_rate
