## Assignment 5 Approximate Work Distribution
### 1. Benny Beinish: 50%
#### 1.  Finished mastermind, minesweeper, main_menu implementation
#### 2. Added flask implementation
#### 3. Added tests for main menu and minesweper menu

### 2. Brandon Kim: 50%
#### 1. Implemented connect_four game to merge
#### 2. Added tests for connect_four, proxy, connect four menu, and mastermind menu
#### 3. Applied use of singleton pattern

# Implementing a Design Pattern

##1. Design Pattern we chose: Singleton

##2. How and Why we Chose it
### The Singleton design pattern ensures that only one instance of an object exists globally. It's purpose is to control access to shared and/or sensitive resources, in our case being the games and specific sessions.
### We chose this design pattern because we wanted to make sure that only one specific game and one session associated with that game can be played at a single time. Without the limitation to a single instance, the data could become messy and create a confusing platform for the user when experiencing our program.
### We implemented Singleton in each of our specific games (mastermind, minesweeper, connect four), as well as our main menu. This allowed our code to become much more maintainable, as we could easily find bugs or errors in our code when testing due to the fact that only one game or one menu option could be inputted or played at one time.

##3. Where it's implemented
### These classes are examples of Singleton:
### pyarcade/mastermind.py

### pyacade/minesweeper.py

### pyarcade/connect_four.py

### pyarcade/main_menu.py

### The only time these classes are instantiated in all the gameplay is in lines 6-11 of the main menu:

```
mastermindGame = MastermindGame()
mmProxy = MastermindGameProxy(mastermindGame)
minesweeperGame = MinesweeperGame()
msProxy = MinesweeperGameProxy(minesweeperGame)
connectFourGame = ConnectFourGame()
cfProxy = ConnectFourGameProxy(connectFourGame)
```

### By having the inner class 'game', the classes 'MastermindGame', 'connectFourGame', and 'MinesweeperGame' are able to have multiple sessions, while only being instantiated once.

### mastermind.py: lines 102-133
### minesweeper.py: lines 51-120
### connect_four.py: lines 

## 4. Code Snippets:
### THe following code snippet is the create_game function. This allows us to only create one minesweeper game at a time.
```
   def create_game(self, request: dict) -> dict:
        MinesweeperGame.sessions += 1

        self.games[MinesweeperGame.sessions] = Game(MinesweeperGame.sessions, [], set())
        return {"session_id": self.games[MinesweeperGame.sessions].get_session_id()}
```

### The following code snippet is the minesweeper game class:
```
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
```