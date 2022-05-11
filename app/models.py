from . import db
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


class Pitch(db.Model):
    """
        Pitch class
    """
    __tablename__='pitches'

    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String)
    pitch = db.Column(db.String)
    pitch_author = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    def __init__(self,id,category,pitch,pitch_author):
        self.id = id
        self.category = category
        self.pitch = pitch
        self.pitch_author = pitch_author

    def create_pitch(self):
       db.session.add(self)
       db.session.commit()
       return self

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitch(cls):
        db.session.drop(self)
        db.session.commit()

    @classmethod
    def search_pitches(cls,category):
        pitches = Pitch.query.filter_by(category=category).all()
        return pitches

    @classmethod
    def get_pitches(cls):
        pitches = Pitch.query.all()

class Comment(db.Model):
    """
        Comments class
    """
    __tablename__='comments'

    id = db.Column(db.Integer, primary_key = True)
    pitch_id = db.Column(db.Integer)
    content = db.Column(db.String)
    author = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def create_comment(self):
       db.session.add(self)
       db.session.commit()
       return self

    def save_comment(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def clear_comment(cls):
        db.session.drop(self)
        db.session.commit()


    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments


class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'

