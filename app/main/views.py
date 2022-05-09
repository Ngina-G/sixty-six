from flask import render_template
from flask_login import login_required
from . import main

@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    return render_template('index.html')

# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_comment(id):