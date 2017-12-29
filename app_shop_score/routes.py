from app_shop_score import app
from flask import render_template


@app.route('/')
def score():
    return render_template('score.html')