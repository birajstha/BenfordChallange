from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from birajwebapp.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from birajwebapp.main.routes import main
    from birajwebapp.benfordapp.routes import benfordapp
    from birajwebapp.errors.handlers import errors
    from birajwebapp.entity.utils import entity
    app.register_blueprint(main)
    app.register_blueprint(benfordapp)
    app.register_blueprint(errors)
    app.register_blueprint(entity)

    return app