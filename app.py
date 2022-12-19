from flask import Flask
from flask import render_template, jsonify
from flask import request
from logic import Game
import time
import pandas as pd

app = Flask(__name__)
game = None
last_time = None
rounds = 0

@app.route("/tic-tac-toe")
def index():
    return render_template('index.html')

@app.route("/tic-tac-toe/play")
def play():
    print("Initializing game...")
    global game, last_time
    last_time = time.time()
    if request.args.get('playmode') == 'pvp':
        game = Game(game_mode=request.args.get('playmode'), start_first=True, player_names=[request.args.get('player1'), request.args.get('player2')])
        return render_template('play.html', player1=request.args.get('player1'), player2=request.args.get('player2'))
    elif request.args.get('playmode') == 'pve':
        game = Game(game_mode=request.args.get('playmode'), bot_type=request.args.get('botmode2'), start_first=True, player_names=[request.args.get('player1')])
        return render_template('play.html', player1=request.args.get('player1'), player2=request.args.get('botmode2') + 'Bot')
    elif request.args.get('playmode') == 'eve':
        return render_template('play.html', player1=request.args.get('botmode1') + 'Bot', player2=request.args.get('botmode2') + 'Bot')
    
@app.route("/tic-tac-toe/move", methods=['POST'])
def get_move():
    print(request.json)
    global last_time
    data = request.json
    row, col = data['row'], data['col']
    success = game.move(game.player_now, (row, col))
    if success:
        game.player_now.num_moves += 1
        game.player_now.time_takes += time.time() - last_time
        last_time = time.time()
        game.player_now = game.other_player(game.player_now)
    else:
        return jsonify({
            'success': success,
            'gameover': False,
            'winner': None,
        })
    global rounds
    rounds += 1
    checked = game.get_winner(game.board)
    winner = None
    if checked != 0:
        winner = checked
        game.add_savegame(game.id_to_name[checked], rounds, False)
        game.save_game("savegame.csv")
        game.update_statistics(winner)
        return jsonify({
            'success': success,
            'gameover': True,
            'winner': game.id_to_name[winner],
        })
    elif game.check_draw(game.board):
        game.add_savegame(None, rounds, True)
        game.save_game("savegame.csv")
        game.update_statistics(winner)
        return jsonify({
            'success': success,
            'gameover': True,
            'winner': None,
        })
    else:
        if game.game_mode == 'pve':
            rounds += 1
            row, col = game.player_now.get_move(game)
            success = game.move(game.player_now, (row, col))
            if success:
                game.player_now.num_moves += 1
                game.player_now.time_takes += time.time() - last_time
                last_time = time.time()
                game.player_now = game.other_player(game.player_now)
            checked = game.get_winner(game.board)
            if checked != 0:
                winner = checked
                game.add_savegame(game.id_to_name[checked], rounds, False)
                game.save_game("savegame.csv")
                game.update_statistics(winner)
                return jsonify({
                    'success': success,
                    'gameover': True,
                    'winner': game.id_to_name[winner],
                    'with_bot': True,
                    'bot_move': [str(row), str(col)],
                })
            elif game.check_draw(game.board):
                game.add_savegame(None, rounds, True)
                game.save_game("savegame.csv")
                game.update_statistics(winner)
                return jsonify({
                    'success': success,
                    'gameover': True,
                    'winner': None,
                    'with_bot': True,
                    'bot_move': [str(row), str(col)],
                })
            else:
                return jsonify({
                    'success': success,
                    'gameover': False,
                    'winner': None,
                    'with_bot': True,
                    'bot_move': [str(row), str(col)]
                })
        else:
            return jsonify({
                'success': success,
                'gameover': False,
                'winner': None,
                'with_bot': False,
            })
            
@app.route("/tic-tac-toe/statistics")
def stats():
    stats = pd.read_csv("statistics.csv", index_col=0)
    stats['timepermove'] = stats['thinking_time'] / stats['moves_take']
    stats.sort_values(by=['wins'], ascending=False, inplace=True)
    names = stats.index.tolist()[:8]
    games = [int(v) for v in stats['played'].tolist()[:8]]
    wins =  [int(v) for v in stats['wins'].tolist()[:8]]
    timepermove = ["%.5f" % v for v in stats['timepermove'].tolist()[:8]]
    return render_template('stats.html', len=len(names), names=names, games=games, wins=wins, timepermove=timepermove)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)