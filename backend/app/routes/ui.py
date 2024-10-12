from flask import Blueprint, send_from_directory

ui_blueprint = Blueprint("ui", __name__)

# NOTE
# send_from_directory takes relative path from the __init__.py file from the app directory


@ui_blueprint.route("/")
def serve_vue():
    return send_from_directory("../../frontend/dist", "index.html")


@ui_blueprint.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory("../../frontend/dist", filename)
