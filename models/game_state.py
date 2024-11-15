from models.base import Base
from models.board_action import BoardAction
from models.game import Game
from models.game_config import GameConfig


class GameState:
    def __init__(
        self,
        actions: list[BoardAction],
        bases: list[Base],
        game_config: GameConfig,
        game: Game,
    ):
        self.config = game_config
        self.game = game
        self.actions = actions
        self.bases = bases
