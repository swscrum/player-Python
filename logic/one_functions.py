from strategy import *
from models.position import Position


def getdistance(pos1, pos2) -> int:
    if type(pos1) == type(pos2) == type(Position) and type(pos1) == type(Position):
        return int(((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2 + (pos1.z - pos2.z) ** 2) ** 0.5)
    elif type(pos1) == type(pos2) == type(tuple[int, int, int]):
        return int(((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 + (pos1[2] - pos2[2]) ** 2) ** 0.5)
    else:
        return -1  # TypeError


def get_overflowing_bases():
    pass


def calculate_idle_moves() -> list[PlayerAction]:
    pass


def units_until_upgrade(base) -> int:
    return gamestate.config.base_levels[base.level].upgrade_cost - base.units_until_upgrade


def upgrade(base, amount: int) -> PlayerAction:
    amount = min(amount, units_until_upgrade(base))
    return PlayerAction(base.uid, base.uid, amount)


if __name__ == '__main__':
    print(getdistance((1, 2, 3), (4, 5, 6)))
