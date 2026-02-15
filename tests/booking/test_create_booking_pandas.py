import json
from pathlib import Path

from src.actions.booking_actions import BookingActions
from src.common.common_paths import CommonPaths

from src.db.booking.booking_table import BookingTable
from src.models.bookings.booking_model import BookingDatesModel, BookingModel


class TestCreateBookingDB:
    def test_create_booking_pandas(self, connect_to_db_sql_alchemy):
        existing_in_db_booking_id = 1
        booking_table = BookingTable(connect_to_db_sql_alchemy)

        data = json.loads(Path(
            CommonPaths.project_root().joinpath("tests").joinpath("resources")
            .joinpath("booking_api_response.json")).read_text())
        expected_booking_api_response = BookingModel.model_validate(data)

        actual_result_as_df = booking_table.as_data_frame()
        row = actual_result_as_df[actual_result_as_df["bookingid"] == existing_in_db_booking_id].iloc[0]
        actual_result_from_df = BookingModel(firstname=row.firstname,
            lastname=row.lastname,
            totalprice=row.totalprice,
            depositpaid=row.depositpaid,
            bookingdates=BookingDatesModel(
                checkin=row.checkin,
                checkout=row.checkout,
            ),
            additionalneeds=row.additionalneeds)

        BookingActions().assert_comparison_results(expected_booking_api_response, actual_result_from_df)

