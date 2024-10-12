from operator import add
from os import name
from flask import Blueprint, jsonify, session
from flask import request
from ..models import Recipe
from ..extensions import db

recipes_blueprint = Blueprint("recipes", __name__)


@recipes_blueprint.route("/")
def get_all_recipes():
    recipes = Recipe.query.all()
    return {"recipes": [recipe.to_dict() for recipe in recipes]}


@recipes_blueprint.route("/", methods=["POST"])
def create_recipe():
    data = request.get_json()
    if not data:
        return jsonify({"error": "no json data provided"}), 400

    try:
        name = data.get("name")
        description = data.get("description")
    except:
        return jsonify({"error": "Exception when deserializing data"}), 400

    try:
        new_recipe = Recipe(name, description)
        db.session.add(new_recipe)
        db.session.commit()
    except:
        return jsonify({"err": "Exception when creating object in database"}), 400

    return jsonify(new_recipe.to_dict()), 204
