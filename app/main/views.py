from flask import render_template
from flask_login import login_required
from . import main
from ..requests import get_all_pitches, get_pitch
from ..models import Comment

@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    get_all_pitches = get_all_pitches()
    title = 'Home'
    return render_template('index.html', title=title, pitches=get_all_pitches)



# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_comment(id):