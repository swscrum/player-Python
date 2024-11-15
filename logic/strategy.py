import math
from typing import List

from models.base import Base
from models.game_state import GameState
from models.player_action import PlayerAction

PLAYER_ID = 1


def calc_distance(b1, b2):
    x1 = b1.position.x
    y1 = b1.position.y
    z1 = b1.position.z

    x2 = b2.position.x
    y2 = b2.position.y
    z2 = b2.position.z

    d = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2) + math.pow(z1-z2, 2))
    return math.floor(d)


def get_own_bases(bases_list):
    own_bases = []
    for base in bases_list:
        if base.player == PLAYER_ID:
            own_bases.append(base)
    return own_bases


def get_foreign_bases(bases_list):
    foreign_bases = []
    for base in bases_list:
        if base.player != PLAYER_ID:
            foreign_bases.append(base)
    return foreign_bases


def travel(src_base, dest_base):
    return PlayerAction(src_base.uid, dest_base.uid, src_base.population - math.floor(math.sqrt(src_base.population)))

def decide(gameState: GameState) -> List[PlayerAction]:
    # TODO: place your logic here

    player_actions = []

    own_bases = get_own_bases(gameState.bases)
    foreign_bases = get_foreign_bases(gameState.bases)

    for own_base in own_bases:
        shortest_distance = 99999
        destination_base = own_base

        for foreign_base in foreign_bases:
            distance = calc_distance(own_base, foreign_base)

            if distance < shortest_distance:
                shortest_distance = distance
                destination_base = foreign_base

        if shortest_distance <= gameState.config.paths.grace_period:
            # Empty base
            if foreign_base.player != 0:
                # empty base that is within grace_period
                player_actions.append(travel(own_base, destination_base))
            # Base of another player with less population than own population within grace_period
            elif foreign_base.population < own_base.population - math.ceil(math.sqrt(own_base.population)):
                player_actions.append(travel(own_base, foreign_base))

            # Base of another player where distance is above grace_period and own population is larger than enemy population
            # And leaving some population for guarding own base behind
            elif own_base.population - math.ceil(math.sqrt(own_base.population)) > gameState.config.base_levels[own_base.level-1]:
                player_actions.append(travel(own_base, own_base))
            else:
                continue
        else:
            player_actions.a
            # Here: Handle logic for when distance to enemy base is above grace_period and potentially from a different player

    return player_actions
