# Define the application directory
import os


class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # Statement for enabling the development environment
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False
