from flask import render_template, redirect,url_for, abort
from flask_login import login_required, current_user
from . import main
from ..requests import get_pitch, display_all_pitches
from ..models import Comment, Pitch, User, PhotoProfile
from .forms import PitchForm, CommentForm, UpdateProfile
from .. import db,photos


@main.route('/')
@login_required
def index():

    form = PitchForm()
    pitches = Pitch.query.all()

    # pitches=Pitch.query.order_by(Pitch.posted.desc())
    # top_pitch=Pitch.query.order_by(Pitch.upvotes.desc()).first()  
    return render_template('index.html', pitches=pitches, pitch_form=form)

@main.route('/pitch', methods = ['POST','GET'])
@login_required
def pitch():
    form = PitchForm()
    user = User.query.all()

    if form.validate_on_submit():
        user = User.query.all()

        form = PitchForm()
        category = form.category.data,
        pitch = form.pitch.data,
        pitch_author = form.pitch_author.data
        user_id = current_user._get_current_object().id
        new_pitch = Pitch(category=category,pitch=pitch,pitch_author=pitch_author,user_id=user_id)
        new_pitch.save_pitch()
        

        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))

        
    return render_template( 'pitch.html',pitch_form=form)



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