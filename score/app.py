from flask import Flask


score_shop = Flask(__name__)
score_shop.config.from_object('config')
