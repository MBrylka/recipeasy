from flask import Blueprint
from flask import request

from ..exceptions import DatabaseError, InvalidUUIDError, NotFoundError
from ..services.upload_service import delete_image_by_id, get_all_images, get_image_path, save_recipe_image

upload_blueprint = Blueprint("upload", __name__)

@upload_blueprint.route("/recipe-image/<string:recipe_id>", methods=["POST"])
def upload_recipe_image(recipe_id):
    if "file" not in request.files:
        return {'error': 'No file part'}, 400
    file = request.files['file']
    try:
        save_recipe_image(file, recipe_id)
    except ValueError as err:
        return {"error": str(err)}, 400
    except DatabaseError as err:
        return {"error": str(err)}, 400
    
    return {"message": "file saved"}, 200

    
@upload_blueprint.route("/recipe-image/<string:recipe_id>", methods=["GET"])
def get_image_path_for_recipe(recipe_id):
    try:
        path = get_image_path(recipe_id)
        return path, 200
    except InvalidUUIDError as err:
        return {"error": str(err)}, 400
    except NotFoundError as err:
        return {"error": str(err)}, 404

@upload_blueprint.route("/recipe-image", methods=["GET"])
def get_all_image_paths():
    images = get_all_images()
    return {"recipes": images}, 200



@upload_blueprint.route("/recipe-image/<string:image_id>", methods=["DELETE"])
def remove_image(image_id):
    try:
        result = delete_image_by_id(image_id)
        return result, 200
    except InvalidUUIDError as err:
        return {"error": str(err)}, 400
    except NotFoundError as err:
        return {"error": str(err)}, 404