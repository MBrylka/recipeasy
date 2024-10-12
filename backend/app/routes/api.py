from flask import Blueprint
from .recipes import recipes_blueprint
from .ingredients import ingredients_blueprint

api_blueprint = Blueprint("api", __name__)

api_blueprint.register_blueprint(recipes_blueprint, url_prefix="/recipes")
api_blueprint.register_blueprint(ingredients_blueprint, url_prefix="/ingredients")
