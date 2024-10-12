from flask import Flask
from .extensions import db, migrate
from .routes.ui import ui_blueprint
from .routes.api import api_blueprint
from .models import Ingredient, Recipe, RecipeIngredient


def create_app(config_class):
    app = Flask(__name__, static_folder="../../frontend/dist")
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(ui_blueprint, url_prefix=None)
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
