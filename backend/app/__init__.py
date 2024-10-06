from flask import Flask


def create_app():
    app = Flask(__name__, static_folder="../../frontend/dist")

    # Serve vue app and static files

    @app.route("/")
    def serve_vue():
        return app.send_static_file("index.html")

    @app.route("/<path:filename>")
    def serve_static(filename):
        return app.send_static_file(filename)

    return app
