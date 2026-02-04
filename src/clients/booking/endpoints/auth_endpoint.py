from requests import Session, Request, PreparedRequest

from src.configs.booking_config_model import BookingEnvironmentConfig


class AuthEndpoint(Session):
    def __init__(self, config: BookingEnvironmentConfig):
        super().__init__()

        self._host = config.host
        self._username = config.username
        self._password = config.password
        self._token = None
        self._auth_url = f"{self._host}/auth"

    def _generate_token(self) -> str:
        s = Session()
        s.headers = {"Content-Type": "application/json"}
        s.body = {"username": self._username, "password": self._password}

        response = s.request(
            method = "POST",
            url = self._auth_url,
            json=s.body,
            headers=s.headers
        )

        self._token = response.json()["token"]

        return self._token

    def prepare_request(self, request: Request) -> PreparedRequest:
        prepared_request = PreparedRequest()
        return prepared_request

