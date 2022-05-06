from flask import Blueprint
from . import views,forms,error

main = Blueprint('main', __name_)