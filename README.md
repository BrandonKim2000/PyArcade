Smell 1: Data Clumps
The dictionary games contains many dictionaries that should all be made into their own object.
Lines 29 and 30
Method: replace array with object

Smell 2:
Made it so the return of update_game would return read_game()
Line 99

Smell 3: Duplicate code in proxy.py
The code that checks for basic pieces of the input dictionary was repeated multiple times. Made it into one method.
Method: Extract Method

Smell 4:
Moved code for generating randoms from the create_game to the initialization of game object