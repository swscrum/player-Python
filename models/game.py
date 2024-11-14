class Game:
    def __init__(self, uid: int, tick: int, player_count: int, remaining_players: int, player: int):
        self.uid: int = uid
        self.tick: int = tick
        self.player_count: int = player_count
        self.remaining_players: int = remaining_players
        self.player: int = player
