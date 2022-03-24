from flask import Flask

from .routes import register_routes
from .settings import Settings


def create_app():
    app = Flask(__name__)
    app.config.from_object(Settings)
    
    register_routes(app)
    
    return app
