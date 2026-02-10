"""Booking client module.

This module provides a client facade for accessing booking-related API
endpoints.
"""

from src.clients.booking.endpoints.booking_endpoint import BookingEndpoint
from src.clients.common.base_client import AbstractionClient


class BookingClient(AbstractionClient):
    """Client facade for booking-related API endpoints.

    This class acts as an entry point for interacting with the booking system.
    It initializes configuration, authentication, and provides access to
    booking-related endpoints.
    """

    def __init__(self):
        """Initialize the booking client.

        Loads booking-related configuration and prepares the client for
        accessing booking API endpoints. Configuration is resolved via the
        underlying ``AbstractionClient`` using the ``booking_config`` profile.
        """
        super().__init__(client_config='booking_config')

    def booking_endpoint(self) -> BookingEndpoint:
        """Create and return a booking endpoint instance.

        The returned endpoint is configured with booking environment settings
        and an authenticated session, enabling interaction with booking-related
        API operations.

        Returns:
            BookingEndpoint: An initialized booking endpoint client.
        """
        return BookingEndpoint(config=self.config)
