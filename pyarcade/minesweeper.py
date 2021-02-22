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
        MinesweeperGame.sessions += 1

        self.games[MinesweeperGame.sessions] = Game(MinesweeperGame.sessions, [], set())
        return {"session_id": self.games[MinesweeperGame.sessions].get_session_id()}

    def read_game(self, request: dict) -> dict:
        board = self.games[request["session_id"]].get_board()
        return {"board": board,
                "session_id": self.games[request["session_id"]].session_id,
                "status": self.games[request["session_id"]].status}

    def update_game(self, request: dict) -> dict:
        if len(request["guess"]) >= 3 and request["guess"][2] in ("flag", "f"):
                self.games[request["session_id"]].flag(request["guess"][0], request["guess"][1])
        else:
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


class Game():
    guesses = []
    flags = []
    session_id = 0
    status = False
    nums = ()
    uncovered_spaces = 54
    uncovered = [[False for x in range(8)] for y in range(8)]
    board = [[0 for x in range(8)] for y in range(8)]
    bombs = []

    def __init__(self, session_id, guesses, bombs):
        self.session_id = session_id
        self.guesses = guesses
        bomb_list = []
        while len(bomb_list) < 8:
            b = (random.randrange(0, 8), random.randrange(0, 8))
            if b not in bomb_list:
                bomb_list.append(b)
        self.bombs = bomb_list
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
                if (r, c) in self.flags:
                    ret_board[r][c] = "F"
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
        if (r, c) in self.flags:
            self.flags.remove((r, c))
        if self.board[r][c] == -1:
            self.status = "LOSE"
        else:
            self.uncovered_spaces -= 1
            if self.uncovered_spaces == 0:
                self.status = "WIN!"

    def flag(self, r, c):
        if self.uncovered[r][c]:
            return
        if (r, c) in self.flags:
            self.flags.remove((r, c))
        else:
            self.flags.append((r, c))

