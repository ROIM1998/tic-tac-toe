# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import Game
import argparse

parser = argparse.ArgumentParser(description='Play Tic-Tac-Toe.')
parser.add_argument('--player1', default='none', choices=['human', 'random', 'minimax'])
parser.add_argument('--player2', default='none', choices=['human', 'random', 'minimax'])
args = parser.parse_args()
playertype2abbreviation = {
    'human': 'p',
    'random': 'r',
    'minimax': 'e',
}


if __name__ == '__main__':
    if args.player1 == 'none' or args.player2 == 'none':
        args = None
        game_mode = None
        while game_mode not in ['pvp', 'pve', 'eve', 'evr']:
            game_mode = input('Choose game mode (pvp, pve, eve, or evr): ')
            if game_mode not in ['pvp', 'pve', 'eve', 'evr']:
                print('Invalid game mode. Please try again.')
        if game_mode == 'pvp' or game_mode == 'eve' or game_mode == 'evr':
            start_first = True
        else:
            start_command = input('Do you want to start first? (y/n): ')
            while start_command not in ['y', 'n']:
                start_command = input('Invalid input. Please input "y" or "n": ')
            start_first = start_command == 'y'
    else:
        # When using args to specify players, the player1 always starts first.
        game_mode = playertype2abbreviation[args.player1] + 'v' + playertype2abbreviation[args.player2]
        start_first = True
    game = Game(game_mode=game_mode, start_first=start_first, args=args)
    game.start()
        
        
        
        