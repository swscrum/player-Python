from models.position import Position


def getdistance(x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> int:
    return int(((x1-x2)**2 + (y1-y1)**2 + (z1-z2)**2) ** 0.5)


def getdistance(pos1, pos2) -> int:
    if type(pos1) == type(pos2) == type(Position) and type(pos1) == type(Position):
        return int(((pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2 + (pos1.z - pos2.z)**2) ** 0.5)
    elif type(pos1) == type(pos2) == type(tuple[int, int, int]):
        return int(((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2 + (pos1[2] - pos2[2])**2) ** 0.5)


if __name__ == '__main__':
    print(getdistance((1, 2, 3), (4, 5, 6)))
