class PlayerAction:
    src: int    # uid of source base
    dest: int   # uid of destination base
    amount: int # number of bits moved


    def __init__(self, src:int, dest:int, amount:int):
        self.src = src
        self.dest = dest 
        self.amount = amount

    def __str__(self) -> str:
        return f"({self.src}) -> ({self.dest}): ({self.amount})"

    def serialize(self):
        return {
            'src': self.src,
            'dest': self.dest,
            'amount': self.amount
        }
