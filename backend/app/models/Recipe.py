import uuid
from ..extensions import db
from sqlalchemy_serializer import SerializerMixin


class Recipe(db.Model, SerializerMixin):
    __tablename__ = "recipes"
    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(length=100))
    description = db.Column(db.String(255))
    ingredients = db.relationship("RecipeIngredient", back_populates="recipe")

    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
