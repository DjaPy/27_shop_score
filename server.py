from flask import render_template
from sqlalchemy import func
from datetime import datetime, date
from score.app import score_shop

TIME_WAITING = 0.0


@score_shop.route('/')
def score():


    day_confirmed_filter = func.date(Orders.confirmed) == date.today()
    if Orders.confirmed.is_(None):

    confirmed_is_not_none = Orders.confirmed.isnot(None)


    open_orders = Orders.query.filter(confirmed_is_none)
    open_orders_count = open_orders.count()
    done_today = Orders.query.filter(day_confirmed_filter)

    if done_today:
        confirmed_orders_count = done_today.filter(c.count()
    if open_orders.order_by(Orders.created).first():
        waiting_time = datetime.now() - open_orders.order_by(Orders.created).first().created
        waiting_time = round(waiting_time, 1)
    else:
        waiting_time = TIME_WAITING

    return render_template('score.html',
                           now=datetime.today(),
                           score=waiting_time,
                           orders_count=open_orders_count,
                           done_today=confirmed_orders_count,
                           )


if __name__ == "__main__":
    score_shop.run()
