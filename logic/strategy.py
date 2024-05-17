from typing import List
from models.game_state import GameState
from models.player_action import PlayerAction


def getdistance(x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> int:
    return int(((x1-x2)**2 + (y1-y1)**2 + (z1-z2)**2) ** 0.5)


def decide(gameState: GameState) -> List[PlayerAction]:
    actions = List[PlayerAction]
    myBases = List[Base]
    otherBases = List[Base]
    for base in gameState.bases:
        if base.player:
            myBases.append(base)
        else:
            otherBases.append(base)
    for base in myBases:
        if base.population > gameState.config.base_levels[base.level].upgrade_cost:
            actions.append(PlayerAction(base.uid, base.uid, gameState.config.base_levels[base.level].upgrade_cost))

    # TODO: place your logic here
    return actions