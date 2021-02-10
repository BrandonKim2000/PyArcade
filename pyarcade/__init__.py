from pyarcade.proxy import MastermindGameProxy
from pyarcade.mastermind import MastermindGame

def main():
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
        proxy.read_game({"session_id", session_id})
        guess = input("Enter your guess as four integers separated by spaces\n")
        guess = guess.split(" ")
        


if __name__ == "__main__":
    main()