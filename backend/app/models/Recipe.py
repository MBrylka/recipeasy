import sqlalchemy
from db.ext.declarative import declarative_base
from Ingredient import Ingredient

Base = declarative_base()


class Recipe(Base):
    __tablename__ = "recipes"
    id = db.Column(db.UUID, primary_key=True)
    name = db.Column(db.String(length=100))
    description = db.Column(db.String(255))
    ingredients = db.Column(db.ARRAY(Ingredient))
