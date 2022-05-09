from . import db
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class Pitch:
    """
        Pitch class
    """
    all_pitches = []

    def __init__(self,id,category,pitch,pitch_author):
        self.id = id
        self.category = category
        self.pitch = pitch
        self.pitch_author = pitch_author

    def save_pitch(self):
        Pitch.all_pitches.append(self)

    @classmethod
    def clear_pitch(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def search_pitches(cls,category):

        for pitch in cls.all_pitches:
            if pitch.category == category:
                return pitch
    @classmethod
    def get_pitches(cls):
        response = []
        for pitch in cls.all_pitches:
            response.append(pitch)
        return response

class Comment:
    """
        Comments class
    """
    all_comments = []

    def __init__(self,pitch_id,content,author):
        self.pitch_id = pitch_id
        self.content = content
        self.author = author

    def save_comment(self):
        Comment.all_comments.append(self)


    @classmethod
    def clear_comment(cls):
        Comment.all_comments.clear()


    @classmethod
    def get_comments(cls,id):

        response = []

        for comment in cls.all_comments:
            if comment.pitch_id == id:
                response.append(comment)

        return response

class User(UserMixin,db.Model):
    """
    User class that will help in creating users
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'
