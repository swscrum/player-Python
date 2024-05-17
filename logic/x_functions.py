from logic.strategy import *
from models.base_level import BaseLevel
from models.player_action import PlayerAction


def base_overflow(base: Base):
    return base.population - gamestate.config.base_levels[base.level].max_population 
# returns difference in base population and max population
# +val: base underflow, -val: base overflow

def attack(attacker: Base, target: Base, amount: int) -> PlayerAction:
    if units_needed_to_defeat_base(attacker.uid , target.uid) == amount:
        return PlayerAction(attacker.uid, target.uid, amount)
    else:
        return -1


if __name__ == '__main__':
    print('hello world')
