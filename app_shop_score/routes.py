from flask import Blueprint, render_template

score_page = Blueprint('score_page', __name__,
                       template_folder='templates')

@score_page.route('/')
def score():
    return render_template('score.html')
