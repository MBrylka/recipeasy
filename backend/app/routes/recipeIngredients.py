import uuid
from flask import Blueprint, jsonify
from flask import request
from ..models import RecipeIngredient
from ..extensions import db

recipe_ingredients_blueprint = Blueprint("recipe-ingredients", __name__)


@recipe_ingredients_blueprint.route("/")
def get_all_recipe_ingredients():
    recipe_ingredients = RecipeIngredient.query.all()
    return {
        "recipeIngredients": [
            recipe_ingredient.to_dict() for recipe_ingredient in recipe_ingredients
        ]
    }


@recipe_ingredients_blueprint.route("/", methods=["POST"])
def create_recipe_ingredient():
    data = request.get_json()
    if not data:
        return {"error": "no json data provided"}, 400
    try:
        recipe_id = data.get("recipeId")
        ingredient_id = data.get("ingredientId")
        quantity = data.get("quantity")
    except:
        return {"error": "Exception when deserializing data"}, 400

    try:
        new_recipe_ingredient = RecipeIngredient(recipe_id, ingredient_id, quantity)
        db.session.add(new_recipe_ingredient)
        db.session.commit()
    except:
        return {"error": "Exception when creating object in database"}, 400

    return new_recipe_ingredient.to_dict(), 204


@recipe_ingredients_blueprint.route("/<string:recipe_ingredient_id>", methods=["PATCH"])
def update_recipe_ingredient_by_id(recipe_ingredient_id):
    try:
        recipe_ingredient_uuid = uuid.UUID(recipe_ingredient_id)
    except ValueError:
        return {"error": "ID must be in uuid format"}, 400

    recipe_ingredient = RecipeIngredient.query.filter_by(
        id=recipe_ingredient_uuid
    ).first()
    if not recipe_ingredient:
        return {"error": f"Ingredient with ID: {recipe_ingredient_id} not found"}, 404
    data = request.get_json()

    for key, value in data.items():
        if hasattr(recipe_ingredient, key):
            setattr(recipe_ingredient, key, value)

    db.session.commit()
    return {"success": True, "Recipe Ingredient": recipe_ingredient.to_dict()}, 200


@recipe_ingredients_blueprint.route(
    "/<string:recipe_ingredient_id>", methods=["DELETE"]
)
def delete_recipe_ingredient_by_id(recipe_ingredient_id):
    try:
        recipe_ingredient_uuid = uuid.UUID(recipe_ingredient_id)
    except ValueError:
        return {"error": "ID must be in uuid format"}, 400

    deleted = RecipeIngredient.query.filter_by(id=recipe_ingredient_uuid).delete()
    db.session.commit()
    if deleted > 0:
        return {"success": True}, "200"
    else:
        return {
            "error": f"Recipe Ingredient with ID: {recipe_ingredient_id} not found"
        }, 404
