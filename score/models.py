from flask_sqlalchemy import SQLAlchemy
from score.app import score_shop

db = SQLAlchemy(score_shop)
db.Model.metadata.reflect(db.engine)


class Orders(db.Model):
    __tablename__ = 'orders'
