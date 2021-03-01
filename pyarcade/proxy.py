from pyarcade.game_interface import GameInterface
from pyarcade.mastermind import MastermindGame
from pyarcade.minesweeper import MinesweeperGame


class MastermindGameProxy(GameInterface):
    """ MastermindGameProxy is meant to be a mediator between client code attempting to play the game
    Mastermind and the Mastermind implementation. More specifically, this class's responsibility
    is to validate requests before passing them on to a Mastermind instance. Separating the responsibility of
    validating inputs to a game and actually running a game helps us follow the single-responsibility principle

    Args:
        game_instance: A reference to the game being played.
    """

    def __init__(self, game_instance: MastermindGame):
        self.game_instance = game_instance

    def create_game(self, request: dict) -> dict:
        """
        Args:
            request: dictionary containing single key-value pair. The key is "game_id". The value
            should be zero.

        Returns:
            reply: dictionary containing a single key-value pair. The key is "session_id". The value is a
            integer unique to all ongoing game sessions. If the request is invalid, a session_id of
            zero should be returned. Otherwise, pass the request onto the game.
        """
        if isinstance(request, dict):
            if "game_id" in request.keys():
                if isinstance(request["game_id"], int):
                    if request["game_id"] == 0:
                        return self.game_instance.create_game(request)

        return {"session_id": 0}

    def read_game(self, request: dict) -> dict:

        if self.valid_game(request):
            return self.game_instance.read_game(request)

        return {"session_id": 0}

    def update_game(self, request: dict) -> dict:
        """
        Args:
            request: dictionary containing two key-value pairs. One key is "session_id". The value is a
            integer unique to all ongoing game sessions. The second key is "guess." The value should be a tuple
            of four integers.

        Returns:
            reply: dictionary containing a single key-value pair. The key is "session_id". The value is a
            integer unique to all ongoing game sessions. If the request is invalid, a session_id of
            zero should be returned. Otherwise, pass the request onto the game.
        """
        if self.valid_game(request):
            if "guess" in request.keys():
                if isinstance(request["guess"], tuple):
                    if list(map(type, request["guess"])) == [int, int, int, int]:
                        return self.game_instance.update_game(request)

        return {"session_id": 0}

    def delete_game(self, request: dict) -> dict:
        """
        Args:
            request: dictionary containing single key-value pair. The key is "session_id". The value is a
            integer unique to all ongoing game sessions.

        Returns:
            reply: dictionary containing single key-value pair. The key is "session_id". The value is a
            integer unique to all ongoing game sessions. If the session_id is invalid, then a session_id of
            zero is returned. Otherwise, pass the request onto the game.
        """
        if self.valid_game(request):
            return self.game_instance.delete_game(request)

        return {"session_id": 0}

    def valid_game(self, request: dict) -> bool:
        if isinstance(request, dict):
            if "session_id" in request.keys():
                if isinstance(request["session_id"], int):
                    if request["session_id"] in self.game_instance.games.keys():
                        return True
        return False

class MinesweeperGameProxy(GameInterface):

    def __init__(self, game_instance: MinesweeperGame):
        self.game_instance = game_instance

    def create_game(self, request: dict) -> dict:
        if isinstance(request, dict):
            if "game_id" in request.keys():
                if isinstance(request["game_id"], int):
                    if request["game_id"] == 1:
                        return self.game_instance.create_game(request)

        return {"session_id": 0}

    def read_game(self, request: dict) -> dict:
        if self.valid_game(request):
            return self.game_instance.read_game(request)

        return {"session_id": 0}

    def update_game(self, request: dict) -> dict:
        if self.valid_game(request):
            if "guess" in request.keys():
                if isinstance(request["guess"], tuple):
                    if list(map(type, request["guess"])) == [int, int]\
                            or list(map(type, request["guess"])) == [int, int, str]:
                        return self.game_instance.update_game(request)

        return {"session_id": 0}

    def delete_game(self, request: dict) -> dict:
        if self.valid_game(request):
            return self.game_instance.delete_game(request)

        return {"session_id": 0}

    def valid_game(self, request: dict) -> bool:
        if isinstance(request, dict):
            if "session_id" in request.keys():
                if isinstance(request["session_id"], int):
                    if request["session_id"] in self.game_instance.games.keys():
                        return True
        return False
