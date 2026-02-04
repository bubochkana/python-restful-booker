"""Booking client module.

This module provides a client facade for accessing booking-related API
endpoints.
"""
from requests import Session

from src.clients.booking.endpoints.auth_endpoint import AuthEndpoint
from src.clients.booking.endpoints.booking_endpoint import BookingEndpoint
from src.clients.common.base_client import AbstractionClient


class BookingClient(AbstractionClient):
    """Client facade for booking-related API endpoints.

    This class acts as an entry point for interacting with the booking system.
    It initializes configuration, authentication, and provides access to
    booking-related endpoints.
    """

    def __init__(self, session: Session = None):
        """Initialize the BookingClient.

        Loads booking configuration from the environment and initializes
        the authentication endpoint using configured credentials.
        """
        super().__init__(client_config="booking_config")

        self._session = session or AuthEndpoint(self.config)

    def booking_endpoint(self) -> BookingEndpoint:
        """Return the booking endpoint.

        Returns:
            BookingEndpoint: A booking endpoint configured with authentication.
        """
        return BookingEndpoint(host=self.config.host, session=self._session)
