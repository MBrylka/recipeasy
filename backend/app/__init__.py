from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes.ui import ui_blueprint
from app.routes.api import api_blueprint

db = SQLAlchemy()


def create_app(config_class):
    app = Flask(__name__, static_folder="../../frontend/dist")
    app.config.from_object(config_class)

    db.init_app(app)

    app.register_blueprint(ui_blueprint, url_prefix=None)
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
