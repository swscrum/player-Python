class PlayerAction:
    def __init__(self, src: int, dest: int, amount: int):
        self.src: int = src
        self.dest: int = dest
        self.amount: int = amount

    def __str__(self) -> str:
        return f"({self.src}) -> ({self.dest}): ({self.amount})"

    def serialize(self):
        return {"src": self.src, "dest": self.dest, "amount": self.amount}
