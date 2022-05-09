from flask import render_template
from flask_login import login_required
from . import main
from ..requests import get_all_pitches, get_pitch
from ..models import Comment
from .forms import PitchForm, CommentForm

@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    get_all_pitches = Pitches.get_all_pitches()
    title = 'Home'
    return render_template('index.html', title=title, pitches=get_all_pitches)

def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        category = form.category.data
        pitch = form.pitch.data
        author = form.pitch_author.data

        new_pitch = Pitch(id,category,pitch,pitch_author)
        new_pitch.save_pitch()

        return render_template('index.html',category=category,pitch=pitch,author=author)

# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_comment(id):