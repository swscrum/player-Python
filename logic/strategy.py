from typing import List
from models.game_state import GameState
from models.player_action import PlayerAction
from models.base import Base
from logic.one_functions import *
from logic.me_functions import *


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
