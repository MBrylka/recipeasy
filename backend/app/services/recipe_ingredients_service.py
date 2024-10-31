
import uuid
from ..models import RecipeIngredient
from ..exceptions import EmptyBodyError, InvalidUUIDError, JsonParseError, DatabaseError, NotFoundError
from ..extensions import db


def get_all_recipe_ingredients():
    ingredients = RecipeIngredient.query.all()
    return [ingredient.to_dict() for ingredient in ingredients]


def create_recipe_ingredient(data):
    if not data:
        raise EmptyBodyError("No json data provided")
    try:
        recipe_id = data.get("recipeId")
        ingredient_id = data.get("ingredientId")
        quantity = data.get("quantity")
    except:
        raise JsonParseError("Exception when deserializing data")
    try:
        new_recipe_ingredient = RecipeIngredient(recipe_id, ingredient_id, quantity)
        db.session.add(new_recipe_ingredient)
        db.session.commit()
    except:
        raise DatabaseError("Exception when creating object in database")
    return new_recipe_ingredient.to_dict()


def update_recipe_ingredient_by_id(recipe_ingredient_id, data):
    try:
        recipe_ingredient_uuid = uuid.UUID(recipe_ingredient_id)
    except ValueError:
        raise InvalidUUIDError("ID must be in uuid format")
    recipe_ingredient = RecipeIngredient.query.filter_by(
        id=recipe_ingredient_uuid
    ).first()
    if not recipe_ingredient:
        raise NotFoundError(f"Recipe ingredient with ID: {recipe_ingredient_id} not found")
    for key, value in data.items():
        if hasattr(recipe_ingredient, key):
            setattr(recipe_ingredient, key, value)
    db.session.commit()
    return recipe_ingredient.to_dict()


def delete_recipe_ingredient_by_id(recipe_ingredient_id):
    try:
        recipe_ingredient_uuid = uuid.UUID(recipe_ingredient_id)
    except ValueError:
        raise InvalidUUIDError("ID must be in uuid format")

    deleted = RecipeIngredient.query.filter_by(id=recipe_ingredient_uuid).delete()
    db.session.commit()
    if deleted > 0:
        return {"success": True}
    else:
        raise NotFoundError(f"Recipe ingredient with ID: {recipe_ingredient_id} not found")