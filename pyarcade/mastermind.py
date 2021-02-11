import random

from pyarcade.game_interface import GameInterface


class MastermindGame(GameInterface):
    """ A class representing a Mastermind game session.

    Note:
        For now, Mastermind must have a hidden sequence of length 4 in which all 4 integers may take on values
        between 0 and 9.
    """

    sessions = 0

    def __init__(self):
        self.games = {}

    def create_game(self, request: dict) -> dict:
        """ Upon calling create_game, the Mastermind game should initialize its hidden sequence

         Args:
             request: dictionary containing single key-value pair. The key is "game_id".

         Returns:
            reply: dictionary containing the session_id in the request.
        """
        MastermindGame.sessions += 1
        self.games[MastermindGame.sessions] = {"guesses": [], "session_id": 0, "done": False}
        self.games[MastermindGame.sessions]["session_id"] = MastermindGame.sessions
        i1 = random.randrange(0, 9)
        i2 = random.randrange(0, 9)
        while i2 == i1:
            i2 = random.randrange(0, 9)
        i3 = random.randrange(0, 9)
        while i3 == i1 or i3 == i2:
            i3 = random.randrange(0, 9)
        i4 = random.randrange(0, 9)
        while i4 == i1 or i4 == i2 or i4 == i3:
            i4 = random.randrange(0, 9)
        self.games[MastermindGame.sessions]["nums"] = (i1, i2, i3, i4)

        return {"session_id": self.games[MastermindGame.sessions]["session_id"]}

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

        return {"guesses": self.games[request["session_id"]]["guesses"], "session_id": self.games[request["session_id"]]["session_id"], "done": self.games[request["session_id"]]["done"]}

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
        cows = 0
        bulls = 0
        for i in range(4):
            if request["guess"][i] == self.games[request["session_id"]]["nums"][i]:
                bulls += 1
            elif request["guess"][i] in self.games[request["session_id"]]["nums"]:
                cows += 1

        self.games[request["session_id"]]["guesses"].append((request["guess"], (cows, bulls)))
        if bulls == 4:
            self.games[request["session_id"]]["done"] = True

        return {"guesses": self.games[request["session_id"]]["guesses"], "session_id": self.games[request["session_id"]]["session_id"], "done": self.games[request["session_id"]]["done"]}

    def delete_game(self, request: dict) -> dict:
        """
        Args:
            request: dictionary containing single key-value pair. The key is "session_id". The value is a
            integer unique to all ongoing game sessions.

        Returns:
            reply: dictionary containing the session_id in the request.
        """
        return {}
