from app import create_app
from config import DevelopmentConfig, TestingConfig

env = "development"  # TODO: get from env variable

if __name__ == "__main__":
    if env == "development":
        app = create_app(DevelopmentConfig)
    if env == "testing":
        app = create_app(TestingConfig)

    app.run()
