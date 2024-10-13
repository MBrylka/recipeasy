import uuid
from flask import Blueprint, jsonify
from flask import request
from ..models import Recipe
from ..extensions import db

recipes_blueprint = Blueprint("recipes", __name__)


@recipes_blueprint.route("/")
def get_all_recipes():
    recipes = Recipe.query.all()
    return {"recipes": [recipe.to_dict() for recipe in recipes]}


@recipes_blueprint.route("/<string:recipe_id>")
def get_recipe_by_id(recipe_id):
    try:
        recipe_uuid = uuid.UUID(recipe_id)
    except ValueError:
        return {"error": "ID must be in uuid format"}, 400

    recipe = Recipe.query.filter_by(id=recipe_uuid).first()
    if not recipe:
        return {"error": f"Recipe with ID: {recipe_id} not found"}, 404

    return recipe.to_dict(), 200


@recipes_blueprint.route("/<string:recipe_id>", methods=["PATCH"])
def update_recipe_by_id(recipe_id):
    try:
        recipe_uuid = uuid.UUID(recipe_id)
    except ValueError:
        return {"error": "ID must be in uuid format"}, 400

    recipe = Recipe.query.filter_by(id=recipe_uuid).first()
    if not recipe:
        return {"error": f"Recipe with ID: {recipe_id} not found"}, 404

    data = request.get_json()

    for key, value in data.items():
        if hasattr(recipe, key):
            setattr(recipe, key, value)

    db.session.commit()
    return jsonify({"success": True, "recipe": recipe.to_dict()}), 200


@recipes_blueprint.route("/<string:recipe_id>", methods=["DELETE"])
def delete_recipe_by_id(recipe_id):
    try:
        recipe_uuid = uuid.UUID(recipe_id)
    except ValueError:
        return {"error": "ID must be in uuid format"}, 400

    deleted = Recipe.query.filter_by(id=recipe_uuid).delete()
    db.session.commit()
    if deleted > 0:
        return {"success": True}, "200"
    else:
        return {"error": f"Recipe with ID: {recipe_id} not found"}, 404


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
