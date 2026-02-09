from src.actions.booking_actions import BookingActions
from src.common.sql_alchemy_manager import SqlAlchemyManager
from src.models.bookings.booking_model import CreateBookingResponse, BookingDatesModel, BookingModel


class TestCreateBookingDB:
    def test_create_booking_db(self):
        sql_manager = SqlAlchemyManager()
        existing_in_db_booking_id = 1

        expected_booking = BookingModel(firstName="Gabriella",
                lastName="Soliz",
                totalPrice=300,
                depositPaid=True,
                bookingDates=BookingDatesModel(
                    checkIn="2024-11-25", checkOut="2024-12-07"
                ),
                additionalNeeds="A bed for a child")
        #TODO - compare the model from the API response (hardcoded model, no actual API call was made)
        # and the model received from the DB tabe
        expected_booking_api_response = CreateBookingResponse(existing_in_db_booking_id, expected_booking)

        actual_result_booking_db = sql_manager.select_booking(existing_in_db_booking_id)

        BookingActions().assert_comparison_results(expected_booking_api_response, actual_result_booking_db)