from models.position import Position
from models.board_action import BoardAction
from logic.incoming_units import IncomingUnits
from logic.strategy import *


def getdistance(pos1, pos2) -> int:
    if type(pos1) == type(pos2) == type(Position) and type(pos1) == type(Position):
        return int(((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2 + (pos1.z - pos2.z) ** 2) ** 0.5)
    elif type(pos1) == type(pos2) == type(tuple[int, int, int]):
        return int(((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 + (pos1[2] - pos2[2]) ** 2) ** 0.5)
    else:
        return -1  # TypeError


def incoming_units(base: Base) -> IncomingUnits:
    """
    returns a dictionary like object containing the amount of change in unites at a given amount of ticks into the future

    :param base:
        base the units are incoming to
    :return:
        dict{int: int} like
        incoming_units(base)[ticks_into_future] -> the sum of units incoming during the Round with friendly units being
        counted positive and enemy units
    """
    incoming: IncomingUnits = IncomingUnits()
    for act in gamestate.actions:
        if act.dest == base.uid:
            timeremaining = act.progress.distance - act.progress.traveled
            if act.player == gamestate.game.player:
                incoming[timeremaining] += act.amount
            else:
                incoming[timeremaining] -= act.amount
    return incoming


def get_overflowing_bases():
    pass


def calculate_idle_moves() -> list[PlayerAction]:
    pass


def units_until_upgrade(base: Base) -> int:
    return gamestate.config.base_levels[base.level].upgrade_cost - base.units_until_upgrade


def upgrade(base: Base, amount: int = None) -> PlayerAction:
    if amount is None:
        amount = base.population / 2
    amount = min(amount, units_until_upgrade(base))
    return PlayerAction(base.uid, base.uid, amount)


if __name__ == '__main__':
    print(getdistance((1, 2, 3), (4, 5, 6)))
