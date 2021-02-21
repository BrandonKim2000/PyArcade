**Smell 1: Data Clumps**

The dictionary games contains many dictionaries that should all be made into their own object.
Lines 29 and 30 of mastermind.py

Before:
```
    self.games[MastermindGame.sessions] = {"guesses": [], "session_id": 0, "done": False}
    self.games[MastermindGame.sessions]["session_id"] = MastermindGame.sessions
```
Method: replace array with object

Instead of storing each game as a dictionary I made a Game class:
```
class Game():
    guesses = []
    session_id = 0
    done = False
    nums = ()

    def __init__(self, guesses, session_id):
        self.guesses = guesses
        self.session_id = session_id
```



**Smell 2: Duplicate Code**

The code that checks for basic pieces of the input dictionary was repeated multiple times throughout proxy.py. Made it
into one function that could be called by each proxy function.

Method: Extract Method

Before: this appeared 4 times throughout the code

```
        if isinstance(request, dict):
            if "session_id" in request.keys():
                if isinstance(request["session_id"], int):
                    if request["session_id"] in self.game_instance.games.keys():
                        #perform action here
```

Made the extract method to perform this function and return a boolean.

```
    def valid_game(self, request: dict) -> bool:
        if isinstance(request, dict):
            if "session_id" in request.keys():
                if isinstance(request["session_id"], int):
                    if request["session_id"] in self.game_instance.games.keys():
                        return True
        return False
```

**Smell 3: Duplicate Code**

Realized that the returns of update_game() and read_game() were the same, so to save space I made update_game() call
and return read_game()

Can be seen in the new last line of update_game():
```
return MastermindGame.read_game(self, request)
```

**Smell 4: Divergent Change**

The setting of the random numbers for each game was being done in the create_game() function, so I moved it into the
game class so it would be easier to get more random numbers if needed.

Method: Extract Class

Randomization and setting of hidden code in the game class here:
```
    def __init__(self, guesses, session_id):
        self.guesses = guesses
        self.session_id = session_id
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
        self.nums = (i1, i2, i3, i4)
```