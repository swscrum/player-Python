class Progress:
    distance: int # distance between the bases
    traveled: int # distance already traveled

    def __init__(self, distance:int, traveled:int):
        self.distance = distance 
        self.traveled = traveled 

    def __str__(self) -> str:
        return f"({self.distance}/{self.traveled})"