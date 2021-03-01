from pyarcade.proxy import ConnectFourGameProxy
from pyarcade.connect_four import ConnectFourGame
import unittest

class ConnectFourTestCase(unittest.TestCase):
    """
    create_game tests
    """

    def test_proxy_create_game_is_wrong_type(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)

        reply = proxy.create_game({"game_id": "string"})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.create_game({"game_id": 1.0})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.create_game({"game_id": {}})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.create_game({"game_id": []})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.create_game({"game_id": False})
        self.assertEqual(reply["session_id"], 0)

    def test_proxy_create_game_multiple_keys(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)

        reply = proxy.create_game({"game_id": 2, "random_key": ""})
        self.assertEqual(reply["session_id"], 1)

        reply = proxy.create_game({"game_id": 2, "random_key": "", "another_key": 3})
        self.assertEqual(reply["session_id"], 2)

    def test_proxy_create_game_game_id_wrong_name(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)

        reply = proxy.create_game({"game": 2})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.create_game({"game_ids": 2})
        self.assertEqual(reply["session_id"], 0)

    def test_proxy_create_game_correct_game_id(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)

        reply = proxy.create_game({"game_id": 2})
        self.assertFalse(reply["session_id"] == 0)

    """
    read_game tests
    """

    def test_proxy_read_game_is_wrong_type(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        reply = proxy.read_game({"session_id": "string"})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.read_game({"session_id": 1.0})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.read_game({"session_id": {}})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.read_game({"session_id": []})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.read_game({"session_id": False})
        self.assertEqual(reply["session_id"], 0)

    def test_proxy_read_game_extra_keys(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        reply = proxy.read_game({"session_id": 1, "extra_key": ""})
        self.assertEqual(reply, {"board": [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                           [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                           [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']],
                                 "player_to_play": 1, "done": False, "session_id": 1})

    def test_proxy_read_game_correct_session_id(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        reply = proxy.read_game({"session_id": 1})
        self.assertEqual(reply, {"board": [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                           [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                           [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']],
                                 "player_to_play": 1, "done": False, "session_id": 1})

    """
    update_game tests
    """

    def test_proxy_update_game_session_id_is_wrong_type(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        reply = proxy.update_game({"session_id": "string", "column": 1})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.update_game({"session_id": 1.0, "column": 1})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.update_game({"session_id": {}, "column": 1})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.update_game({"session_id": [], "column": 1})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.update_game({"session_id": False, "column": 1})
        self.assertEqual(reply["session_id"], 0)

    def test_proxy_update_game_column_is_wrong_type(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        reply = proxy.update_game({"session_id": 1, "guess": 1.0})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.update_game({"session_id": 1, "guess": {}})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.update_game({"session_id": 1, "guess": []})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.update_game({"session_id": 1, "guess": True})
        self.assertEqual(reply["session_id"], 0)

    def test_proxy_update_game_column_invalid(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        reply = proxy.update_game({"session_id": 1, "guess": -1})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.update_game({"session_id": 1, "guess": 7})
        self.assertEqual(reply["session_id"], 0)

    def test_proxy_update_game_extra_keys(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        reply = proxy.update_game({"session_id": 1, "column": 1, "extra_key": ""})
        reply.pop("board")
        reply.pop("done")
        reply.pop("player_to_play")
        self.assertEqual(reply, {"session_id": 1})

    def test_proxy_update_game_correct_entry(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        reply = proxy.update_game({"session_id": 1, "column": 1})
        reply.pop("board")
        reply.pop("done")
        reply.pop("player_to_play")
        self.assertEqual(reply, {"session_id": 1})

    def test_proxy_update_game_integration_test_pass_row(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        copy = game.games[1]
        copy["board"] = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['O', 'O', 'O', ' ', ' ', ' ', ' '], ['X', 'X', 'X', ' ', ' ', ' ', ' ']]
        reply = proxy.update_game({"session_id": 1, "column": 3})
        self.assertEqual(reply, {"board": [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                           [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                           ['O', 'O', 'O', ' ', ' ', ' ', ' '], ['X', 'X', 'X', 'X', ' ', ' ', ' ']],
                                 "player_to_play": 2, "done": True, "session_id": 1})

    def test_proxy_update_game_integration_test_pass_column(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        copy = game.games[1]
        copy["board"] = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['X', 'O', ' ', ' ', ' ', ' ', ' '],
                         ['X', 'O', ' ', ' ', ' ', ' ', ' '], ['X', 'O', ' ', ' ', ' ', ' ', ' ']]
        reply = proxy.update_game({"session_id": 1, "column": 0})
        self.assertEqual(reply, {"board": [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                           ['X', ' ', ' ', ' ', ' ', ' ', ' '], ['X', 'O', ' ', ' ', ' ', ' ', ' '],
                                           ['X', 'O', ' ', ' ', ' ', ' ', ' '], ['X', 'O', ' ', ' ', ' ', ' ', ' ']],
                                 "player_to_play": 2, "done": True, "session_id": 1})

    def test_proxy_update_game_integration_test_pass_diagonal(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        copy = game.games[1]
        copy["board"] = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'X', 'O', ' ', ' ', ' '],
                         [' ', 'X', 'O', 'X', ' ', ' ', ' '], ['X', 'O', 'O', 'X', 'O', ' ', ' ']]
        reply = proxy.update_game({"session_id": 1, "column": 3})
        self.assertEqual(reply, {"board": [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                           [' ', ' ', ' ', 'X', ' ', ' ', ' '], [' ', ' ', 'X', 'O', ' ', ' ', ' '],
                                           [' ', 'X', 'O', 'X', ' ', ' ', ' '], ['X', 'O', 'O', 'X', 'O', ' ', ' ']],
                                 "player_to_play": 2, "done": True, "session_id": 1})

    def test_proxy_update_game_integration_test_fail(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        copy = game.games[1]
        copy["board"] = [[' ', 'X', 'O', 'O', 'O', 'X', 'O'], ['X', 'O', 'X', 'X', 'X', 'O', 'X'],
                         ['O', 'X', 'O', 'O', 'O', 'X', 'O'], ['O', 'X', 'O', 'X', 'X', 'O', 'X'],
                         ['X', 'O', 'X', 'O', 'O', 'X', 'X'], ['X', 'O', 'X', 'X', 'X', 'O', 'O']]
        copy["player_to_play"] = 2
        reply = proxy.update_game({"session_id": 1, "column": 0})
        self.assertEqual(reply, {"board": [['O', 'X', 'O', 'O', 'O', 'X', 'O'], ['X', 'O', 'X', 'X', 'X', 'O', 'X'],
                         ['O', 'X', 'O', 'O', 'O', 'X', 'O'], ['O', 'X', 'O', 'X', 'X', 'O', 'X'],
                         ['X', 'O', 'X', 'O', 'O', 'X', 'X'], ['X', 'O', 'X', 'X', 'X', 'O', 'O']],
                                 "player_to_play": 1, "done": True, "session_id": 1})

    def test_proxy_update_game_wrong_parameter_name(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        reply = proxy.update_game({"session": 1, "column": 1})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.update_game({"session_id": 1, "columns": 1})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.update_game({"sessions": 1, "column_id": 1})
        self.assertEqual(reply["session_id"], 0)

    """
    delete_game tests
    """
    def test_proxy_delete_game_session_id_is_wrong_type(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        reply = proxy.delete_game({"session_id": "string"})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.delete_game({"session_id": 1.0})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.delete_game({"session_id": {}})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.delete_game({"session_id": []})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.delete_game({"session_id": False})
        self.assertEqual(reply["session_id"], 0)

    def test_proxy_delete_game_proper_delete(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        proxy.delete_game({"session_id": 1})
        self.assertEqual(len(game.games), 0)

    def test_proxy_delete_game_extra_keys(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        proxy.delete_game({"session_id": 1, "extra_key": ""})
        self.assertEqual(len(game.games), 0)

    def test_proxy_delete_game_session_id_wrong_name(self):
        game = ConnectFourGame()
        proxy = ConnectFourGameProxy(game_instance=game)
        proxy.create_game({"game_id": 2})

        reply = proxy.delete_game({"session": 1})
        self.assertEqual(reply["session_id"], 0)

        reply = proxy.delete_game({"session_ids": 1})
        self.assertEqual(reply["session_id"], 0)

    # create_game function tests
    def test_create_game_proper_start(self):
        game = ConnectFourGame()
        self.assertEqual(game.create_game({"game_id": 2}), {"session_id": 1})

    # read_game function tests
    def test_read_game_base_read(self):
        game = ConnectFourGame()
        game.create_game({"game_id": 2})
        request = {"session_id": 1}

        self.assertEqual(game.read_game(request),
                         {"board": [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']],
                          "player_to_play": 1, "done": False, "session_id": 1})

    def test_read_game_second_session(self):
        game = ConnectFourGame()
        game.create_game({"game_id": 2})
        game.create_game({"game_id": 2})
        request = {"session_id": 2}

        self.assertEqual(game.read_game(request),
                         {"board": [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']],
                          "player_to_play": 1, "done": False, "session_id": 2})

    # update_game functions
    def test_update_game_adding_piece(self):
        game = ConnectFourGame()
        game.create_game({"game_id": 2})
        request = {"session_id": 1, "column": 0}

        self.assertEqual(game.update_game(request),
                         {"board": [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['X', ' ', ' ', ' ', ' ', ' ', ' ']],
                          "player_to_play": 2, "done": False, "session_id": 1})

    def test_update_game_adding_second_piece(self):
        game = ConnectFourGame()
        game.create_game({"game_id": 2})
        game.update_game({"session_id": 1, "column": 0})

        self.assertEqual(game.update_game({"session_id": 1, "column": 0}),
                         {"board": [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    ['O', ' ', ' ', ' ', ' ', ' ', ' '], ['X', ' ', ' ', ' ', ' ', ' ', ' ']],
                          "player_to_play": 1, "done": False, "session_id": 1})

    # delete_game function tests
    def test_delete_game_base(self):
        game = ConnectFourGame()
        game.create_game({"game_id": 2})
        request = {"session_id": 1}
        game.delete_game(request)

        self.assertEqual(len(game.games), 0)

    def test_delete_game_multiple_ids(self):
        game = ConnectFourGame()
        game.create_game({"game_id": 2})
        game.create_game({"game_id": 2})
        request = {"session_id": 1}
        game.delete_game(request)

        self.assertEqual(len(game.games), 1)