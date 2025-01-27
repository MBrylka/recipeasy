from flask import Blueprint
from .recipes import recipes_blueprint
from .ingredients import ingredients_blueprint
from .recipeIngredients import recipe_ingredients_blueprint
from .upload import upload_blueprint

api_blueprint = Blueprint("api", __name__)

api_blueprint.register_blueprint(recipes_blueprint, url_prefix="/recipes")
api_blueprint.register_blueprint(ingredients_blueprint, url_prefix="/ingredients")
api_blueprint.register_blueprint(
    recipe_ingredients_blueprint, url_prefix="/recipe-ingredients"
)
api_blueprint.register_blueprint(upload_blueprint, url_prefix="/upload")