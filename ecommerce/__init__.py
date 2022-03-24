from flask import Flask

from .settings import Settings


def create_app():
    app = Flask(__name__)
    app.config.from_object(Settings)
    
    return app
