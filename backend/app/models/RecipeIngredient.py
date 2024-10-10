import uuid
from ..extensions import db
from dataclasses import dataclass


@dataclass
class RecipeIngredient(db.Model):
    __tablename__ = "recipe_ingredients"

    recipe_id = db.Column(db.UUID, db.ForeignKey("recipes.id"), primary_key=True)
    ingredient_id = db.Column(
        db.UUID, db.ForeignKey("ingredients.id"), primary_key=True
    )
    quantity = db.Column(
        db.Float, nullable=False
    )  # Quantity for that ingredient in the recipe

    # Relationships
    recipe = db.relationship("Recipe", back_populates="ingredients")
    ingredient = db.relationship("Ingredient", back_populates="recipes")
