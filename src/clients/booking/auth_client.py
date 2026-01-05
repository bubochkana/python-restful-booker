import requests

from src.configs.settings_management_model import Settings
from src.common.common_paths import get_qa_env_dir


class AuthClient:
    def __init__(self):
        settings = Settings.read_yaml(get_qa_env_dir().joinpath("qa_config.yaml"))
        self.host = settings.restful_booker_url
        self.username = settings.username
        self.password = settings.password

    def get_token(self):
        headers = {"Content-Type": "application/json"}
        body = {"username": self.username, "password": self.password}
        response = requests.post(f"{self.host}/auth", json=body, headers=headers)
        return response.json()["token"]
