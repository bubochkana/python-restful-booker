from src.common.common_paths import CommonPaths
from src.endpoints.booking.auth_endpoint import AuthEndpoint
from src.endpoints.booking.booking_endpoint import BookingEndpoint
from src.utils.env_loader import EnvLoader


class BookingClient:
    def __init__(self):
        env = EnvLoader(CommonPaths.env_booking_config_path()).booking_config

        self.host = str(env.host)
        self.username = env.username
        self.password = env.password

        self._auth_endpoint = AuthEndpoint(
            self.host, self.username, self.password)

    def get_auth_endpoint(self) -> AuthEndpoint:
        return self._auth_endpoint

    def get_booking_endpoint(self) -> BookingEndpoint:
        return BookingEndpoint(self.host, auth_endpoint=self._auth_endpoint)
