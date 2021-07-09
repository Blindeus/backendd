from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from marshmallow.exceptions import ValidationError
from .configs import Config


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
ma = Marshmallow()


def register_blueprint(app):
    from project.endpoints import usuariosb

    app.register_blueprint(usuariosb)

def register_error_handlers(app):
    @app.errorhandler(ValidationError)
    def validation_error_handler(e):
        return e.massages,400

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_blueprint(app)
    register_error_handlers(app)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    ma.init_app(app)

    return app
