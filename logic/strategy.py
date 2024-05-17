from typing import List
from models.game_state import GameState
from models.player_action import PlayerAction
from models.base import Base
from logic.x_functions import *
from logic.one_functions import *
from logic.me_functions import *

gamestate: GameState
actions: List[PlayerAction] = []
mybases: List[Base] = []
otherbases: List[Base] = []


def decide(game_state: GameState) -> List[PlayerAction]:
    global gamestate
    global actions
    global mybases
    global otherbases
    gamestate = game_state

    for base in gamestate.bases:
        if base.player:
            mybases.append(base)
        else:
            otherbases.append(base)

    for base in mybases:
        if base.population > gamestate.config.base_levels[base.level].upgrade_cost:
            actions.append(upgrade_base(base))

    return actions
