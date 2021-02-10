from pyarcade.mastermind import MastermindGame
import unittest


class MastermindTestCase(unittest.TestCase):
    def test_create_game_gives_unique_sequence(self):
        session_ids = []
        game = MastermindGame()
        for idx in range(100):
            session_ids.append(game.create_game({"game_id": 0})["session_id"])

        self.assertEqual(len(set(session_ids)), 100)

    def test_create_game_gives_unique_sequence(self):
        session_ids = []
        game = MastermindGame()
        for idx in range(100):
            session_ids.append(game.create_game({"game_id": 0})["session_id"])

        self.assertEqual(len(set(session_ids)), 100)

