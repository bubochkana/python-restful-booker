import requests
from src.utils.booker_config_parser import get_username, get_password
from src.utils.booker_config_parser import get_restful_booker_api_url


class AuthClient:

    def __init__(self):
        self.host = get_restful_booker_api_url()

    USERNAME = get_username()
    PASSWORD = get_password()

    def get_token(self):
        headers = {"Content-Type": "application/json"}
        body = {
            "username": self.USERNAME,
            "password": self.PASSWORD
        }
        response = requests.post(f"{self.host}/auth", json=body, headers=headers)
        return response.json()['token']
