from flask import Flask, jsonify, request
from flask_cors import CORS
from uuid import UUID
from logic.strategy import decide
from models.game import Game
from models.game_config import GameConfig, PathConfig
from models.game_state import GameState
from models.base_level import BaseLevel
from models.base import Base
from models.position import Position
from models.board_action import BoardAction
from models.progress import Progress

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def identify():
    app.logger.info("identity called")
    return "Bitwars Python-Player"


@app.route("/", methods=["POST"])
def index():
    data = request.get_json()

    # build config
    config_base_levels = [
        BaseLevel(level["max_population"], level["upgrade_cost"], level["spawn_rate"])
        for level in data["config"]["base_levels"]
    ]
    config_paths = data["config"]["paths"]
    config_paths = PathConfig(config_paths["grace_period"], config_paths["death_rate"])
    game_config = GameConfig(config_base_levels, config_paths)

    # build current game statistics
    game_stats = data["game"]
    game = Game(
        game_stats["uid"],
        game_stats["tick"],
        game_stats["player_count"],
        game_stats["remaining_players"],
        game_stats["player"],
    )

    # build bases
    bases = [
        Base(
            base["uid"],
            base["name"],
            base["player"],
            base["population"],
            base["level"],
            base["units_until_upgrade"],
            Position(
                base["position"]["x"], base["position"]["y"], base["position"]["z"]
            ),
        )
        for base in data["bases"]
    ]

    # build actions of all players
    actions = [
        BoardAction(
            UUID(action["uuid"]),
            action["player"],
            action["src"],
            action["dest"],
            action["amount"],
            Progress(action["progress"]["distance"], action["progress"]["traveled"]),
        )
        for action in data["actions"]
    ]

    game_state = GameState(actions, bases, game_config, game)

    return jsonify([action.serialize() for action in decide(game_state)])
