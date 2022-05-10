from flask import Flask, render_template
from model import db, Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def home():
    games = Game.query.order_by(Game.name).all()
    return render_template('games.html', title="Games", games=games)