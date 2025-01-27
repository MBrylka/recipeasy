import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    UPLOAD_FOLDER_RELATIVE = "uploads/images"
    UPLOAD_FOLDER = os.path.join(basedir,"app/static/dist", UPLOAD_FOLDER_RELATIVE)
    ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg"}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1025 # 16 MB


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "dev.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
