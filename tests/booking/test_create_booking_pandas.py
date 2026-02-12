import json
from pathlib import Path

from src.actions.booking_actions import BookingActions
from src.common.common_paths import CommonPaths

from src.db.booking.booking_table import BookingTable
from src.models.bookings.booking_model import BookingDatesModel, BookingModel


class TestCreateBookingDB:
    def test_create_booking_pandas(self, connect_to_db):
        existing_in_db_booking_ids = [1,2,3,4]
        booking_table = BookingTable(connect_to_db)

        data = json.loads(Path(
            CommonPaths.project_root().joinpath("tests").joinpath("resources")
            .joinpath("booking_api_response.json")).read_text())
        expected_booking_api_response = BookingModel.model_validate(data)

        actual_result_as_booking_db_model = booking_table.get_all()
        df = booking_table.as_data_frame(actual_result_as_booking_db_model)

        actual_result_as_booking_model = BookingModel(firstName=actual_result_as_booking_db_model.firstname,
                                                      lastName=actual_result_as_booking_db_model.lastname,
                                                      totalPrice=actual_result_as_booking_db_model.totalprice,
                                                      depositPaid=actual_result_as_booking_db_model.depositpaid,
                                                      bookingDates=BookingDatesModel(
                                                          checkIn=actual_result_as_booking_db_model.checkin,
                                                          checkOut=actual_result_as_booking_db_model.checkout),
                                                      additionalNeeds=actual_result_as_booking_db_model.additionalneeds)

        BookingActions().assert_comparison_results(expected_booking_api_response, actual_result_as_booking_model)

