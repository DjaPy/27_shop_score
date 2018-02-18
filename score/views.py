import datetime
from flask import render_template, Response, send_from_directory, request
from score.models import db
from score.app import score_shop
from score import query_db


@score_shop.route('/')
def score():
    confirmed_orders_count = query_db.get_completed_orders()
    open_orders_count = query_db.get_fulfillment_orders()
    waiting_time = query_db.get_time_fulfillment_delay()
    waiting_time = round(waiting_time, 1)
    return render_template('score.html',
                           score=waiting_time,
                           orders_count=open_orders_count,
                           done_today=confirmed_orders_count,
                           )


@score_shop.route('/robots.txt')
def static_from_root():
    return send_from_directory(score_shop.static_folder, request.path[1:])
