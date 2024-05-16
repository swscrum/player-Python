class Position:
    x: int # x coordinate
    y: int # y coordinate
    z: int # z coordinate

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
