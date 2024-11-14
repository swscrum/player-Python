class BaseLevel:
    # max_population: int  # number of sustainable bits
    # upgrade_cost: int    # bits required to unlock next upgrade
    # spawn_rate: int      # number uf bits spawned per tick


    # @classmethod
    # def fromAttributes(cls, maxPopulation:int, upgradeCost:int, spawnRate:int):
    #     baselevel = {
    #         'max_population': maxPopulation,
    #         'upgrade_cost': upgradeCost,
    #         'spawn_rate': spawnRate
    #     }
    #     return cls(baselevel)

    def __init__(self, max_population: int, upgrade_cost: int, spawn_rate: int):
        self.max_population: int = max_population
        self.upgrade_cost: int = upgrade_cost
        self.spawn_rate: int = spawn_rate
