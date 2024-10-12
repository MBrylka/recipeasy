from flask import Blueprint, jsonify
from ..models import Ingredient

ingredients_blueprint = Blueprint("ingredients", __name__)


@ingredients_blueprint.route("/")
def get_all_ingredients():
    ingredients = Ingredient.query.all()
    return {"ingredients": [ingredient.to_dict() for ingredient in ingredients]}
