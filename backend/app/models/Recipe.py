from ..extensions import db
from .Ingredient import Ingredient


class Recipe(db.Model):
    __tablename__ = "recipes"
    id = db.Column(db.UUID, primary_key=True)
    name = db.Column(db.String(length=100))
    description = db.Column(db.String(255))
    ingredients = db.Column(db.ARRAY(Ingredient))
