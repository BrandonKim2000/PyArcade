from pyarcade.game_interface import GameInterface


class MastermindGame(GameInterface):
    """ A class representing a Mastermind game session.

    Note:
        For now, Mastermind must have a hidden sequence of length 4 in which all 4 integers may take on values
        between 0 and 9.
    """
    def __init__(self):
        pass

    def create_game(self, request: dict) -> dict:
        """ Upon calling create_game, the Mastermind game should initialize its hidden sequence

         Args:
             request: dictionary containing single key-value pair. The key is "game_id".

         Returns:
            reply: dictionary containing the session_id in the request.
        """
        return {}

    def read_game(self, request: dict) -> dict:
        """
        Args:
            request: dictionary containing single key-value pair. The key is "session_id". The value is a
            integer unique to all ongoing game sessions.

        Returns:
            reply: dictionary containing three keys.
                "guesses": all previous guesses and their respective numbers of cows and bulls
                for this game_session. All guesses should be kept as a list of tuples under the key "guesses."
                A guess of (0, 1, 2, 3) that has one cow and two bulls should be APPENDED to the list as
                ((0, 1, 2, 3), (1, 2)).
                "session_id": session_id provided with the original request.
                "done": True or False depending on whether the game is over.

            So the overall reply could look like:
            {"guesses": [((0, 1, 2, 3), (1, 2), ((3, 2, 1, 0), (2, 1))], "session_id": 1, "done": False}
        """
        return {}

    def update_game(self, request: dict) -> dict:
        """
        Args:
            request: dictionary containing two key-value pairs. One key is "session_id". The value is a
            integer unique to all ongoing game sessions. The second key is "guess." The value should be a tuple
            of four integers.

        Returns:
            reply: dictionary containing three keys.
                "guesses": all previous guesses and their respective numbers of cows and bulls
                for this game_session. All guesses should be kept as a list of tuples under the key "guesses."
                A guess of (0, 1, 2, 3) that has one cow and two bulls should be APPENDED to the list as
                ((0, 1, 2, 3), (1, 2)).
                "session_id": session_id provided with the original request.
                "done": True or False depending on whether the game is over.

            So the overall reply could look like:
            {"guesses": [((0, 1, 2, 3), (1, 2), ((3, 2, 1, 0), (2, 1))], "session_id": 1, "done": False}
        """
        return {}

    def delete_game(self, request: dict) -> dict:
        """
        Args:
            request: dictionary containing single key-value pair. The key is "session_id". The value is a
            integer unique to all ongoing game sessions.

        Returns:
            reply: dictionary containing the session_id in the request.
        """
        return {}
