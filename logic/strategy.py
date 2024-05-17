from typing import List
from models.game_state import GameState
from models.player_action import PlayerAction
import math

def get_own_bases(gameState):
    own_bases = []
    for base in gameState.bases:
        if base.player == "04":
            own_bases.append(base)
    return own_bases




def get_closest_base(own_base, all_existing_bases):
    shortest_base = all_existing_bases[0]
    shortest_distance = own_base.distance(all_existing_bases[0])

    for base in all_existing_bases:
        current_distance = base.distance(base)
        if current_distance < shortest_distance and str(base) != str(own_base):
            shortest_distance = current_distance
            shortest_base = base

    return shortest_base



def decide(gameState: GameState) -> List[PlayerAction]:
    own_bases = get_own_bases(gameState)

    print(gameState)

    base = get_closest_base(own_bases[0], own_bases)

    return [PlayerAction(0, 0, 0)]
