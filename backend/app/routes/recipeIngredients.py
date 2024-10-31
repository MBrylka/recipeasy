import uuid
from flask import Blueprint
from flask import request

from ..exceptions import EmptyBodyError, InvalidUUIDError, JsonParseError, DatabaseError, NotFoundError
from ..services.recipe_ingredients_service import create_recipe_ingredient, delete_recipe_ingredient_by_id, get_all_recipe_ingredients, update_recipe_ingredient_by_id

recipe_ingredients_blueprint = Blueprint("recipe-ingredients", __name__)


@recipe_ingredients_blueprint.route("/")
def get_recipe_ingredients():
    recipe_ingredients = get_all_recipe_ingredients()
    return {"ingredients": recipe_ingredients}, 200


@recipe_ingredients_blueprint.route("/", methods=["POST"])
def add_recipe_ingredient():
    try:
        data = request.get_json()
        result = create_recipe_ingredient(data)
        return result, 200
    except EmptyBodyError as err:
        return {"error": str(err)}, 400
    except JsonParseError as err:
        return {"error": str(err)}, 400
    except DatabaseError as err:
        return {"error": str(err)}, 500


@recipe_ingredients_blueprint.route("/<string:recipe_ingredient_id>", methods=["PATCH"])
def update_recipe_ingredient(recipe_ingredient_id):
    try:
        data = request.get_json()
        result = update_recipe_ingredient_by_id(recipe_ingredient_id, data)
        return result, 200
    except InvalidUUIDError as err:
        return {"error": str(err)}, 400
    except NotFoundError as err:
        return {"error": str(err)}, 404


@recipe_ingredients_blueprint.route(
    "/<string:recipe_ingredient_id>", methods=["DELETE"]
)
def remove_recipe_ingredient(recipe_ingredient_id):
    try:
        result = delete_recipe_ingredient_by_id(recipe_ingredient_id)
        return result, 200
    except InvalidUUIDError as err:
        return {"error": str(err)}, 400
    except NotFoundError as err:
        return {"error": str(err)}, 404
