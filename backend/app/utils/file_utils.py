import os
import uuid
from werkzeug.utils import secure_filename
from flask import current_app

def allowed_file(filename):
    allowed_extensions = current_app.config["ALLOWED_IMAGE_EXTENSIONS"]
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_extensions

def save_file(file):
    if not allowed_file(file.filename):
        raise ValueError("File type not allowed")
    generated_filename = f"{uuid.uuid4()}.{file.filename.rsplit(".", 1)[1].lower()}"
    filename = secure_filename(generated_filename)
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    relative_upload_folder = current_app.config["UPLOAD_FOLDER_RELATIVE"]
    os.makedirs(upload_folder, exist_ok=True)
    filepath = os.path.join(upload_folder, filename)
    file.save(filepath)
    return os.path.join(relative_upload_folder,filename)