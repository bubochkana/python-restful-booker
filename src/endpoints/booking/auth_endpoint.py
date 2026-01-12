import requests


class AuthEndpoint:
    def __init__(self, host: str, username: str, password: str):
        self.host = host
        self.username = username
        self.password = password

    def get_token(self) -> str:
        headers = {"Content-Type": "application/json"}
        body = {"username": self.username, "password": self.password}
        response = requests.post(
            f"{self.host}/auth", json=body, headers=headers)
        return response.json()["token"]
