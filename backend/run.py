from app import create_app
from config import DevelopmentConfig, TestingConfig

env = "development"  # TODO: get from env variable

if env == "development":
    app = create_app(DevelopmentConfig)
elif env == "testing":
    app = create_app(TestingConfig)
else:
    raise ValueError("Invalid environment name")
