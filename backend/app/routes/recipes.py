from flask import Blueprint

recipes_blueprint = Blueprint("recipes", __name__)


@recipes_blueprint.route("/")
def get_all_recipes():
    return "all recipes"
