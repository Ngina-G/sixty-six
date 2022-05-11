from flask import render_template, redirect,url_for, abort
from flask_login import login_required, current_user
from . import main
from ..requests import get_pitch, display_all_pitches
from ..models import Comment, Pitch, User, PhotoProfile
from .forms import PitchForm, CommentForm, UpdateProfile
from .. import db,photos

# @main.route('/', methods = ['GET','POST'])
# def index():
#     """
#     View root page function that returns the index page and its data
#     """
#     pitches = Pitch.get_pitches()
#     title = 'Home'

#     return render_template('index.html', title=title, pitches=pitches)

@main.route('/')
@login_required
def index():

    form = PitchForm()
    pitches = Pitch.query.all()

    if form.validate_on_submit():
        form = PitchForm()
        pitch = Pitch(
            category = form.category.data,
            pitch = form.pitch.data,
            pitch_author = form.pitch_author.data)

        db.session.add(pitch)
        db.session.commit()
        new_pitch = Pitch(id,category,pitch,pitch_author)
        new_pitch.save_pitch()

        if current_user.is_authenticated:
            pitches = Pitch.query.filter_by(user=current_user.username).all()
        else:
            pitches = []

    # pitches=Pitch.query.order_by(Pitch.posted.desc())
    # top_pitch=Pitch.query.order_by(Pitch.upvotes.desc()).first()  
          
    return render_template('index.html', pitches=pitches, pitch_form=form)

    # form = PitchForm()
    # pitch = display_all_pitches(self)
    # comments = Comment.get_comments(pitch.id) 

    # if form.validate_on_submit():
    #     form = PitchForm()
    #     pitch = Pitch(
    #         category = form.category.data,
    #         pitch = form.pitch.data,
    #         pitch_author = form.pitch_author.data)

    #     db.session.add(pitch)
    #     db.session.commit()
    #     # new_pitch = Pitch(id,category,pitch,pitch_author)
    #     # new_pitch.save_pitch()
    #     if current_user.is_authenticated:
    #         pitches = Pitch.query.filter_by(user=current_user.username).all()
    #     else:
    #         pitches = []
    # return render_template('index.html')

@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    pitch = Pitch.query.filter_by(id=id).all()

    if form.validate_on_submit():
        content = form.content.data
        author = form.author.data

        #update comments instance
        new_comment = Comment(pitch_id=pitch.id, content=content, author=author, user=current_user)
        # save review method
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

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        user_photo = PhotoProfile(pic_path = path,user = user)
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))