import requests
from core.utils.booker_config_parser import get_auth_url, get_username, get_password


class AuthClient:
    AUTH_URL = get_auth_url()
    USERNAME = get_username()
    PASSWORD = get_password()

    def get_token(self):
        headers = {"Content-Type": "application/json"}
        body = {
            "username": self.USERNAME,
            "password": self.PASSWORD
        }
        response = requests.post(self.AUTH_URL, json=body, headers=headers)
        return response.json()['token']
