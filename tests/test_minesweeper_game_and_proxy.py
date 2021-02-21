from pyarcade.minesweeper import MinesweeperGame
from pyarcade.proxy import MinesweeperGameProxy
import unittest


class MinesweeperTestCase(unittest.TestCase):


    def test_proxy_create_game_gives_unique_session_id(self):
        session_ids = []
        game = MinesweeperGame()
        proxy = MinesweeperGameProxy(game)
        for idx in range(100):
            session_ids.append(proxy.create_game({"game_id": 1})["session_id"])

        self.assertEqual(len(set(session_ids)), 100)

    def test_different_sessions_unique_boards(self):
        session_ids = []
        bombs = []
        game = MinesweeperGame()
        proxy = MinesweeperGameProxy(game)
        for idx in range(100):
            session_ids.append(proxy.create_game({"game_id": 1})["session_id"])
        for idx in session_ids:
            bombs.append(list(game.games[idx].bombs)[0])
        self.assertNotEqual(len(set(bombs)), 1)


    def test_delete_game(self):
        game = MinesweeperGame()
        proxy = MinesweeperGameProxy(game)
        session_id = proxy.create_game({"game_id": 1})["session_id"]
        proxy.update_game({"session_id": session_id, "guess": (1, 2)})
        self.assertTrue(session_id in game.games.keys())
        proxy.delete_game({"session_id": session_id})
        self.assertTrue(session_id not in game.games.keys())

    def test_incorrect_input_create_game(self):
        game = MinesweeperGame()
        proxy = MinesweeperGameProxy(game)
        ret = proxy.create_game({"game_id": 10})
        self.assertEqual(ret, {"session_id": 0})

    def test_incorrect_input_read_game(self):
        game = MinesweeperGame()
        proxy = MinesweeperGameProxy(game)
        ret = proxy.read_game({"game_id": -10})
        self.assertEqual(ret, {"session_id": 0})

    def test_incorrect_session_id_update_game(self):
        game = MinesweeperGame()
        proxy = MinesweeperGameProxy(game)
        session_id = proxy.create_game({"game_id": 1})["session_id"]
        ret = proxy.update_game({"session_id": -10, "guess": (1, 2)})
        self.assertEqual(ret, {"session_id": 0})

    def test_extraneous_guess_update_game(self):
        game = MinesweeperGame()
        proxy = MinesweeperGameProxy(game)
        session_id = proxy.create_game({"game_id": 1})["session_id"]
        ret = proxy.update_game({"session_id": session_id, "guess": (1, 2, 3, 4, 5)})
        self.assertEqual(ret, {"session_id": 0})

    def test_game_played_extraneous_input(self):
        game = MinesweeperGame()
        proxy = MinesweeperGameProxy(game)
        session_id = proxy.create_game({"game_id": 1, "extraneous input": "MONKEY"})["session_id"]
        guess = game.games[session_id].nums
        proxy.update_game({"session_id": session_id, "guess": guess, "more extra input": "DOG"})
        done = proxy.read_game({"session_id": session_id, "even more extra input": "DRAGON"})
        self.assertTrue(done)

    def test_incorrect_input_delete_game(self):
        game = MinesweeperGame()
        proxy = MinesweeperGameProxy(game)
        session_id = proxy.create_game({"game_id": 1})["session_id"]
        ret = proxy.delete_game({"session_id": -10})
        self.assertEqual({"session_id": 0}, ret)


    def test_flag_return(self):
        game = MinesweeperGame()
        proxy = MinesweeperGameProxy(game)
        session_id = proxy.create_game({"game_id": 1})["session_id"]
        proxy.update_game({"session_id": session_id, "guess": (4, 4, "flag")})
        ret = game.read_game({"session_id": session_id})["board"][4][4]
        self.assertEqual("F", ret)