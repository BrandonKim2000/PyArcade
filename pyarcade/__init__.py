from pyarcade.proxy import MastermindGameProxy
from pyarcade.mastermind import MastermindGame
from pyarcade.minesweeper import MinesweeperGame

def mastermind():
    print("Welcome to Benny's arcade!")
    print("Press enter to start a new game of Mastermind")
    input()
    game = MastermindGame()
    proxy = MastermindGameProxy(game)
    d = {"game_id": 0}
    session = proxy.create_game(d)
    session_id = session["session_id"]
    game_in_session = True
    while (game_in_session):
        proxy.read_game({"session_id": session_id})
        guess = input("Enter your guess as four integers separated by spaces\n")
        guess = guess.split(" ")
        guess = tuple([int(i) for i in guess])
        res = proxy.update_game({"session_id": session_id, "guess": guess})
        print(res)
        if res["done"]:
            game_in_session = False

def minesweeper():
    print("Welcome to Benny's arcade!")
    print("Press enter to start a new game of Minesweeper")
    input()
    game = MinesweeperGame()
    d = {"game_id": 0}
    session = game.create_game(d)
    session_id = session["session_id"]
    game_in_session = True
    while (game_in_session):
        game.read_game({"session_id": session_id})
        guess = input("Enter your guess as four integers separated by spaces\n")
        guess = guess.split(" ")
        guess = tuple([int(i) for i in guess])
        res = game.update_game({"session_id": session_id, "guess": guess})
        board = res["board"]
        for r in range(len(board)):
            line = ""
            for c in range(len(board[0])):
                line += str(board[r][c]) + " "
            print(line)
        if res["status"]:
            game_in_session = False

if __name__ == "__main__":
    minesweeper()