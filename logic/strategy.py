from typing import List
from models.game_state import GameState
from models.player_action import PlayerAction


def getdistance(x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> int:
    return int(((x1-x2)**2 + (y1-y1)**2 + (z1-z2)**2) ** 0.5)


def decide(gamestate: GameState) -> List[PlayerAction]:
    # TODO: place your logic here
    return [PlayerAction(0, 0, 0)]
