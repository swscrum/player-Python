class Game:
    uid: int                # uid of game
    tick: int               # tick in game
    playerCount: int        # number of players
    remainingPlayers: int   # number of players remaining
    player: int             # uid of your player

    def __init__(self, uid: int, tick: int, playerCount: int, remainingPlayers: int, player: int):
        self.uid = uid
        self.tick = tick
        self.playerCount = playerCount
        self.remainingPlayers = remainingPlayers
        self.player = player
