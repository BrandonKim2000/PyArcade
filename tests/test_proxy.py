from pyarcade.mastermind import MastermindGame
from pyarcade.proxy import MastermindGameProxy
import unittest


class MastermindTestCase(unittest.TestCase):
    def test_proxy_create_game_gives_unique_session_id(self):
        session_ids = []
        game = MastermindGame()
        proxy = MastermindGameProxy(game)
        for idx in range(100):
            session_ids.append(proxy.create_game({"game_id": 0})["session_id"])

        self.assertEqual(len(set(session_ids)), 100)

    def test_different_sessions_unique_numbers(self):
        session_ids = []
        bulls_and_cows = []
        game = MastermindGame()
        proxy = MastermindGameProxy(game)
        for idx in range(100):
            session_ids.append(proxy.create_game({"game_id": 0})["session_id"])
        for idx in session_ids:
            proxy.update_game({"session_id": idx, "guess": (1, 2, 3, 4)})
            bulls_and_cows.append(proxy.read_game({"session_id": idx})["guesses"][0][1])
        self.assertNotEqual(len(set(bulls_and_cows)), 1)

    def test_update_and_read_game(self):
        game = MastermindGame()
        proxy = MastermindGameProxy(game)
        session_id = proxy.create_game({"game_id": 0})["session_id"]
        proxy.update_game({"session_id": session_id, "guess": (1, 2, 3, 4)})
        proxy.update_game({"session_id": session_id, "guess": (4, 3, 2, 1)})
        guess1 = proxy.read_game({"session_id": session_id})["guesses"][0][0]
        guess2 = proxy.read_game({"session_id": session_id})["guesses"][1][0]
        self.assertEqual(guess1, (1, 2, 3, 4))
        self.assertEqual(guess2, (4, 3, 2, 1))

    def test_delete_game(self):
        game = MastermindGame()
        proxy = MastermindGameProxy(game)
        session_id = proxy.create_game({"game_id": 0})["session_id"]
        proxy.update_game({"session_id": session_id, "guess": (1, 2, 3, 4)})
        proxy.delete_game({"session_id": session_id})
        #self.assertTrue(session_id not in game.games.keys())

    def test_play_win_game(self):
        game = MastermindGame()
        proxy = MastermindGameProxy(game)
        session_id = proxy.create_game({"game_id": 0})["session_id"]
        sequence = game.games[session_id]["nums"]
        proxy.update_game({"session_id": session_id, "guess": sequence})
        done = proxy.read_game({"session_id": session_id})["done"]
        self.assertTrue(done)
