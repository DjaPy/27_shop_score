from flask import Flask
from app_shop_score.routes import score_page
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(score_page)

db = SQLAlchemy()