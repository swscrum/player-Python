from logic.strategy import *
from models.base_level import BaseLevel
from models.player_action import PlayerAction


def base_overflow(base: Base):
    return base.population - gamestate.config.base_levels[base.level].max_population 
# returns difference in base population and max population
# +val: base underflow, -val: base overflow

def attack(attacker: Base, target: Base, amount: int) -> PlayerAction:
    arriving_units = units_needed_to_defeat_base(attacker.uid , target.uid)
    if arriving_units < 0:
        return PlayerAction(-1, -1, -1)
    if units_needed_to_defeat_base(attacker.uid , target.uid) < amount:
        return PlayerAction(-1, -1, -1)
    return PlayerAction(attacker.uid, target.uid, amount)

if __name__ == '__main__':
    print('hello world')
