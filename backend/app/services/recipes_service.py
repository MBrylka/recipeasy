import uuid

from ..exceptions import DatabaseError, EmptyBodyError, InvalidUUIDError, JsonParseError, NotFoundError
from ..models import Recipe, RecipeIngredient, Ingredient
from ..extensions import db

def get_all_recipes():
    recipes = Recipe.query.all()
    return [recipe.to_dict() for recipe in recipes]


def get_recipe_by_id(recipe_id):
    try:
        recipe_uuid = uuid.UUID(recipe_id)
    except ValueError:
        raise InvalidUUIDError("ID must be in uuid format")
    recipe = Recipe.query.filter_by(id=recipe_uuid).first()
    if not recipe:
        raise NotFoundError(f"Recipe with ID: {recipe_id} not found")
    return recipe.to_dict()


def get_recipe_ingredients_by_recipe_id(recipe_id):
    try:
        recipe_uuid = uuid.UUID(recipe_id)
    except ValueError:
        raise InvalidUUIDError("ID must be in uuid format")
    recipe = Recipe.query.filter_by(id=recipe_uuid).first()
    if not recipe:
        raise NotFoundError(f"Recipe with ID: {recipe_id} not found")
    ingredients_list = []
    recipe_ingredients = RecipeIngredient.query.filter_by(recipe_id=recipe_uuid).all()
    for recipe_ingredient in recipe_ingredients:
        ingredient = Ingredient.query.filter_by(
            id=recipe_ingredient.ingredient_id
        ).first()
        ingredients_list.append(
            {
                "recipeIngredient": recipe_ingredient.to_dict(),
                "ingredient": ingredient.to_dict(),
            }
        )
    return ingredients_list


def update_recipe_by_id(recipe_id, data):
    try:
        recipe_uuid = uuid.UUID(recipe_id)
    except ValueError:
        raise InvalidUUIDError("ID must be in uuid format")
    recipe = Recipe.query.filter_by(id=recipe_uuid).first()
    if not recipe:
        raise NotFoundError(f"Recipe with ID: {recipe_id} not found")
    for key, value in data.items():
        if hasattr(recipe, key):
            setattr(recipe, key, value)
    db.session.commit()
    return recipe.to_dict()


def delete_recipe_by_id(recipe_id):
    try:
        recipe_uuid = uuid.UUID(recipe_id)
    except ValueError:
        raise InvalidUUIDError("ID must be in uuid format")
    deleted = Recipe.query.filter_by(id=recipe_uuid).delete()
    db.session.commit()
    if deleted > 0:
        return {"success": True}
    else:
        raise NotFoundError(f"Recipe with ID: {recipe_id} not found")


def create_recipe(data):
    if not data:
        raise EmptyBodyError("No json data provided")
    try:
        name = data.get("name")
        description = data.get("description")
    except:
        raise JsonParseError("Exception when deserializing data")
    try:
        new_recipe = Recipe(name, description)
        db.session.add(new_recipe)
        db.session.commit()
    except:
        raise DatabaseError("Exception when creating object in database")

    return new_recipe.to_dict()