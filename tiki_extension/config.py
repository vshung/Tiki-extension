import os


class Config:
    SECRET_KEY = 'tiki'
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % (os.path.join(PROJECT_ROOT, "tiki.db"))
    JSON_AS_ASCII = False
