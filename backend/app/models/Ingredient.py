import uuid
from ..extensions import db
from sqlalchemy_serializer import SerializerMixin


class Ingredient(db.Model, SerializerMixin):
    __tablename__ = "ingredients"
    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=False)
    recipes = db.relationship("RecipeIngredient", back_populates="ingredient")

    def __init__(self, name) -> None:
        self.name = name
