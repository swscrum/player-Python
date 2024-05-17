from logic.strategy import *
from models.base_level import BaseLevel
from models.player_action import PlayerAction


def base_overflow(base: Base):
    return base.population - gamestate.config.base_levels[base.level].max_population 
# returns difference in base population and max population
# +val: base underflow, -val: base overflow
    
def upgrade_base(base: Base, upby: int):
    if None == upby:
        upby = base.population / 2
    return PlayerAction(base.uid, base.uid, upby)


if __name__ == '__main__':
    print('hello world')
