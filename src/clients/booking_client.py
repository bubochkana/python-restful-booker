from src.endpoints.booking.auth_endpoint import AuthEndpoint
from src.endpoints.booking.booking_endpoint import BookingEndpoint
from src.utils.env_loader import EnvLoader


class BookingClient:
    def __init__(self):
        env = EnvLoader().config

        self.host = str(env.restful_booker_url)
        self.username = env.username
        self.password = env.password

    def get_auth_endpoint(self) -> AuthEndpoint:
        return AuthEndpoint(self.host, self.username, self.password)

    def get_booking_endpoint(self) -> BookingEndpoint:
        return BookingEndpoint(self.host)
