from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240), nullable=False)
    published = db.Column(db.Integer)
    minplayers = db.Column(db.Integer)
    maxplayers = db.Column(db.Integer)
    minplaytime = db.Column(db.Integer)
    maxplaytime = db.Column(db.Integer)
    thumbnail = db.Column(db.String(500))
    description = db.Column(db.String(7500))

    def __repr__(self):
        return f'{self.name} ({self.published})\tPlayers: {self.minplayers}-{self.maxplayers}\tPlaytime: {self.minplaytime}-{self.maxplaytime}'
