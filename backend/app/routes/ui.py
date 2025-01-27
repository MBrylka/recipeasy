from flask import Blueprint, send_from_directory
import os

static_path = os.path.join(os.path.dirname(__file__), '../static/dist')
ui_blueprint = Blueprint("ui", __name__, static_folder=static_path)

@ui_blueprint.route("/", defaults={"path":""})
@ui_blueprint.route("/<path:path>")
def serve_vue(path):
    if path and os.path.exists(os.path.join(ui_blueprint.static_folder, path)):
        print("IMAGE EXISTS")
        # If the requested file exists, serve it
        return send_from_directory(ui_blueprint.static_folder, path)
    # For any other path, serve index.html
    return send_from_directory(ui_blueprint.static_folder, 'index.html')