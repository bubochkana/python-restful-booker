import json
from pathlib import Path

from src.actions.booking_actions import BookingActions
from src.common.common_paths import CommonPaths
from src.db.booking.booking_table import BookingTable
from src.models.bookings.booking_model import BookingDatesModel, BookingModel


class TestCreateBookingDB:
    def test_create_booking_sql_alchemy(self, connect_to_db_sql_alchemy):
        existing_in_db_booking_id = 1
        booking_table = BookingTable(connect_to_db_sql_alchemy)

        data = json.loads(Path(
            CommonPaths.project_root().joinpath("tests").joinpath("resources")
            .joinpath("booking_api_response.json")).read_text())[0]
        expected_booking_api_response = BookingModel.model_validate(data)

        actual_result_as_booking_db_model = booking_table.get_by_id(existing_in_db_booking_id)
        actual_result_as_booking_model = BookingModel(firstName=actual_result_as_booking_db_model.firstname,
                                                      lastName=actual_result_as_booking_db_model.lastname,
                                                      totalPrice=actual_result_as_booking_db_model.totalprice,
                                                      depositPaid=actual_result_as_booking_db_model.depositpaid,
                                                      bookingDates=BookingDatesModel(
                                                          checkIn=actual_result_as_booking_db_model.checkin,
                                                          checkOut=actual_result_as_booking_db_model.checkout),
                                                      additionalNeeds=actual_result_as_booking_db_model.additionalneeds)

        BookingActions().assert_comparison_results(expected_booking_api_response, actual_result_as_booking_model)


    def test_create_booking_cursor(self, connect_to_db_cursor):
        existing_in_db_booking_id = 1

        data = json.loads(Path(
            CommonPaths.project_root().joinpath("tests").joinpath("resources")
            .joinpath("booking_api_response.json")).read_text())[0]
        expected_booking_api_response = BookingModel.model_validate(data)

        actual_db_result_db_model = connect_to_db_cursor.execute(f'SELECT * FROM booking WHERE bookingid={existing_in_db_booking_id}')
        row = actual_db_result_db_model.fetchone()

        actual_result_as_booking_model = BookingModel(
            firstName=row[1],
            lastName=row[2],
            totalPrice=row[3],
            depositPaid=row[4],
            bookingDates=BookingDatesModel(
                checkIn=row[5],
                checkOut=row[6]),
            additionalNeeds=row[7])

        BookingActions().assert_comparison_results(expected_booking_api_response,
                                                   actual_result_as_booking_model)


