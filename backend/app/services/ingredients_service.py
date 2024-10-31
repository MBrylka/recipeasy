from sqlite3 import DatabaseError
import uuid
from ..exceptions import EmptyBodyError, InvalidUUIDError, JsonParseError, NotFoundError
from ..models import Ingredient
from ..extensions import db

def get_all_ingredients():
    ingredients = Ingredient.query.all()
    return [ingredient.to_dict() for ingredient in ingredients]


def get_ingredient_by_id(ingredient_id):
    try:
        ingredient_uuid = uuid.UUID(ingredient_id)
    except ValueError:
        raise InvalidUUIDError("ID must be in uuid format")
    ingredient = Ingredient.query.filter_by(id=ingredient_uuid).first()
    if not ingredient:
        raise NotFoundError(f"Recipe with ID: {ingredient_id} not found")
    return ingredient.to_dict()


def update_ingredient_by_id(ingredient_id, data):
    try:
        ingredient_uuid = uuid.UUID(ingredient_id)
    except ValueError:
        raise InvalidUUIDError("ID must be in uuid format")
    ingredient = Ingredient.query.filter_by(id=ingredient_uuid).first()
    if not ingredient:
        raise NotFoundError(f"Recipe with ID: {ingredient_id} not found")
    for key, value in data.items():
        if hasattr(ingredient, key):
            setattr(ingredient, key, value)
    db.session.commit()
    return ingredient.to_dict()


def delete_ingredient_by_id(ingredient_id):
    try:
        ingredient_uuid = uuid.UUID(ingredient_id)
    except ValueError:
        raise InvalidUUIDError("ID must be in uuid format")
    deleted = Ingredient.query.filter_by(id=ingredient_uuid).delete()
    db.session.commit()
    if deleted > 0:
        return {"success": True}
    else:
        raise NotFoundError(f"Recipe with ID: {ingredient_id} not found")
    

def create_ingredient(data):
    if not data:
        raise EmptyBodyError("No json data provided")
    try:
        name = data.get("name")
        calories = data.get("calories")
        carbs = data.get("carbs")
        protein = data.get("protein")
        fat = data.get("fat")
    except:
        raise JsonParseError("Exception when deserializing data")

    try:
        new_ingredient = Ingredient(name, calories, carbs, protein, fat)
        db.session.add(new_ingredient)
        db.session.commit()
    except:
        raise DatabaseError("Exception when creating object in database")
    return new_ingredient.to_dict()
