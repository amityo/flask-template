from flask import Flask
from .config import config

def create_app(config_name):
    """
    Create App
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .api import v1
    app.register_blueprint(v1)

    return app
