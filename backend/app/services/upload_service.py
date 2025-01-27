import uuid
from ..exceptions import DatabaseError, InvalidUUIDError, NotFoundError
from ..models import Image
from ..utils.file_utils import save_file
from ..extensions import db

def save_recipe_image(file, recipe_id):
    try:
        filepath = save_file(file)
    except ValueError as err:
        raise ValueError(str(err)) 
    try:
        print(type(Image))
        new_image = Image(recipe_id, filepath)
        db.session.add(new_image)
        db.session.commit()
    except Exception as err:
        print(str(err))
        raise DatabaseError("Exception when creating object in database")


def get_image_path(recipe_id):
    try:
        recipe_uuid = uuid.UUID(recipe_id)
    except ValueError:
        raise InvalidUUIDError("ID must be in uuid format")
    image = Image.query.filter_by(recipe_id=recipe_uuid).first()
    if not image:
        raise NotFoundError(f"Image not found for recipe ID: {recipe_id}")
    
    return image.to_dict()

def get_all_images():
    images = Image.query.all()
    return [image.to_dict() for image in images]

def delete_image_by_id(image_id):
    try:
        image_uuid = uuid.UUID(image_id)
    except ValueError:
        raise InvalidUUIDError("ID must be in uuid format")
    deleted = Image.query.filter_by(id=image_uuid).delete()
    db.session.commit()
    if deleted > 0:
        return {"success": True}
    else:
        raise NotFoundError(f"Image with ID: {image_id} not found")