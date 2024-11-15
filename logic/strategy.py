import math
from typing import List

from models.base import Base
from models.game_state import GameState
from models.player_action import PlayerAction

def distance(x1, y1, z1, x2, y2, z2):
    d = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2) + math.pow(z1-z2, 2))
    return math.floor(d)


def get_own_bases(bases_list):
    own_bases = []
    for base in bases_list:
        if base.player == 1:
            own_bases.append(base)
    return own_bases

def decide(gameState: GameState) -> List[PlayerAction]:
    # TODO: place your logic here

    own_bases = get_own_bases(gameState.bases)
    print(len(own_bases))

    return [PlayerAction(0, 0, 0)]
