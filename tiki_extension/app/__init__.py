from flask import Flask

from flask_cors import CORS

from app.extensions import db
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    from app.hello import bp as hello_blueprint
    app.register_blueprint(hello_blueprint)
    from app.tiki import bp as tiki_blueprint
    app.register_blueprint(tiki_blueprint)

    register_extension(app)
    app.app_context().push()
    return app


def register_extension(app):
    with app.app_context():
        db.init_app(app)
