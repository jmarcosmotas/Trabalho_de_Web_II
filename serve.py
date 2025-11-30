# Arquivo main.py
from flask import Flask
from database.init import db
from database.models import *
from database.seed import preencher_table
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///banco.db"
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-secret-change-me')

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    SESSION_COOKIE_SECURE=False,
)

db.init_app(app)

from route import *

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        preencher_table()
    app.run(debug=True)