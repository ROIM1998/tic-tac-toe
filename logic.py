# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import numpy as np

cond_to_chr = {0: ' ', 1: 'O', 2: 'X'}
chr_to_int = {'a': 0, 'b': 1, 'c': 2}
int_to_role = {1: 'O', 2: 'X'}
role_to_int = {'O': 1, 'X': 2}


def make_empty_board():
    return np.zeros([3,3])


def check_winner(board, player):
    checks = []
    checks += [all(board[0] == player), all(board[1] == player), all(board[2] == player)]
    checks += [all(board[:, 0] == player), all(board[:, 1] == player), all(board[:, 2] == player)]
    checks += [all(board.flatten()[0::4] == player), all(board.flatten()[2:7:2] == player)]
    return any(checks)


def check_draw(board):
    return all(board.flatten() != 0)


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    if check_winner(board, 1):
        return int_to_role[1]
    elif check_winner(board, 2):
        return int_to_role[2]
    else:
        return 0


def other_player(player):
    """Given the character for a player, returns the other player."""
    return "O" if player == "X" else "X" 


def move(board, player, position):
    if board[position[0]][position[1]] == 0:
        board[position[0]][position[1]] = role_to_int[player]
        return True
    else:
        print("The place has already been taken!")
        return False
    
    
def board_to_str(board):
    separator = '---------------\n'
    header = '    0   1   2  \n'
    row_index='a'
    row_template = '%s | %s | %s | %s |\n'
    row_strings = []
    for i in range(3):
        row_strings.append(row_template % (chr(ord(row_index)+i), cond_to_chr[board[i][0]], cond_to_chr[board[i][1]], cond_to_chr[board[i][2]]))
    return header + separator.join(row_strings)