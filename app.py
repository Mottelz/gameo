from flask import Flask, render_template, redirect, url_for
from model import db, Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def home():
    return redirect(url_for('games'))


@app.route('/games')
def list_games():
    games = Game.query.order_by(Game.name).all()
    return render_template('games.html', title="Games", games=games)


@app.errorhandler(404)
def page_missing(e):
    return render_template('page.html', title='404', msg=str(e))


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
