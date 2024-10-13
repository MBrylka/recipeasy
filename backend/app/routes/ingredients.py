import uuid
from flask import Blueprint, jsonify
from flask import request
from ..models import Ingredient
from ..extensions import db

ingredients_blueprint = Blueprint("ingredients", __name__)


@ingredients_blueprint.route("/")
def get_all_ingredients():
    ingredients = Ingredient.query.all()
    return {"ingredients": [ingredient.to_dict() for ingredient in ingredients]}


@ingredients_blueprint.route("/<string:ingredient_id>")
def get_ingredient_by_id(ingredient_id):
    try:
        ingredient_uuid = uuid.UUID(ingredient_id)
    except ValueError:
        return {"error": "ID must be in uuid format"}, 400

    ingredient = Ingredient.query.filter_by(id=ingredient_uuid).first()

    if not ingredient:
        return {"error": f"Ingredient with ID: {ingredient_id} not found"}, 404

    return ingredient.to_dict(), 200


@ingredients_blueprint.route("/<string:ingredient_id>", methods=["PATCH"])
def update_ingredient_by_id(ingredient_id):
    try:
        ingredient_uuid = uuid.UUID(ingredient_id)
    except ValueError:
        return {"error": "ID must be in uuid format"}, 400

    ingredient = Ingredient.query.filter_by(id=ingredient_uuid).first()
    if not ingredient:
        return {"error": f"Ingredient with ID: {ingredient_id} not found"}, 404

    data = request.get_json()

    for key, value in data.items():
        if hasattr(ingredient, key):
            setattr(ingredient, key, value)

    db.session.commit()
    return jsonify({"success": True, "ingredient": ingredient.to_dict()}), 200


@ingredients_blueprint.route("/<string:ingredient_id>", methods=["DELETE"])
def delete_ingredient_by_id(ingredient_id):
    try:
        ingredient_uuid = uuid.UUID(ingredient_id)
    except ValueError:
        return {"error": "ID must be in uuid format"}, 400

    deleted = Ingredient.query.filter_by(id=ingredient_uuid).delete()
    db.session.commit()
    if deleted > 0:
        return {"success": True}, "200"
    else:
        return {"error": f"Ingredient with ID: {ingredient_id} not found"}, 404


@ingredients_blueprint.route("/", methods=["POST"])
def create_ingredient():
    data = request.get_json()
    if not data:
        return jsonify({"error": "no json data provided"}), 400

    try:
        name = data.get("name")
    except:
        return jsonify({"error": "Exception when deserializing data"}), 400

    try:
        new_ingredient = Ingredient(name)
        db.session.add(new_ingredient)
        db.session.commit()
    except:
        return jsonify({"err": "Exception when creating object in database"}), 400

    return jsonify(new_ingredient.to_dict()), 204
