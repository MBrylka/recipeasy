import uuid
from ..extensions import db
from sqlalchemy_serializer import SerializerMixin


class RecipeIngredient(db.Model, SerializerMixin):
    __tablename__ = "recipe_ingredients"

    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    recipe_id = db.Column(db.UUID, db.ForeignKey("recipes.id"))
    ingredient_id = db.Column(db.UUID, db.ForeignKey("ingredients.id"))
    quantity = db.Column(db.Float, nullable=False)

    def __init__(self, recipe_id, ingredient_id, quantity) -> None:
        self.recipe_id = uuid.UUID(recipe_id)
        self.ingredient_id = uuid.UUID(ingredient_id)
        self.quantity = quantity
