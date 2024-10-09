from flask import Blueprint

ingredients_blueprint = Blueprint("ingredients", __name__)


@ingredients_blueprint.route("/")
def get_all_ingredients():
    return "all ingredients"
