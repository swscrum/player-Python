from models.base import Base
from models.board_action import BoardAction
from models.game import Game
from models.game_config import GameConfig


class GameState:
    actions: list[BoardAction]
    bases: list[Base]
    config: GameConfig
    game: Game

    def __init__(self, actions: list[BoardAction], bases: list[Base], config: GameConfig, game: Game) -> None:
        self.actions = actions
        self.bases = bases
        self.config = config
        self.game = game
