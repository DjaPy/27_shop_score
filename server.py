from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import datetime, timedelta, date

ORDER_NUM = 10
BAD_DIFF_TIME = 30
SATISFACTORY_DIFF_TIME = 7

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

    if open_orders_count:
        latest_open_order = open_orders.order_by(
            Orders.created).first()

        if latest_open_order:
            latest_open_order_time_min = round((datetime.now() -
                                                latest_open_order.created).total_seconds())

            if latest_open_order_time_min > timedelta(BAD_DIFF_TIME):
                color = 'firebrick'
            elif latest_open_order_time_min > timedelta(SATISFACTORY_DIFF_TIME):
                color = 'darkgoldenrod'
    else:
        color = 'darkgreen'
    return render_template('score.html',
                           now=datetime.today(),
                           seven_minutes=timedelta(minutes=7),
                           thirty_minutes=timedelta(minutes=30),
                           orders=open_orders[:ORDER_NUM],
                           orders_count=open_orders_count,
                           done_today=confirmed_orders_count,
                           color=color)


if __name__ == "__main__":
    app.run()
