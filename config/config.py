from os import environ, path, getcwd
from dotenv import load_dotenv

basedir = path.dirname(getcwd())
load_dotenv(path.join(basedir, ".env"))

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_ENV = environ.get('FLASK_ENV')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # DB_NAME = "development-db"
    # DB_USERNAME = "admin"
    # DB_PASSWORD = "example"

    # IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"
    

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False