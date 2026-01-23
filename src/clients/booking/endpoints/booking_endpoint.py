"""Booking endpoint client.

This module provides an API client for interacting with booking-related
endpoints, including creating, retrieving, updating, and deleting
bookings, as well as generating random booking test data.
"""


from requests import Response

from src.clients.common.base_endpoint import AbstractionEndpoint
from src.models.bookings.booking_model import BookingModel


class BookingEndpoint(AbstractionEndpoint):
    """Client for booking-related API operations.

    This class encapsulates HTTP interactions with the booking service,
    including CRUD operations and helper methods for generating
    booking-related test data.
    """

    def __init__(self, host: str, auth_endpoint=None):
        """Initialize the BookingEndpoint.

        Args:
            host: Base URL of the booking service.
            auth_endpoint: Authentication endpoint used to retrieve
                authorization tokens for protected operations.
        """
        super().__init__()

        self.host = host
        self.auth_endpoint = auth_endpoint

    def get_all_bookings(
        self,
        firstName: str = None,
        lastName: str = None,
        checkin: str = None,
        checkout: str = None,
    ) -> Response:
        """Retrieve all bookings with optional filtering.

        Args:
            firstName: Filter bookings by first name.
            lastName: Filter bookings by last name.
            checkin: Filter bookings by check-in date (YYYY-MM-DD).
            checkout: Filter bookings by checkout date (YYYY-MM-DD).

        Returns:
            Response: HTTP response containing a list of booking IDs.
        """
        params = {"firstName": firstName, "lastName": lastName, "checkin": checkin, "checkout": checkout}

        params = {key: value for key, value in params.items() if value is not None}

        return self.get(f"{self.host}/booking", params=params)

    def get_booking_by_id(self, booking_id) -> Response:
        """Retrieve a booking by its identifier.

        Args:
            booking_id: Unique identifier of the booking.

        Returns:
            Response: HTTP response containing booking details.
        """
        return self.get(f"{self.host}/booking/{booking_id}")

    def create_booking(self, body: BookingModel) -> Response:
        """Create a new booking.

        Args:
            body: Booking model containing booking details.

        Returns:
            Response: HTTP response containing created booking information.
        """
        return self.post(f"{self.host}/booking", json=body.model_dump())

    def update_booking(self, booking_id, body, headers=None) -> Response:
        """Update an existing booking.

        Args:
            booking_id: Unique identifier of the booking.
            body: The booking model to user for update.
            headers: Optional custom HTTP headers. If not provided,
                the default authorization headers will be used.

        Returns:
            Response: HTTP response containing updated booking information.
        """
        token = self.auth_endpoint.get_token()
        default_headers = {"Content-Type": "application/json", "Accept": "application/json", "Cookie": f"token={token}"}

        final_headers = default_headers if headers is None else headers

        return self.put(f"{self.host}/booking/{booking_id}", json=body.model_dump(), headers=final_headers)

    def delete_booking(self, booking_id, headers=None) -> Response:
        """Delete a booking.

        Args:
            booking_id: Unique identifier of the booking.
            headers: Optional custom HTTP headers. If not provided,
                the default authorization headers will be used.

        Returns:
            Response: HTTP response indicating deletion status.
        """
        token = self.auth_endpoint.get_token()
        default_headers = {"Content-Type": "application/json", "Cookie": f"token={token}"}

        final_headers = default_headers if headers is None else headers

        return self.delete(f"{self.host}/booking/{booking_id}", headers=final_headers)


