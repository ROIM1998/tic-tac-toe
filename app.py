from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/tic-tac-toe")
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)