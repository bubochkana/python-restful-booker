import json
from pathlib import Path

from src.actions.booking_actions import BookingActions
from src.common.common_paths import CommonPaths
from src.common.sql_alchemy_query_manager import SqlAlchemyQueryManager
from src.models.bookings.booking_model import CreateBookingResponse, BookingDatesModel, BookingModel


class TestCreateBookingDB:
    def test_create_booking_db(self, connect_to_db):
        sql_manager = SqlAlchemyQueryManager(connect_to_db)
        existing_in_db_booking_id = 1

        data = json.loads(Path(
            CommonPaths.project_root().joinpath("tests").joinpath("resources")
            .joinpath("booking_api_response.json")).read_text())
        expected_booking_api_response = BookingModel.model_validate(data)

        actual_result_as_booking_db_model = sql_manager.select_booking(existing_in_db_booking_id)
        actual_result_as_booking_model = BookingModel(firstName=actual_result_as_booking_db_model.firstname,
                                                      lastName=actual_result_as_booking_db_model.lastname,
                                                      totalPrice=actual_result_as_booking_db_model.totalprice,
                                                      depositPaid=actual_result_as_booking_db_model.depositpaid,
                                                      bookingDates=BookingDatesModel(
                                                          checkIn=actual_result_as_booking_db_model.checkin,
                                                          checkOut=actual_result_as_booking_db_model.checkout),
                                                      additionalNeeds=actual_result_as_booking_db_model.additionalneeds)

        BookingActions().assert_comparison_results(expected_booking_api_response, actual_result_as_booking_model)