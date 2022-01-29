from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import DevelopmentConfig

db = SQLAlchemy()
DB_NAME = "db.sqlite3"

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())
    db.init_app(app)

    from .views import register_views
    register_views(app)

    create_db(app)

    return app

def create_db(app):
    if not path.exists("api/" + DB_NAME):
        db.create_all(app=app)
        print("Db created")