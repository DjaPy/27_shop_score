import json
from flask import render_template, Response, send_from_directory, request
from score.models import db
from score.app import score_shop
from score import query_db


@score_shop.route('/api/score_information')
def score_information():
    json_data = {
        'count_completed_orders': query_db.get_completed_orders(),
        'count_fulfillment_orders': query_db.get_fulfillment_orders(),
        'max_fulfillment_orders_delay': query_db.get_time_fulfillment_delay(),
    }
    response = Response(json.dumps(json_data),
                        status=200,
                        mimetype='application/json')
    return response


@score_shop.route('/')
def score():
    confirmed_orders_count = query_db.get_completed_orders()
    open_orders_count = query_db.get_fulfillment_orders()
    waiting_time = query_db.get_time_fulfillment_delay()


    return render_template('score.html',
                           now=datetime.today(),
                           score=waiting_time,
                           orders_count=open_orders_count,
                           done_today=confirmed_orders_count,
                           )


@score_shop.route('/robots.txt')
def static_from_root():
    return send_from_directory(score.static_folder, request.path[1:])
