class BaseLevel:
    maxPopulation: int  # number of sustainable bits
    upgradeCost: int    # bits required to unlock next upgrade
    spawnRate: int      # number uf bits spawned per tick


    @classmethod
    def fromAttributes(cls, maxPopulation:int, upgradeCost:int, spawnRate:int):
        baselevel = {
            'maxPopulation': maxPopulation,
            'upgradeCost': upgradeCost,
            'spawnRate': spawnRate
        }
        return cls(baselevel)

    def __init__(self, baselevel: dict):
        self.maxPopulation = baselevel['maxPopulation']
        self.upgradeCost = baselevel['upgradeCost']
        self.spawnRate = baselevel['spawnRate']
