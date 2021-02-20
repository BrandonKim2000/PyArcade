import random

from pyarcade.game_interface import GameInterface


class MinesweeperGame(GameInterface):
    """ A class representing a Minesweeper game session.

    Note:
        For now, Minesweeper will be played on an 8 x 8 board with 10 mines
    """

    sessions = 0

    def __init__(self):
        self.games = {}

    def create_game(self, request: dict) -> dict:
        """ Upon calling create_game, the Minesweeper game should initialize its hidden sequence

         Args:
             request: dictionary containing single key-value pair. The key is "game_id".

         Returns:
            reply: dictionary containing the session_id in the request.
        """
        MinesweeperGame.sessions += 1

        self.games[MinesweeperGame.sessions] = Game(MinesweeperGame.sessions)
        return {"session_id": self.games[MinesweeperGame.sessions].get_session_id()}

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
        board = self.games[request["session_id"]].get_board()
        return {"board": board,
                "session_id": self.games[request["session_id"]].session_id,
                "status": self.games[request["session_id"]].status}

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
        self.games[request["session_id"]].guess(request["guess"][0], request["guess"][1])

        return MinesweeperGame.read_game(self, request)

    def delete_game(self, request: dict) -> dict:
        """
        Args:
            request: dictionary containing single key-value pair. The key is "session_id". The value is a
            integer unique to all ongoing game sessions.

        Returns:
            reply: dictionary containing the session_id in the request.
        """
        del self.games[request["session_id"]]
        return {"session_id": request["session_id"]}


class Game:
    guesses = []
    session_id = 0
    status = False
    nums = ()
    uncovered_spaces = 54
    uncovered = [[False for x in range(8)] for y in range(8)]
    board = [[0 for x in range(8)] for y in range(8)]
    bombs = set()

    def __init__(self, session_id):
        self.session_id = session_id
        while len(self.bombs) < 8:
            self.bombs.add((random.randrange(0, 8), random.randrange(0, 8)))
        for b in self.bombs:
            for i1 in (-1, 0, 1):
                for i2 in (-1, 0, 1):
                    try:
                        self.board[b[0] + i1][b[1] + i2] += 1
                    except IndexError:
                        pass
        for b in self.bombs:
            self.board[b[0]][b[1]] = -1

    def get_session_id(self) -> int:
        return self.session_id

    def get_board(self):
        ret_board = [["B" for x in range(8)] for y in range(8)]
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.uncovered[r][c]:
                    ret_board[r][c] = self.board[r][c]
        return ret_board

    def get_status(self) -> bool:
        return self.status

    def get_guesses(self):
        return self.guesses

    def guess(self, r, c):
        if self.uncovered[r][c]:
            return
        self.guesses.append((r, c))
        self.uncovered[r][c] = True
        if self.board[r][c] == -1:
            self.status = "LOSE"
        else:
            self.uncovered_spaces -= 1
            if self.uncovered_spaces == 0:
                self.status = "WIN!"
