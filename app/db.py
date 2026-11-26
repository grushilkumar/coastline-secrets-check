"""Opens the settlement database connection from the settings and the environment."""
import os

import yaml


def connection_settings(path: str = "config/settings.yaml") -> dict:
    db = yaml.safe_load(open(path))["database"]
    return {
        "host": os.environ[db["host_env"]],
        "port": int(os.environ[db["port_env"]]),
        "user": os.environ[db["user_env"]],
        "password": os.environ[db["password_env"]],
        "dbname": db["name"],
    }
