class Game:
    uid: int                # uid of game
    tick: int               # tick in game
    playerCount: int        # number of players
    remainingPlayers: int   # number of players remaining
    player: int             # uid of your player

    @classmethod
    def fromAttributes(cls, uid: int, tick: int, playerCount: int, remainingPlayers: int, player: int):
        game = {
            'uid': uid,
            'tick': tick,
            'playerCount': playerCount,
            'remainingPlayers': remainingPlayers,
            'player': player
        }
        return cls(game)

    def __init__(self, game: dict):
        self.uid = game['uid']
        self.tick = game['tick']
        self.playerCount = game['playerCount']
        self.remainingPlayers = game['remainingPlayers']
        self.player = game['player']
