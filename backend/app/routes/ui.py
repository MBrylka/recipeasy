from flask import Blueprint, send_from_directory
import os
ui_blueprint = Blueprint("ui", __name__)

# NOTE
# send_from_directory takes relative path from the __init__.py file from the app directory


DIST_DIR = os.path.join(os.path.dirname(__file__), "../../../frontend/dist")

@ui_blueprint.route("/")
@ui_blueprint.route("/<path:subpath>")
def serve_vue(subpath=None):
    print("Serving static files from:", DIST_DIR)
    print("Does index.html exist?", os.path.exists(os.path.join(DIST_DIR, "index.html")))

    try:
        return send_from_directory(DIST_DIR, "index.html")
    except FileNotFoundError:
        return "index.html not found", 404


@ui_blueprint.route("/<path:filename>")
def serve_static(filename):
    try:
        return send_from_directory(DIST_DIR, filename)
    except FileNotFoundError:
        return f"{filename} not found", 404
