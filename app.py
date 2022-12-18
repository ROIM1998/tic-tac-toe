from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
game = None

@app.route("/tic-tac-toe")
def index():
    return render_template('index.html')

@app.route("/tic-tac-toe/play")
def play():
    if request.args.get('playmode') == 'pvp':
        return render_template('play.html', player1=request.args.get('player1'), player2=request.args.get('player2'))
    elif request.args.get('playmode') == 'pve':
        return render_template('play.html', player1=request.args.get('player1'), player2=request.args.get('botmode2') + 'Bot')
    elif request.args.get('playmode') == 'eve':
        return render_template('play.html', player1=request.args.get('botmode1') + 'Bot', player2=request.args.get('botmode2') + 'Bot')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)