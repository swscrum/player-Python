from flask import Flask, jsonify, request
from flask_cors import CORS

from logic.strategy import decide
from models.game_state import GameState

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def identify():
    return 'Bitwars Python-Player'


@app.route('/', methods=['POST'])
def index():
    return jsonify(decide(GameState(request.get_json())))
