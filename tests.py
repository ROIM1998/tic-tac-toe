import numpy as np
import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        
        board = [
            ['X', 'O', 'O'],
            [None, 'O', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')

    # TODO: Test all functions from logic.py!
    def test_empty_board(self):
        self.assertEqual(logic.make_empty_board().tolist(), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_check_winner(self):
        board = np.array([
            [0, 1, 0],
            [1, 1, 2],
            [2, 1, 1],
        ])
        player = 1
        self.assertTrue(logic.check_winner(board, player))
    
    def test_other_player(self):
        player = 'X'
        self.assertEqual(logic.other_player(player), 'O')
        
    def test_move(self):
        board = np.array([
            [0, 1, 0],
            [1, 0, 2],
            [2, 0, 1],
        ])
        player = 'X'
        position = [0, 0]
        self.assertTrue(logic.move(board, player, position))
        self.assertEqual(board.tolist(), [[2, 1, 0], [1, 0, 2], [2, 0, 1]])
        
    def test_board_to_str(self):
        board = np.array([
            [1, 2, 0],
            [0, 0, 2],
            [0, 0, 1],
        ])
        result_str = '    0   1   2  \na | O | X |   |\n---------------\nb |   |   | X |\n---------------\nc |   |   | O |\n'
        self.assertEqual(logic.board_to_str(board), result_str)

if __name__ == '__main__':
    unittest.main()