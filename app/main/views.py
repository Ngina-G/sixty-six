from flask import render_template
from flask_login import login_required
from . import main
from ..requests import get_pitch
from ..models import Comment, Pitch
from .forms import PitchForm, CommentForm

@main.route('/', methods = ['GET','POST'])
def index():
    """
    View root page function that returns the index page and its data
    """
    pitches = Pitch.get_pitches()
    title = 'Home'
    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        pitch = form.pitch.data
        pitch_author = form.pitch_author.data

        new_pitch = Pitch(id,category,pitch,pitch_author)
        new_pitch.save_pitch()

    return render_template('index.html', title=title, pitches=pitches, pitch_form=form)

@main.route('/',  methods = ['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        pitch = form.pitch.data
        pitch_author = form.pitch_author.data

        new_pitch = Pitch(id,category,pitch,pitch_author)
        new_pitch.save_pitch()
        

    return render_template('index.html', pitch_form=form)

@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    pitch = get_pitch(id)

    if form.validate_on_submit():
        content = form.content.data
        author = form.author.data

        new_comment = Comment(pitch_id, content, author)
        new_comment.save_comment()

        return redirect(url_for('.pitch', id = pitch.id))

    title = f'{pitch.pitch}'
    return render_template('comment.html', title=title, comment_form=form, pitch=pitch)