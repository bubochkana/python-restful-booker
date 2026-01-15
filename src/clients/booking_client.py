from src.endpoints.booking.auth_endpoint import AuthEndpoint
from src.endpoints.booking.booking_endpoint import BookingEndpoint
from src.utils.env_loader import EnvLoader


class BookingClient:
    def __init__(self):
        self.config = EnvLoader().booking_config

        self._auth_endpoint = AuthEndpoint(
            self.config.host, self.config.username, self.config.password)

    def auth_endpoint(self) -> AuthEndpoint:
        return self._auth_endpoint

    def booking_endpoint(self) -> BookingEndpoint:
        return BookingEndpoint(self.config.host, auth_endpoint=self._auth_endpoint)
