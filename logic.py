# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import numpy as np

cond_to_chr = {0: ' ', 1: 'O', 2: 'X'}
chr_to_int = {'a': 0, 'b': 1, 'c': 2}
int_to_role = {1: 'O', 2: 'X'}
role_to_int = {'O': 1, 'X': 2, None: 0}

def make_empty_board():
    return np.zeros([3,3])


class Game:
    def __init__(self):
        self.board = make_empty_board()


    def check_winner(self, player):
        checks = []
        checks += [all(self.board[0] == player), all(self.board[1] == player), all(self.board[2] == player)]
        checks += [all(self.board[:, 0] == player), all(self.board[:, 1] == player), all(self.board[:, 2] == player)]
        checks += [all(self.board.flatten()[0::4] == player), all(self.board.flatten()[2:7:2] == player)]
        return any(checks)


    def check_draw(self):
        return all(self.board.flatten() != 0)


    def get_winner(self):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        if isinstance(self.board, list):
            self.board = np.array([[role_to_int[v] for v in l] for l in self.board])
        if self.check_winner(1):
            return int_to_role[1]
        elif self.check_winner(2):
            return int_to_role[2]
        else:
            return 0


    def other_player(self, player):
        """Given the character for a player, returns the other player."""
        return "O" if player == "X" else "X" 


    def move(self, player, position):
        if self.board[position[0]][position[1]] == 0:
            self.board[position[0]][position[1]] = role_to_int[player]
            return True
        else:
            print("The place has already been taken!")
            return False
        
        
    def __repr__(self):
        separator = '---------------\n'
        header = '    0   1   2  \n'
        row_index='a'
        row_template = '%s | %s | %s | %s |\n'
        row_strings = []
        for i in range(3):
            row_strings.append(row_template % (chr(ord(row_index)+i), cond_to_chr[self.board[i][0]], cond_to_chr[self.board[i][1]], cond_to_chr[self.board[i][2]]))
        return header + separator.join(row_strings)


class Bot:
    def __init__(self, mode):
        self.mode = mode
        
    def get_move(self, board):
        indices = np.where(board == 0)
        available = [(i, j) for i, j in zip(indices[0], indices[1])]