from flask import Flask
from flask_bootstrap import Bootstrap
from Config import config_options

#Initializing Application and Initializing Flask Extensions

bootstrap = Bootstrap()

def create_app(config_name):
    """Creating app configurations
        Initializing flask extensions
        Registering the blueprint
        setting Config
        Adds the views and forms
    """

    app = Flask(__name__)

    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    