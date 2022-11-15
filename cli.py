# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import Game, chr_to_int


if __name__ == '__main__':
    winner = None
    now = 'O'
    game = Game()
    while winner == None:
        # TODO: Show the board to the user.
        print(game)
        # TODO: Input a move from the player.
        print("TODO: take a turn!")
        position = input("Player %s please input the position you want to take, for example, \"a 0\"" % now)
        row, col = position.split()
        if row not in ['a', 'b', 'c']:
            print("Wrong input! The index of rows should be 'a', 'b', or 'c'")
            continue
        if col not in ['0', '1', '2']:
            print("Wrong input! The index of columns should be '0', '1', or '2'")
            continue
        # TODO: Update the board.
        success = game.move(now, (chr_to_int[row], int(col)))
        # TODO: Update who's turn it is.
        if success:
            now = game.other_player(now)
        checked = game.get_winner()
        if checked != 0:
            winner = checked
            print(game)
            print("Player %s has won!!" % checked)
        if game.check_draw():
            print(game)
            print("Draw!")
            break
        
        
        
        