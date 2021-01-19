# Define the application directory
import os


class Config( object ):
    BASE_DIR = os.path.abspath( os.path.dirname( __file__ ) )
    # Statement for enabling the development environment
    DEBUG = False
    # DATABASE_URI = "postgresql+psycopg2://postgres:password@localhost:5432/flask"
    # DATABASE_URI = "postgresql+psycopg2://postgres:password@localhost:5434/flask"
    DATABASE_URI = "postgresql+psycopg2://postgres:password@db:5432/flask"


class DevelopmentConfig( Config ):
    DEBUG = True


class ProdConfig( Config ):
    DEBUG = False
