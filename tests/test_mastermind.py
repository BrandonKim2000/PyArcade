from pyarcade.mastermind import MastermindGame
import unittest


class MastermindTestCase(unittest.TestCase):
    def test_create_game_gives_unique_session_id(self):
        session_ids = []
        game = MastermindGame()
        for idx in range(100):
            session_ids.append(game.create_game({"game_id": 0})["session_id"])

        self.assertEqual(len(set(session_ids)), 100)

    def test_different_sessions_unique_numbers(self):
        session_ids = []
        bulls_and_cows = []
        game = MastermindGame()
        for idx in range(100):
            session_ids.append(game.create_game({"game_id": 0})["session_id"])
        for idx in session_ids:
            game.update_game({"session_id": idx, "guess": (1, 2, 3, 4)})
            bulls_and_cows.append(game.read_game({"session_id": idx})["guesses"][0][1])
        self.assertNotEqual(len(set(bulls_and_cows)), 1)

    def test_update_and_read_game(self):
        game = MastermindGame()
        session_id = game.create_game({"game_id": 0})["session_id"]
        game.update_game({"session_id": session_id, "guess": (1, 2, 3, 4)})
        game.update_game({"session_id": session_id, "guess": (4, 3, 2, 1)})
        guess1 = game.read_game({"session_id": session_id})["guesses"][0][0]
        guess2 = game.read_game({"session_id": session_id})["guesses"][1][0]
        self.assertEqual(guess1, (1, 2, 3, 4))
        self.assertEqual(guess2, (4, 3, 2, 1))

    def test_delete_game(self):
        game = MastermindGame()
        session_id = game.create_game({"game_id": 0})["session_id"]
        game.update_game({"session_id": session_id, "guess": (1, 2, 3, 4)})
        self.assertTrue(session_id in game.games.keys())
        game.delete_game({"session_id": session_id})
        self.assertTrue(session_id not in game.games.keys())

    def test_play_win_game(self):
        game = MastermindGame()
        session_id = game.create_game({"game_id": 0})["session_id"]
        sequence = game.games[session_id]["nums"]
        game.update_game({"session_id": session_id, "guess": sequence})
        done = game.read_game({"session_id": session_id})["done"]
        self.assertTrue(done)





