# from flask import Flask

# app = Flask(__name__)

# @app.route('/home')
# def index():
#     return "main page!"


# if __name__ == '_main_':
#     app.run(debug=True)

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    released = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)

    def _repr_(self):
        return f"Movie('{self.title}', '{self.released}', '{self.director}', '{self.genre}')"