"""Booking API endpoint client.

This module defines a high-level client for interacting with booking-related
API endpoints. It provides methods for creating, retrieving, updating, and
deleting bookings, and relies on a shared HTTP session supplied by the
``AbstractionEndpoint`` base class.

The endpoint implementation is designed to be used by a client facade and
supports both positive and negative test scenarios by allowing custom request
payloads and headers to be passed through to the underlying HTTP layer.
"""
from typing import Any, Dict, Union

from requests import Response, Session

from src.clients.booking.endpoints.auth_endpoint import AuthEndpoint
from src.clients.common.base_endpoint import AbstractionEndpoint
from src.configs.booking_config_model import BookingEnvironmentConfig
from src.models.bookings.booking_model import BookingModel


class BookingEndpoint(AbstractionEndpoint):
    """API endpoint client for booking-related operations.

    This class provides high-level methods for interacting with the booking
    API, including creating, retrieving, updating, and deleting bookings.
    All HTTP requests are executed through the shared session provided by
    the base ``AbstractionEndpoint`` class.
    """

    def __init__(self, config: BookingEnvironmentConfig, session: Session = None):
        """Initialize the booking endpoint.

        Creates a booking endpoint bound to the configured API host and
        initializes the HTTP session used for request execution. If no
        custom session is provided, an authenticated session
        (``AuthEndpoint``) is created automatically using the supplied
        environment configuration.

        This design allows endpoints that require authentication to
        transparently manage auth while still supporting dependency
        injection for negative test scenarios or custom session behavior.

        Args:
            config: Booking environment configuration containing the API
                host and authentication credentials.
            session: Optional custom HTTP session to use for request
                execution. If not provided, an authenticated session is
                initialized internally.
        """
        self.host = config.host
        auth_session = session or AuthEndpoint(config)
        super().__init__(session=auth_session)

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

    def create_booking(self, body: Union[BookingModel, Dict[str, Any]]) -> Response:
        """Create a new booking.

        Args:
        body: BookingModel (happy path) or dict payload (negative tests).

        Returns:
        Response: HTTP response containing created booking information.
        """
        payload = body.model_dump(mode="json") if hasattr(body, "model_dump") else body
        return self.post(f"{self.host}/booking", json=payload)

    def update_booking(self, booking_id, body, headers=None) -> Response:
        """Update an existing booking by its unique identifier.

        Sends a PUT request to the booking API to update the booking data.
        Optional HTTP headers may be provided to customize the request
        (for example, to override authentication behavior in negative tests).

        Args:
            booking_id: Unique identifier of the booking to update.
            body: BookingModel instance containing updated booking data.
            headers: Optional dictionary of HTTP headers to include in the request.

        Returns:
            Response: HTTP response returned by the update operation.
        """
        return self.put(f"{self.host}/booking/{booking_id}", json=body.model_dump(), headers=headers)

    def delete_booking(self, booking_id, headers=None) -> Response:
        """Delete a booking by its unique identifier.

        Sends a DELETE request to the booking API to remove the specified booking.
        Optional HTTP headers may be provided to customize the request
        (for example, to omit authentication headers in negative test scenarios).

        Args:
            booking_id: Unique identifier of the booking to delete.
            headers: Optional dictionary of HTTP headers to include in the request.

        Returns:
            Response: HTTP response returned by the delete operation.
        """
        return self.delete(f"{self.host}/booking/{booking_id}", headers=headers)


