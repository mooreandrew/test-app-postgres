import os

class Config(object):
    DEBUG = False
    LOGGING_PATH = os.getenv('LOGGING_PATH', 'python_logging/logging.yaml')
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']

class DevelopmentConfig(Config):
    TESTVALUE = os.environ['TESTVALUE']
    DEBUG = True

class ProductionConfig(Config):
    TESTVALUE = os.environ['TESTVALUE']
    DEBUG = True
