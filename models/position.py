class Position:
    def __init__(self, x: int, y: int, z:int):
        self.x: int = x
        self.y: int = y
        self.z: int = z

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
