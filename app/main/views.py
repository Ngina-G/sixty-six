from flask import render_template, redirect,url_for, abort
from flask_login import login_required
from . import main
from ..requests import get_pitch, display_all_pitches
from ..models import Comment, Pitch, User
from .forms import PitchForm, CommentForm, UpdateProfile
from .. import db

@main.route('/', methods = ['GET','POST'])
def index():
    """
    View root page function that returns the index page and its data
    """
    pitches = Pitch.get_pitches()
    title = 'Home'
    # form = PitchForm()

    # if form.validate_on_submit():
    #     category = form.category.data
    #     pitch = form.pitch.data
    #     pitch_author = form.pitch_author.data

    #     new_pitch = Pitch(id,category,pitch,pitch_author)
    #     new_pitch.save_pitch()

    return render_template('index.html', title=title, pitches=pitches)

@main.route('/pitch',  methods = ['GET','POST'])
@login_required
def pitch():

    form = PitchForm()
    pitch = display_all_pitches(self)
    title = f'{pitch.category}'
    comments = Comment.get_comments(pitch.id) 

    if form.validate_on_submit():
        category = form.category.data
        pitch = form.pitch.data
        pitch_author = form.pitch_author.data

        new_pitch = Pitch(id,category,pitch,pitch_author)
        new_pitch.save_pitch()
        

    return render_template('index.html', pitch_form=form, pitch=pitch, title=title, comments=comments)

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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)