from sqlite3 import DatabaseError
import uuid


from ..exceptions import EmptyBodyError, InvalidUUIDError, JsonParseError, NotFoundError
from ..services.ingredients_service import create_ingredient, delete_ingredient_by_id, get_all_ingredients, get_ingredient_by_id, update_ingredient_by_id
from flask import Blueprint, jsonify
from flask import request
from ..models import Ingredient
from ..extensions import db

ingredients_blueprint = Blueprint("ingredients", __name__)


@ingredients_blueprint.route("/")
def get_ingredients():
    ingredients = get_all_ingredients()
    return {"ingredients": ingredients}, 200


@ingredients_blueprint.route("/<string:ingredient_id>")
def select_ingredient(ingredient_id):
    try:
        ingredient = get_ingredient_by_id(ingredient_id)
        return ingredient, 200
    except InvalidUUIDError as err:
        return {"error": str(err)}, 400
    except NotFoundError as err:
        return {"error": str(err)}, 404


@ingredients_blueprint.route("/<string:ingredient_id>", methods=["PATCH"])
def update_ingredient(ingredient_id):
    try:
        data = request.get_json()
        result = update_ingredient_by_id(ingredient_id, data)
        return result, 200
    except InvalidUUIDError as err:
        return {"error": str(err)}, 400
    except NotFoundError as err:
        return {"error": str(err)}, 404


@ingredients_blueprint.route("/<string:ingredient_id>", methods=["DELETE"])
def remove_ingredient(ingredient_id):
    try:
        result = delete_ingredient_by_id(ingredient_id)
        return result, 200
    except InvalidUUIDError as err:
        return {"error": str(err)}, 400
    except NotFoundError as err:
        return {"error": str(err)}, 404


@ingredients_blueprint.route("/", methods=["POST"])
def add_ingredient():
    try:
        data = request.get_json()
        result = create_ingredient(data)
        return result, 200
    except EmptyBodyError as err:
        return {"error": str(err)}, 400
    except JsonParseError as err:
        return {"error": str(err)}, 400
    except DatabaseError as err:
        return {"error": str(err)}, 500
