import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = False
SQLALCHEMY_DATABASE_URI = 'postgresql://score:Rysherat2@shopscore' \
                          '.devman.org:5432/shop'
SQLALCHEMY_TRACK_MODIFICATIONS = False
