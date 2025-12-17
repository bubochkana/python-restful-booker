import requests
from assertpy import assert_that


class TestCreateBooking:
    def test_create_booking(self, booking_client, booking_helper):

        response = booking_client.create_booking(booking_helper.BODY)

        # TODO - not sure how to make an assert here using the model
        assert_that(response.status_code).is_equal_to(requests.codes.ok)

    # TODO - find a way to write a test when one of the required fields is missing
    # @pytest.mark.parametrize("case_id, remove, remove_nested", [
    #     ("missing_firstname", ["firstName"], []),
    #     ("missing_checkout", [], [("bookingDates", "checkOut")]),
    #     ("missing_totalprice_and_depositpaid", ["totalPrice", "depositPaid"], [])
    # ])
    # def test_create_booking_no_req_fields(self, case_id, remove, remove_nested,
    #                                       booking_client, booking_helper):
    #     body = booking_helper.make_body(remove=remove, remove_nested=remove_nested)
    #
    #     response = booking_client.create_booking(body)
    #     assert response.status_code == 500
