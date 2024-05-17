from typing import List
from models.game_state import GameState
from models.player_action import PlayerAction
import math

def get_own_bases(all_existing_bases):
    own_bases = []
    for base in all_existing_bases:
        if base.player == 4:
            own_bases.append(base)
    return own_bases


def get_neutral_bases(all_existing_bases):
    neutral_bases = []
    for base in all_existing_bases:
        if base.player == 0:
            neutral_bases.append(base)

    return neutral_bases

def get_closest_base(own_base, all_existing_bases):
    shortest_base = all_existing_bases[0]
    shortest_distance = own_base.distance(all_existing_bases[0])

    for base in all_existing_bases:
        current_distance = base.distance(base)
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_base = base

    return shortest_base

def decide(gameState: GameState) -> List[PlayerAction]:
    own_bases = get_own_bases(gameState.bases)
    neutral_bases = get_neutral_bases(gameState.bases)

    print(gameState)

    return [PlayerAction(0, 0, 0)]
