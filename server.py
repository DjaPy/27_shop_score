from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import datetime, timedelta, date


TIME_WAITING = 0.0

app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)


class Orders(db.Model):
    __tablename__ = 'orders'


@app.route('/')
def score():
    day_confirmed_filter = func.date(Orders.confirmed) == date.today()
    confirmed_is_none = Orders.confirmed.is_(None)
    confirmed_is_not_none = Orders.confirmed.isnot(None)

    db_query = Orders.query
    open_orders = db_query.filter(confirmed_is_none)
    open_orders_count = open_orders.count()
    done_today = db_query.filter(day_confirmed_filter)

    if done_today:
        confirmed_orders_count = done_today.filter(
            confirmed_is_not_none).count()
    if open_orders.order_by(Orders.created).first():
        waiting_time = datetime.now() - open_orders.order_by(Orders.created).first().created
        waiting_time = round(waiting_time, 1)
    else:
        waiting_time = TIME_WAITING

    return render_template('score.html',
                           now=datetime.today(),
                           score =waiting_time,
                           orders_count=open_orders_count,
                           done_today=confirmed_orders_count,
                           )


if __name__ == "__main__":
    app.run()
