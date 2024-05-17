from typing import List
from models.game_state import GameState
from models.player_action import PlayerAction
from models.base import Base
from logic.x_functions import *
from logic.one_functions import *
from logic.me_functions import *

gamestate: GameState


def decide(game_state: GameState) -> List[PlayerAction]:
    global gamestate
    gamestate = game_state
    actions: List[PlayerAction] = []

    mybases, otherbases = get_base_list()

    otherbases = sort_bases_by_pop(otherbases)

    my_inactive_bases = mybases

    for base in my_inactive_bases:
        if base.population > gamestate.config.base_levels[base.level].upgrade_cost:
            actions.append(upgrade(base))
            my_inactive_bases.pop(my_inactive_bases.index(base))
    
    for base in my_inactive_bases:
        if base.population > get_max_population(base)/2:
            for hostilebase in otherbases:
                tmp_action:PlayerAction = attack(base, hostilebase)
                if tmp_action.src >= 0 and tmp_action.dest >= 0 and tmp_action.amount > 0:
                    actions.append(tmp_action)
                    my_inactive_bases.pop(my_inactive_bases.index(base))
                    break

    for base in my_inactive_bases:
        pass

    return actions


def get_base_list() -> tuple[List[Base], List[Base]]:
    for base in gamestate.bases:
        mybases: List[Base] = []
        otherbases: List[Base] = []
        if base.player:
            mybases.append(base)
        else:
            otherbases.append(base)
    
    return mybases, otherbases