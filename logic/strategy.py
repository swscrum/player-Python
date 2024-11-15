from typing import List
from models.game_state import GameState
from models.player_action import PlayerAction


def decide(gameState: GameState) -> List[PlayerAction]:
    # TODO: place your logic here
    for base in gameState.bases:
        print(base)

    return [PlayerAction(0, 0, 0)]
