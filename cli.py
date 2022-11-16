# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import Game


if __name__ == '__main__':
    game_mode = None
    while game_mode not in ['pvp', 'pve', 'eve']:
        game_mode = input('Choose game mode (pvp, pve, or eve): ')
        if game_mode not in ['pvp', 'pve', 'eve']:
            print('Invalid game mode. Please try again.')
    if game_mode == 'pvp' or game_mode == 'eve':
        start_first = True
    else:
        start_command = input('Do you want to start first? (y/n): ')
        while start_command not in ['y', 'n']:
            start_command = input('Invalid input. Please input "y" or "n": ')
        start_first = start_command == 'y'
    game = Game(game_mode=game_mode, start_first=start_first)
    game.start()
        
        
        
        