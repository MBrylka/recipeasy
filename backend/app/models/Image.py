import uuid
from ..extensions import db
from sqlalchemy_serializer import SerializerMixin


class Image(db.Model, SerializerMixin):
    __tablename__ = "images"
    
    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    recipe_id = db.Column(db.UUID, db.ForeignKey("recipes.id"))
    filepath = db.Column(db.String(100), nullable=False)

    def __init__(self, recipe_id, filepath) -> None:
        self.recipe_id = uuid.UUID(recipe_id)
        self.filepath = filepath
