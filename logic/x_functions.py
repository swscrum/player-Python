from logic.strategy import *
from models.base import Base
from models.player_action import PlayerAction


def base_overflow(base: Base):
    return base.population - gamestate.config.base_levels[base.level].max_population 
# returns difference in base population and max population
# +val: base overflow, -val: base underflow

def attack(attacker: Base, target: Base, amount: int) -> PlayerAction:
    arriving_units = units_needed_to_defeat_base(attacker.uid , target.uid)
    if arriving_units < 0:
        return PlayerAction(-1, -1, -1)
    if units_needed_to_defeat_base(attacker.uid , target.uid) < amount:
        return PlayerAction(-1, -1, -1)
    return PlayerAction(attacker.uid, target.uid, amount)

def sort_bases_by_pop(bases: list[Base]):
    for i in range(len(bases)):
        min_idx = i
        for j in range(i+1, len(bases)):
            if bases[min_idx].population > bases[j].population:
                min_idx = j
        bases[i].population, bases[min_idx].population = bases[min_idx].population, bases[i].population


if __name__ == '__main__':
    print('hello world')
