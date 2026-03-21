# config.py
SECRET_KEY = 'your_secret_key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
DEBUG = True


class Config:
    SECRET_KEY = 'your_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/prod_db'