import uuid
from flask import Blueprint
from flask import request
from ..exceptions import DatabaseError, EmptyBodyError, InvalidUUIDError, JsonParseError, NotFoundError
from ..services.recipes_service import create_recipe, delete_recipe_by_id, get_all_recipes, get_recipe_by_id, get_recipe_ingredients_by_recipe_id, update_recipe_by_id


recipes_blueprint = Blueprint("recipes", __name__)


@recipes_blueprint.route("/")
def get_recipes():
    recipes = get_all_recipes()
    return {"recipes": recipes}, 200


@recipes_blueprint.route("/<string:recipe_id>")
def select_recipe(recipe_id):
    try:
        recipe = get_recipe_by_id(recipe_id)
        return recipe, 200
    except InvalidUUIDError as err:
        return {"error": str(err)}, 400
    except NotFoundError as err:
        return {"error": str(err)}, 404


@recipes_blueprint.route("/<string:recipe_id>/ingredients")
def select_recipe_ingredients(recipe_id):
    try:
        ingredients = get_recipe_ingredients_by_recipe_id(recipe_id)
        return ingredients, 200
    except InvalidUUIDError as err:
        return {"error": str(err)}, 400
    except NotFoundError as err:
        return {"error": str(err)}, 404


@recipes_blueprint.route("/<string:recipe_id>", methods=["PATCH"])
def update_recipe(recipe_id):
    try:
        data = request.get_json()
        result = update_recipe_by_id(recipe_id, data)
        return result, 200
    except InvalidUUIDError as err:
        return {"error": str(err)}, 400
    except NotFoundError as err:
        return {"error": str(err)}, 404


@recipes_blueprint.route("/<string:recipe_id>", methods=["DELETE"])
def remove_recipe(recipe_id):
    try:
        result = delete_recipe_by_id(recipe_id)
        return result, 200
    except InvalidUUIDError as err:
        return {"error": str(err)}, 400
    except NotFoundError as err:
        return {"error": str(err)}, 404


@recipes_blueprint.route("/", methods=["POST"])
def add_recipe():
    try:
        data = request.get_json()
        result = create_recipe( data)
        return result, 200
    except EmptyBodyError as err:
        return {"error": str(err)}, 400
    except JsonParseError as err:
        return {"error": str(err)}, 400
    except DatabaseError as err:
        return {"error": str(err)}, 500