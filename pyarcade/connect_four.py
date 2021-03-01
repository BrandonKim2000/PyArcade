from pyarcade.game_interface import GameInterface


class ConnectFourGame(GameInterface):
    """ A class representing a connect four game session
   Note:
       The connect four board will have 7 columns and 6 rows, and the player will
       choose a column to insert the piece into
   """

    def __init__(self):
        self.games = {}
        self.session_id_next = 1
        self.width = 7
        self.height = 6

    def create_game(self, request: dict) -> dict:
        """ Upon calling create_game, the Connect Four game should initialize the board

       Args:
           request: dictionary containing single key-value pair. The key is "game_id".

       Returns:
           reply: dictionary containing the session_id in the request
       """

        # '_' is used because the local variable is not used anywhere else, represent
        # each space in the multidimensional array
        board = []
        for row in range(self.height):
            board_row = []
            for column in range(self.width):
                board_row.append(' ')
            board.append(board_row)

        session_id_current = self.session_id_next
        self.session_id_next += 1
        self.games[session_id_current] = {"board": board, "player_to_play": 1, "done": False}

        return {"session_id": session_id_current}

    def read_game(self, request: dict) -> dict:
        """
       Args:
           request: dictionary containing single key-value pair. The key is "session_id". The value is a
           integer unique to all ongoing game sessions.

       Returns:
           reply: dictionary containing four keys.
           "board": The board at the time the session is called.
           "curr_player": The current player at the time the board is brought up.
           "done": True or False depending on whether the game is over.
           "session_id": session_id provided with the original request.
       """
        current_game = dict(self.games[request["session_id"]])  # dict() created a copy of self.games
        current_game["session_id"] = request["session_id"]
        return current_game

    def get_column(self, request, index):
        """
       Returns a column at the specified index.

       :param request: Holding the session_id to check the correct board
       :param index: Index at which column will be returned
       """
        current_game = dict(self.games[request["session_id"]])
        current_board = current_game["board"]

        return [col[index] for col in current_board]

    def get_row(self, request, index):
        """
       Returns a row at the specified index

       :param request: Holding the session_id to check the correct board
       :param index: Index at which column will be returned
       """
        current_game = dict(self.games[request["session_id"]])
        current_board = current_game["board"]

        return current_board[index]

    def get_diagonals(self, request):
        """
       Returns all the diagonals in the game
       """
        current_game = dict(self.games[request["session_id"]])
        current_board = current_game["board"]
        diagonals = []

        for idx in range(self.height + self.width - 1):
            diagonals.append([])
            for idx_2 in range(max(idx - self.height + 1, 0), min(idx + 1, self.height)):
                diagonals[idx].append(current_board[self.height - idx + idx_2 - 1][idx_2])

        for idx in range(self.height + self.width - 1):
            diagonals.append([])
            for idx_2 in range(max(idx - self.height + 1, 0), min(idx + 1, self.height)):
                diagonals[idx].append(current_board[idx - idx_2][idx_2])

        return diagonals

    def check_win(self, request):
        """
       Checks the board to see if either user has four in a row
       """
        four_in_a_row = [['X', 'X', 'X', 'X'], ['O', 'O', 'O', 'O']]

        # check the rows
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.get_row(request, row)[col:col + 4] in four_in_a_row:
                    return True

        # check the columns
        for col in range(self.width):
            for row in range(self.height - 3):
                if self.get_column(request, col)[row:row + 4] in four_in_a_row:
                    return True

        # Check diagonals
        for val in self.get_diagonals(request):
            for diagonal, _ in enumerate(val):
                if val[diagonal:diagonal + 4] in four_in_a_row:
                    return True

        return False

    def check_full_board(self, request):
        """
       Checks to see if the board is full, if so the game is done
       """
        current_game = dict(self.games[request["session_id"]])
        current_board = current_game["board"]

        for row in current_board:
            for elem in row:
                if elem == ' ':
                    return False
        return True

    def make_move(self, request: dict) -> dict:
        """
        Simplifying the update_game function, call to drop the piece in the correct column.
        """
        current_game = self.games[request["session_id"]]
        current_board = current_game["board"]

        column = request["column"]
        session_id = {"session_id": request["session_id"]}

        if ' ' not in self.get_column(session_id, column):
            return current_game
        height = self.height - 1
        while current_board[height][column] != ' ':
            height -= 1

        if current_game["player_to_play"] == 1:
            current_board[height][column] = 'X'
            current_game["player_to_play"] = 2
        elif current_game["player_to_play"] == 2:
            current_board[height][column] = 'O'
            current_game["player_to_play"] = 1

        return current_game

    def update_game(self, request: dict) -> dict:
        """
       Args:
           request: dictionary containing two key-value pairs. One key is "session_id". This value is an
           integer unique to all ongoing game sessions. The second key is "column". The value should be an integer
           between 0 and 6 (to signify columns 1-7)

       Returns:
           reply: dictionary containing four keys:
               "board": The current board after the move is made
               "player_to_play": The next player to make a move
               "done": True or False depending on whether the game is over
               "session_id": session_id provided with the original request
       """
        current_game = self.games[request["session_id"]]

        move = self.make_move(request)

        if self.check_win(request) is True or self.check_full_board(request) is True:
            current_game["done"] = True

        copy_game = dict(move)
        copy_game["session_id"] = request["session_id"]
        return copy_game

    def delete_game(self, request: dict) -> dict:
        """
       Args:
           request: dictionary containing single key-value pair. The key is "session_id". The value is an
           integer unique to all ongoing game sessions.

       Returns:
           reply: dictionary containing the session_id in the request
       """
        self.games.pop(request["session_id"])
        return request
    