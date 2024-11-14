class Progress:
    # distance: int # distance between the bases
    # traveled: int # distance already traveled

    # @classmethod
    # def fromAttributes(cls, distance:int, traveled:int):
    #     progress = {
    #         'distance': distance,
    #         'traveled': traveled
    #     }
    #     return cls(progress)

    def __init__(self, distance: int, traveled: int):
        self.distance: int = distance
        self.traveled: int = traveled

    def __str__(self) -> str:
        return f"({self.distance}/{self.traveled})"
