from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import ValidationError, InputRequired
from ..models import Pitch, Comment

class PitchForm(FlaskForm):

    category = StringField('Add Category (business, love, comedy, insiprational)',validators=[InputRequired()])
    pitch = TextAreaField('Pitch', validators=[InputRequired()])
    pitch_author = StringField('Your Name', validators=[InputRequired()])
    submit_pitch = SubmitField('Submit')

class CommentForm(FlaskForm):

    content = TextAreaField('Pitch', validators=[InputRequired()])
    author = StringField('Your Name', validators=[InputRequired()])
    submit_comment = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')