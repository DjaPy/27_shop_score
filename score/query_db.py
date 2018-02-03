import pytz
from score.models import Orders
from datetime import timedelta, datetime

NUMBERS_OF_DAYS = 1
SECONDS = 60
NO_FULFILMENT = 0


def get_completed_orders(period=NUMBERS_OF_DAYS):
    tz = pytz.timezone('Europe/Moscow')
    orders_query = Orders.query
    orders_query = orders_query.filter((Orders.created + timedelta(period)) > datetime.now(tz))
    orders_query = orders_query.filter(Orders.status == 'COMPLETED')
    return orders_query.count()


def get_fulfillment_orders():
    orders_query = Orders.query
    orders_query = orders_query.filter(Orders.status == 'FULFILLMENT')
    return orders_query.count()


def utc_to_local(utc_dt):
    local_tz = pytz.timezone('Europe/Moscow')
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    local_dt = local_tz.normalize(local_dt)
    return local_dt.replace(tzinfo=None)


def get_oldest_fulfillment_order():
    orders_query = Orders.query
    orders_query = orders_query.filter(Orders.status == 'FULFILLMENT')
    orders_query = orders_query.order_by(Orders.created)
    if not orders_query.count():
        return None
    return orders_query.first().created


def get_time_fulfillment_delay():
    created = get_oldest_fulfillment_order()
    if created is None:
        return NO_FULFILMENT
    now = utc_to_local(datetime.now())
    difference_in_seconds = (now - created).total_seconds()
    return difference_in_seconds / SECONDS


if __name__ == "__main__":
    print(get_completed_orders(period=NUMBERS_OF_DAYS))
    print(get_fulfillment_orders())
    print(get_fulfillment_orders())
    print(get_oldest_fulfillment_order())

