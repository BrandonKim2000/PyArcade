from flask import Flask, request
from pyarcade.connect_four import ConnectFourGame
from pyarcade.minesweeper import MinesweeperGame
from pyarcade.mastermind import MastermindGame
from pyarcade.proxy import MastermindGameProxy, MinesweeperGameProxy, ConnectFourGameProxy

def create_app():
    flask_app = Flask(__name__)

    mastermindGame = MastermindGame()
    mmProxy = MastermindGameProxy(mastermindGame)
    minesweeperGame = MinesweeperGame()
    msProxy = MinesweeperGameProxy(minesweeperGame)
    connectFourGame = ConnectFourGame()
    cfProxy = ConnectFourGameProxy(connectFourGame)

    # Mastermind
    @flask_app.route("/mastermind", methods=["GET"])
    def get_mastermind():
        return mmProxy.read_game(request.get_json())

    @flask_app.route("/mastermind", methods=["POST"])
    def post_mastermind():
        return mmProxy.rcreate_game(request.get_json())

    @flask_app.route("/mastermind", methods=["PUT"])
    def put_mastermind():
        return mmProxy.update_game(request.get_json())

    @flask_app.route("/mastermind", methods=["DELETE"])
    def delete_mastermind():
        return mmProxy.delete_game(request.get_json())

    # Minesweeper
    @flask_app.route("/minesweeper", methods=["GET"])
    def get_minesweeper():
        return msProxy.read_game(request.get_json())

    @flask_app.route("/minesweeper", methods=["POST"])
    def post_minesweeper():
        return msProxy.rcreate_game(request.get_json())

    @flask_app.route("/minesweeper", methods=["PUT"])
    def put_mminesweeper():
        return msProxy.update_game(request.get_json())

    @flask_app.route("/minesweeper", methods=["DELETE"])
    def delete_minesweeper():
        return msProxy.delete_game(request.get_json())

    # Connect Four
    @flask_app.route("/connectfour", methods=["GET"])
    def get_mconnectfour():
        return cfProxy.read_game(request.get_json())

    @flask_app.route("/connectfour", methods=["POST"])
    def post_connectfour():
        return cfProxy.rcreate_game(request.get_json())

    @flask_app.route("/connectfour", methods=["PUT"])
    def put_connectfour():
        return cfProxy.update_game(request.get_json())

    @flask_app.route("/connectfour", methods=["DELETE"])
    def delete_connectfour():
        return cfProxy.delete_game(request.get_json())


    return flask_app
