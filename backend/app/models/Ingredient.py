import uuid
from ..extensions import db
from sqlalchemy_serializer import SerializerMixin


class Ingredient(db.Model, SerializerMixin):
    __tablename__ = "ingredients"
    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=False)
    makro_calories = db.Column(db.Float, default=0.0)
    makro_carbs = db.Column(db.Float, default=0.0)
    makro_protein = db.Column(db.Float, default=0.0)
    makro_fat = db.Column(db.Float, default=0.0)
    base_unit = db.Column(db.String(10), nullable=False, default="g") #'g', 'ml', or 'pcs'
    density = db.Column(db.Float, nullable=True)
    weight_per_piece = db.Column(db.Float, nullable=True)

    def __init__(self, name, calories, carbs, protein, fat, base_unit="g", density=None, weight_per_piece=None) -> None:
        self.name = name
        self.makro_calories = calories
        self.makro_carbs = carbs
        self.makro_protein = protein
        self.makro_fat = fat
        self.base_unit = base_unit
        self.density = density
        self.weight_per_piece = weight_per_piece
