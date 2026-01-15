"""Booking client module.

This module provides a client facade for accessing booking-related API
endpoints.
"""

from src.endpoints.booking.auth_endpoint import AuthEndpoint
from src.endpoints.booking.booking_endpoint import BookingEndpoint
from src.utils.env_loader import EnvLoader


class BookingClient:
    """Client facade for booking-related API endpoints.

    This class acts as an entry point for interacting with the booking system.
    It initializes configuration, authentication, and provides access to
    booking-related endpoints.
    """

    def __init__(self):
        """Initialize the BookingClient.

        Loads booking configuration from the environment and initializes
        the authentication endpoint using configured credentials.
        """
        self.config = EnvLoader().booking_config

        self._auth_endpoint = AuthEndpoint(self.config.host, self.config.username, self.config.password)

    def auth_endpoint(self) -> AuthEndpoint:
        """Return the authentication endpoint.

        Returns:
            AuthEndpoint: An initialized authentication endpoint instance.
        """
        return self._auth_endpoint

    def booking_endpoint(self) -> BookingEndpoint:
        """Return the booking endpoint.

        Returns:
            BookingEndpoint: A booking endpoint configured with authentication.
        """
        return BookingEndpoint(self.config.host, auth_endpoint=self._auth_endpoint)
