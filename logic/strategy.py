from typing import List
from models.game_state import GameState
from models.player_action import PlayerAction
from models.base import Base
import x_functions
from one_functions import *


def getdistance(x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> int:
    return int(((x1-x2)**2 + (y1-y1)**2 + (z1-z2)**2) ** 0.5)


def decide(gamestate: GameState) -> List[PlayerAction]:
    actions: List[PlayerAction] = []
    mybases: List[Base] = []
    otherbases: List[Base] = []
    for base in gamestate.bases:
        if base.player:
            mybases.append(base)
        else:
            otherbases.append(base)
    for base in mybases:
        if base.population > gamestate.config.base_levels[base.level].upgrade_cost:
            actions.append(PlayerAction(base.uid, base.uid, gamestate.config.base_levels[base.level].upgrade_cost))

    return actions
