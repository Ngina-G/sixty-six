from . import db

class User(db.Model):
    """
    User class that will help in creating users
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'