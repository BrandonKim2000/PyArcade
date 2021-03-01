from pyarcade.proxy import *
from pyarcade.mastermind import MastermindGame
from pyarcade.minesweeper import MinesweeperGame

mastermindGame = MastermindGame()
mmProxy = MastermindGameProxy(mastermindGame)
minesweeperGame = MinesweeperGame()
msProxy = MinesweeperGameProxy(minesweeperGame)

def mastermind():
    print("Welcome to Benny's arcade!")
    print("Press enter to start a new game of Mastermind")
    input()
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

def minesweeperMenu():
    print("Welcome to the Minesweeper Menu")

    while (True):
        gs = input("Press 1 to start a new game of Minesweeper. Press 2 to load an existing game of Minesweeper. "
                   "Press 3 to see the Minesweeper rules. Press 4 to return to the arcade main menu.")
        if gs == "1":
            d = {"game_id": 1}
            session = msProxy.create_game(d)
            session_id = session["session_id"]
            print(f"You have created a new game of Minesweeper. The session_id is {session_id}")
            playMinesweeper(session_id)
        elif gs == "2":
            print("The active sessions of Minesweeper are:")
            games = minesweeperGame.games.keys()
            print(games)
            session_id = input("Enter the session of Minesweeper that you would like to resume")
            #Need to adjust for non-integer input.
            if int(session_id) in minesweeperGame.games:
                print(f"Resuming game with session_id {session_id}")
                playMinesweeper(int(session_id))
            else:
                print("Could not find a game with that session_id")
        elif gs == "3":
            #List the rules/instructions
            pass
        elif gs == "4":
            break
        else:
            print("I'm sorry, I didn't catch that.")

    print("Returning to the arcade main menu")

def playMinesweeper(session_id: int):
    print(f"You are playing Minesweeper session #{session_id}. To return to Minesweeper game menu enter \"quit\".")

    game_in_session = True
    while (game_in_session):
        msProxy.read_game({"session_id": session_id})
        guess = input("Enter your guess as four integers separated by spaces\n")
        if guess == "quit":
            break
        guess = guess.split(" ")
        guess = tuple([int(i) for i in guess])
        res = msProxy.update_game({"session_id": session_id, "guess": guess})
        board = res["board"]
        for r in range(len(board)):
            line = ""
            for c in range(len(board[0])):
                line += str(board[r][c]) + " "
            print(line)
        if res["status"]:
            game_in_session = False
            #Make it call delete_game

    print("Returning to Minesweeper main menu.")


if __name__ == "__main__":
    print("Welcome to Benny and Brando's arcade!")
    print("This arcade currently contains 3 games. You can switch between the games and create multiple sessions of"
          "each one.")
    while (True):
        gs = input("Enter 0 to play Mastermind, 1 to play Minesweeper, or 2 to play Connect Four")
        if gs == "0":
            #go to Mastermind menus
            pass
        elif gs == "1":
            minesweeperMenu()
        elif gs == "2":
            #go to Connect 4 menus
            pass
        else:
            print("I'm sorry, I didn't catch that.")