class Progress:
    def __init__(self, distance: int, traveled: int):
        self.distance: int = distance
        self.traveled: int = traveled

    def __str__(self) -> str:
        return f"({self.distance}/{self.traveled})"
