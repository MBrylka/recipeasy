import sqlalchemy
from app import db


class Ingredient(db.Model):
    __tablename__ = "ingredients"
    id = db.Column(db.UUID, primary_key=True)
    name = db.Column(db.String(100))
