class Position:
    # x: int # x coordinate
    # y: int # y coordinate
    # z: int # z coordinate

    # @classmethod
    # def fromAttributes(cls, x: int, y: int, z: int):
    #     position = {
    #         'x': x,
    #         'y': y,
    #         'z': z
    #     }
    #     return cls(position)

    def __init__(self, x: int, y: int, z:int):
        self.x: int = x
        self.y: int = y
        self.z: int = z

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
