from flask import Flask
from flask import render_template
import game_of_life

app = Flask(__name__)


@app.route('/')
def index():
    game_of_life.GameOfLife(50, 50)
    return render_template('index.html')


@app.route('/live')
def live():
    game = game_of_life.GameOfLife()
    if game.counter > 0:
            game.form_new_generation()
    game.counter += 1
    return render_template('live.html', game=game)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)





