from logic.strategy import *


def units_needed_to_defeat_base(srcid: int, destid: int) -> int:
    destbase = get_base_from_uid(destid)
    srcbase = get_base_from_uid(srcid)
    if destbase.uid < 0 or srcbase.uid < 0:
        return -1
    dist = getdistance(srcbase.position, destbase.position)
    if dist < 0:
        return -1
    units_at_dest_after_travel = destbase.population + gamestate.config.base_levels[destbase.level].spawn_rate * dist
    return adjust_for_death_rate(units_at_dest_after_travel, dist, gamestate)


def adjust_for_death_rate(units_that_arrive: int, distance: int) -> int:
    return units_that_arrive + get_death_rate * max(distance - get_grace_period, 0)


def unit_amount_after_travel(units_sent: int, distance: int) -> int:
    out = units_sent - get_death_rate * max(distance - get_grace_period, 0)
    print(f"\treturn: {out}\n")
    return out


def get_base_from_uid(uid: int) -> Base:
    for base in gamestate.bases:
        if base.uid == uid:
            return base
    return Base.fromAttributes(Position.fromAttributes(0, 0, 0), -1, 0, 0, 0, 0)


def get_upgrade_cost(base:Base) -> int:
    return gamestate.config.base_levels[base.level+1].upgrade_cost

def get_max_population(base:Base) -> int:
    return gamestate.config.base_levels[base.level].max_population

def get_spawn_rate(base:Base) -> int:
    return gamestate.config.base_levels[base.level].spawn_rate

def get_grace_period() -> int:
    return gamestate.config.paths.grace_period

def get_death_rate() -> int:
    return gamestate.config.paths.death_rate