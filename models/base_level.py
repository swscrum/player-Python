class BaseLevel:
    maxPopulation: int  # number of sustainable bits
    upgradeCost: int    # bits required to unlock next upgrade
    spawnRate: int      # number uf bits spawned per tick


    def __init__(self, maxPopulation:int, upgradeCost:int, spawnRate:int):
        self.maxPopulation = maxPopulation
        self.upgradeCost = upgradeCost 
        self.spawnRate = spawnRate