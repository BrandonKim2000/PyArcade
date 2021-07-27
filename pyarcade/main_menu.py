from pyarcade.proxy import *
from pyarcade.mastermind import MastermindGame
from pyarcade.minesweeper import MinesweeperGame
from pyarcade.connect_four import ConnectFourGame

mastermindGame = MastermindGame()
mmProxy = MastermindGameProxy(mastermindGame)
minesweeperGame = MinesweeperGame()
msProxy = MinesweeperGameProxy(minesweeperGame)
connectFourGame = ConnectFourGame()
cfProxy = ConnectFourGameProxy(connectFourGame)


def mastermind_menu(request: dict = {}):
    print("Welcome to the Mastermind Menu")

    while True:
        try:
            gs = request["gs"]
        except:
            gs = input("Press 1 to start a new game of Mastermind. Press 2 to load an existing game of Mastermind.\n"
                       "Press 3 to see the Mastermind rules. Press 4 to return to the arcade main menu.\n")
        if gs == "1":
            d = {"game_id": 0}
            session = mmProxy.create_game(d)
            session_id = session["session_id"]
            print(f"You have created a new game of Mastermind. The session_id is {session_id}")
            play_mastermind(session_id)
        elif gs == "2":
            print("The active sessions of Mastermind are:")
            games = mastermindGame.games.keys()
            print(games)
            session_id = input("Enter the session of Mastermind that you would like to resume")
            # Need to adjust for non-integer input.
            if int(session_id) in mastermindGame.games:
                print(f"Resuming game with session_id {session_id}")
                play_mastermind(int(session_id))
            else:
                print("Could not find a game with that session_id")
        elif gs == "3":
            print("Mastermind is quite simple. The computer will give think of four numbers and you have to guess what "
                  "they are. Every time you make a guess you will see your previous guesses and a number that "
                  "indicates how many of those guesses were in the pattern, yet you put them in the wrong spot (cows), "
                  "and how many numbers of your guess were in the correct spot (bulls). Use this feedback to adjust "
                  "your guess until you guess the number in all four spots.")
        elif gs == "4":
            break
        else:
            print("I'm sorry, I didn't catch that.")

    print("Returning to the arcade main menu")


def play_mastermind(session_id: int):
    game_in_session = True

    while game_in_session:
        mmProxy.read_game({"session_id": session_id})
        guess = input("Enter your guess as four integers separated by spaces\n")
        if guess == "quit":
            break
        guess = guess.split(" ")
        try:
            guess = tuple([int(i) for i in guess])
        except (ValueError, TypeError):
            print("Guess not entered correctly")
            continue
        res = mmProxy.update_game({"session_id": session_id, "guess": guess})
        print(res)
        if res["done"]:
            game_in_session = False
            mmProxy.delete_game({"session_id": session_id})

    print("Returning to the Mastermind menu")


def minesweeper_menu(request: dict = {}):
    print("Welcome to the Minesweeper Menu")

    while True:

        try:
            gs = request["gs"]
        except:
            gs = input("Press 1 to start a new game of Minesweeper. Press 2 to load an existing game of Minesweeper.\n"
                       "Press 3 to see the Minesweeper rules. Press 4 to return to the arcade menu.\n")
        if gs == "1":
            d = {"game_id": 1}
            session = msProxy.create_game(d)
            session_id = session["session_id"]
            print(f"You have created a new game of Minesweeper. The session_id is {session_id}")
            play_minesweeper(session_id)
        elif gs == "2":
            print("The active sessions of Minesweeper are:")
            games = minesweeperGame.games.keys()
            print(games)
            session_id = input("Enter the session of Minesweeper that you would like to resume")
            # Need to adjust for non-integer input.
            if int(session_id) in minesweeperGame.games:
                print(f"Resuming game with session_id {session_id}")
                play_minesweeper(int(session_id))
            else:
                print("Could not find a game with that session_id")
        elif gs == "3":
            print("Minesweeper is quite simple. There are 64 mystery boxes that contain either a bomb or a number. "
                  "Your job is to open each box that doesn't contain a bomb, without clicking on any bombs. "
                  "When you click a square it reveals the number behind that square. That number is how many adjacent "
                  "boxes contain a bomb. Use these as clues to avoid the bombs and click thorugh all the free spots!")
        elif gs == "4":
            break
        else:
            print("I'm sorry, I didn't catch that.")

    print("Returning to the arcade menu")


def play_minesweeper(session_id: int):
    print(f"You are playing Minesweeper session #{session_id}. To return to Minesweeper game menu enter \"quit\".")

    game_in_session = True
    while game_in_session:
        msProxy.read_game({"session_id": session_id})
        print("Example input: X * Y (X up to 7, Y up to 7)")
        guess = input("Enter your guess as 2 integers separated by spaces (similar to an array)\n")
        if guess == "quit":
            break
        guess = guess.split(" ")
        try:
            if len(guess) == 2:
                guess = tuple([int(i) for i in guess])
            else:
                guess = tuple(int(guess[0]), int(guess[1]), guess[2])
        except (ValueError, TypeError):
            print("Guess not entered correctly")
            continue
        res = msProxy.update_game({"session_id": session_id, "guess": guess})
        board = res["board"]
        for r in range(len(board)):
            line = ""
            for c in range(len(board[0])):
                line += str(board[r][c]) + " "
            print(line)
        if res["status"]:
            game_in_session = False
            msProxy.delete_game({"session_id": session_id})

    print("Returning to Minesweeper menu.")


def connect_four_menu(request: dict = {}):
    print("Welcome to the Connect Four Menu")
    while True:

        try:
            gs = request["gs"]
        except:
            gs = input("Press 1 to start a new game of Connect Four. Press 2 to load an existing game of Connect "
                       "Four.\n"
                       "Press 3 to see the Connect Four rules. Press 4 to return to the arcade main menu.\n")
        if gs == "1":
            d = {"game_id": 2}
            session = cfProxy.create_game(d)
            session_id = session["session_id"]
            print(f"You have created a new game of Connect Four. The session_id is {session_id}")
            play_connect_four(session_id)
        elif gs == "2":
            print("The active sessions of Connect Four are:")
            games = connectFourGame.games.keys()
            if len(games) == 0:
                print("There are no active sessions!\n")
            print(games)
            session_id = input("Enter the session of Connect Four that you would like to resume")
            # Accounting for non-integer input.
            if int(session_id) in connectFourGame.games:
                print(f"Resuming game with session_id {session_id}")
                play_connect_four(int(session_id))
            else:
                print("Could not find a game with that session_id\n")
        elif gs == "3":
            # List the rules/instructions
            print("In Connect Four, the goal is to create a line of four of your color. This can be done by creating \n"
                  "a line in a horizontal, vertical, or diagonal direction. In this game of Connect Four, it will \n"
                  "be a two-player game in which each user takes turns making their moves until the game is finished.\n")
            print("Returning to the Connect Four game menu\n")
        elif gs == "4":
            break
        else:
            print("I'm sorry, I didn't catch that.")


def play_connect_four(session_id: int):
    game_in_session = True

    while game_in_session:
        cfProxy.read_game({"session_id": session_id})
        column = input("Enter the column (from 0-6) that you would like to update, or 'quit' if you would like to "
                       "exit.\n")
        if column == "quit":
            break
        int_column = int(column)
        res = cfProxy.update_game({"session_id": session_id, "column": int_column})

        for row in res["board"]:
            print('|' + '|'.join(row) + '|')

        res.pop("board")
        print(res)
        if res["done"]:
            print("Player " + str(res["player_to_play"]) + ", you have lost!\n")
            game_in_session = False
            cfProxy.delete_game({"session_id": session_id})

    print("Returning to the Connect Four Menu\n")
    connect_four_menu()


def main_menu(request: dict = {}):
    print("Welcome to Benny and Brando's arcade!")
    print("This arcade currently contains 3 games. You can switch between the games and create multiple sessions of"
          " each one.")
    while True:
        try:
            gs = request["gs"]
        except:
            gs = input("Press 0 to play Mastermind, 1 to play Minesweeper, or 2 to play Connect Four.")
        if gs == "0":
            mastermind_menu()
        elif gs == "1":
            minesweeper_menu()
        elif gs == "2":
            connect_four_menu()
        else:
            print("I'm sorry, I didn't catch that.")


if __name__ == "__main__":
    main_menu()
