import requests
from src.configs.settings_management_model import Settings


class AuthClient:

    def __init__(self):
        self.host = Settings().url

    username = Settings().username
    password = Settings().password

    def get_token(self):
        headers = {"Content-Type": "application/json"}
        body = {
            "username": self.username,
            "password": self.password
        }
        response = requests.post(f"{self.host}/auth", json=body, headers=headers)
        return response.json()['token']
