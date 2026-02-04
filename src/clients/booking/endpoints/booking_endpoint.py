from typing import Any, Dict, Union

from requests import Response

from src.clients.common.base_endpoint import AbstractionEndpoint
from src.models.bookings.booking_model import BookingModel


class BookingEndpoint(AbstractionEndpoint):

    def __init__(self, host: str, session):
        super().__init__(session=session)

        self.host = host

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
        # token = self.auth_endpoint.get_token()
        # default_headers = {"Content-Type": "application/json", "Accept": "application/json", "Cookie": f"token={token}"}
        #
        # final_headers = default_headers if headers is None else headers

        return self.put(f"{self.host}/booking/{booking_id}", json=body.model_dump(), headers=headers)

    def delete_booking(self, booking_id, headers=None) -> Response:
        # default_headers = {"Content-Type": "application/json", "Cookie": f"token={token}"}
        #
        # final_headers = default_headers if headers is None else headers

        return self.delete(f"{self.host}/booking/{booking_id}", headers=headers)


