# PyArcade -- The Back End Test Suite

# Software Requirements
All of the software requirements are written in detail in comments directly under the function signatures for two files
```proxy.py``` and ```mastermind.py```. You may, and probably will need to, create more functions for both of the 
classes defined in these files.

# Testing Requirements
Testing is a huge part of this assignment. The code implementations defined in the comments should not be 
terribly difficult. You must create a test suite that *efficiently* and *exhaustively* tests sensible inputs and 
outputs for the provided specifications. The concept of equivalence partitions is important here. When creating unit 
tests, you should not be creating an abundance of tests for which the input exercises the function in a similar way. 
Rather, you should choose tests that represent unique requirements for a function.

The rubric states:

1. Has higher than 90% code coverage using [pytest-cov](https://pypi.org/project/pytest-cov/)
2. Has test names which meaningfully describe the test.
3. Has tests which are atomic (definition of a unit test). 
4. Has tests which test *features* (integration tests) as well as simple functionality (unit tests). 

What you SHOULD consider testing:
1. Correctly typed inputs that have extra data. (behavior should be unaffected)
2. Correctly typed but erroneous inputs.
3. An entire sequence of inputs that results in winning the game in several ways. This is an integration test.

What is NOT required to be tested:
1. Input *types* being correct. We will consider type-hints as sufficient.

## Rubric
As always, mind the rubric. **You are not being graded solely on whether it works.** You must incorporate
good practices to keep code complexity to a minimum and also use git correctly.


 