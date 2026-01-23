"""Action layer for Booking API test operations.

This module contains high-level, reusable actions for interacting with
the Booking API. It abstracts low-level endpoint calls, handles response
validation, and returns strongly-typed domain models to keep test cases
concise and focused on assertions.
"""
import logging
import random

from assertpy import assert_that
from faker import Faker
from requests import Response

from src.clients.booking.booking_client import BookingClient
from src.helpers.compare_models import CompareModel
from src.models.bookings.booking_model import BookingDatesModel, BookingIdModel, BookingModel, CreateBookingResponse


class BookingActions:
    """High-level action layer for Booking API operations.

    This class provides reusable, test-oriented actions for interacting
    with the Booking API, such as creating, retrieving, updating, and
    deleting bookings. It abstracts low-level endpoint calls and
    response handling, returning strongly-typed domain models and
    performing automatic response validation.

    The class is intended to be used by test cases to keep test logic
    concise and focused on assertions rather than API mechanics.
    """

    def __init__(self):
        """Initialize BookingActions with a booking client and endpoint.

        Creates an instance of ``BookingClient`` and resolves the
        corresponding booking endpoint for performing API requests.
        """
        self.booking_client = BookingClient()
        self.booking_endpoint = self.booking_client.booking_endpoint()

    def get_booking(self, booking_id) -> BookingModel:
        """Retrieve a booking by its identifier.

        Sends a request to fetch a booking by ID, validates the response
        status code, and converts the response payload into a
        ``BookingModel``.

        Args:
            booking_id: Identifier of the booking to retrieve.

        Returns:
            BookingModel: The retrieved booking represented as a domain model.

        Raises:
            Exception: If the response status code is not 200.
        """
        logging.info("Getting a booking")

        response: Response = self.booking_endpoint.get_booking_by_id(booking_id)
        if response.status_code != 200:
            raise Exception(f"Expected status code 200, but got {response.status_code}")

        booking_as_model = BookingModel(**response.json())

        return booking_as_model

    def get_bookings(self) -> BookingIdModel:
        """Retrieve all booking identifiers.

        Sends a request to fetch all existing bookings and converts the
        response payload into a ``BookingIdModel``.

        Returns:
            BookingIdModel: Model containing booking identifiers.

        Raises:
            Exception: If the response status code is not 200.
        """
        logging.info("Getting a booking")

        response: Response = self.booking_endpoint.get_all_bookings()
        if response.status_code != 200:
            raise Exception(f"Expected status code 200, but got {response.status_code}")

        all_bookings_as_model = BookingIdModel(**response.json())

        return all_bookings_as_model

    def create_booking(self, post_model: BookingModel = None) -> CreateBookingResponse:
        """Create a new booking.

        Sends a request to create a booking using the provided booking
        model. If no model is provided, a random booking model is
        generated automatically. The created booking is validated by
        comparing the request payload with the response payload.

        Args:
            post_model: Optional booking model to use for creation.
                If not provided, a random booking model is generated.

        Returns:
            CreateBookingResponse: Response model containing the created
            booking and its identifier.

        Raises:
            Exception: If the response status code is not 200.
            AssertionError: If the created booking does not match the
            request payload.
        """
        logging.info("Creating a new booking")

        if post_model is None:
            post_model = self.build_random_booking()

        response: Response = self.booking_endpoint.create_booking(post_model)
        if response.status_code != 200:
            raise Exception(f"Expected status code 200, but got {response.status_code}")

        created_booking_as_model = CreateBookingResponse(**response.json())

        comparison_results = CompareModel().compare_values(
            post_model.model_dump(), created_booking_as_model.booking.model_dump()
        )
        assert_that(comparison_results,
                    f"Following differences found: {comparison_results}").is_empty()

        logging.info("Booking created successfully!")

        return created_booking_as_model

    def update_booking(self, booking_id, put_model: BookingModel = None) -> BookingModel:
        """Update an existing booking.

        Sends a request to update a booking by ID using the provided
        booking model. If no model is provided, a random booking model is
        generated. The updated booking is validated against the request
        payload.

        Args:
            booking_id: Identifier of the booking to update.
            put_model: Optional booking model to use for the update.
                If not provided, a random booking model is generated.

        Returns:
            BookingModel: Updated booking represented as a domain model.

        Raises:
            Exception: If the response status code is not 200.
            AssertionError: If the updated booking does not match the
            request payload.
        """
        logging.info("Updating an existing booking")

        if put_model is None:
            put_model = self.build_random_booking()

        response: Response = self.booking_endpoint.update_booking(booking_id, put_model)
        if response.status_code != 200:
            raise Exception(f"Expected status code 200, but got {response.status_code}")

        updated_booking_as_model = BookingModel(**response.json())

        comparison_results = CompareModel().compare_values(
            put_model.model_dump(), updated_booking_as_model.model_dump()
        )
        assert_that(comparison_results,
                    f"Following differences found: {comparison_results}").is_empty()

        logging.info("Booking updated successfully!")

        return updated_booking_as_model

    def delete_booking(self, booking_id) -> None:
        """Delete an existing booking.

        Sends a request to delete a booking by ID and validates that the
        operation completed successfully.

        Args:
            booking_id: Identifier of the booking to delete.

        Raises:
            Exception: If the response status code is not 201.
        """
        logging.info("Deleting an existing booking")

        response: Response = self.booking_endpoint.delete_booking(booking_id)
        if response.status_code != 201:
            raise Exception(f"Expected status code 201, but got {response.status_code}")

        logging.info("Booking deleted successfully!")


    def build_random_booking(self) -> BookingModel:
        """Build a random booking model for testing purposes.

        Uses Faker to generate realistic random booking data.

        Returns:
            BookingModel: Randomly generated booking model.
        """
        faker: Faker = Faker()
        return BookingModel(
            firstName=faker.first_name(),
            lastName=faker.last_name(),
            totalPrice=faker.random_int(min=1, max=500),
            depositPaid=faker.boolean(),
            bookingDates=BookingDatesModel(
                checkIn=faker.date(pattern="%Y-%m-%d"), checkOut=faker.date(pattern="%Y-%m-%d")
            ),
            additionalNeeds=faker.name(),
        )

    def pick_random_booking_id(self) -> str:
        """Pick a random booking ID from existing bookings.

        Returns:
            str: Randomly selected booking identifier.
        """
        booking_ids_list = self.booking_endpoint.get_all_bookings()
        my_obj_list: list[BookingIdModel] = [BookingIdModel(**dict_item) for dict_item in booking_ids_list.json()]
        return str(random.choice(my_obj_list).bookingid)