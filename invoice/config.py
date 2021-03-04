# Define the application directory
import os

POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
DB_URL = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/flask'


class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # Statement for enabling the development environment
    DEBUG = False
    # DATABASE_URI = "postgresql+psycopg2://postgres:password@localhost:5432/flask"
    # DATABASE_URI = "postgresql+psycopg2://postgres:password@localhost:5434/flask"
    # DATABASE_URI = "postgresql+psycopg2://postgres:password@db:5432/flask"
    # DATABASE_URI = "postgresql+psycopg2://postgres:password@localhost:5434/flask"
    DATABASE_URI = DB_URL


class DevelopmentConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False
