from strategy import *
from x_functions import *
from one_functions import *
from models.game_state import GameState
from models.base import Base


def units_needed_to_defeat_base(srcid: int, destid: int, gamestate: GameState):
    destbase = get_base_from_uid(destid, gamestate)
    srcbase = get_base_from_uid(srcid, gamestate)
    dist = getdistance(srcbase.position, destbase.position)
    units_at_dest_after_travel = destbase.population + gamestate.config.base_levels[destbase.level].spawn_rate * dist
    return adjust_for_death_rate(units_at_dest_after_travel, dist, gamestate)


def adjust_for_death_rate(units_that_arrive: int, distance: int, gamestate: GameState):
    grace_period = gamestate.config.paths.grace_period
    death_rate = gamestate.config.paths.death_rate
    return units_that_arrive + death_rate * max(distance - grace_period, 0)


def unit_amount_after_travel(units_sent: int, distance: int, gamestate: GameState) -> int:
    grace_period = gamestate.config.paths.grace_period
    death_rate = gamestate.config.paths.death_rate
    return units_sent - death_rate * max(distance - grace_period, 0)


def get_base_from_uid(uid: int, gamestate: GameState) -> Base:
    for base in gamestate.bases:
        if base.uid == uid:
            return base
    return None
