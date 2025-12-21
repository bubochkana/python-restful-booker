import requests
from src.utils.booker_config_parser import ConfigurationParser


class AuthClient:

    def __init__(self):
        self.host = ConfigurationParser().get_restful_booker_api_url()

    username = ConfigurationParser().get_username()
    password = ConfigurationParser().get_password()

    def get_token(self):
        headers = {"Content-Type": "application/json"}
        body = {
            "username": self.username,
            "password": self.password
        }
        response = requests.post(f"{self.host}/auth", json=body, headers=headers)
        return response.json()['token']
