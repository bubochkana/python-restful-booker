import json
from pathlib import Path

import pandas as pd

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
            .joinpath("booking_api_response.json")).read_text())[0]
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

    def test_merge_same_bookings(self):
        data = json.loads(Path(CommonPaths.project_root().joinpath("tests").joinpath("resources").joinpath("booking_api_response.json")).read_text())
        df_booking1 = pd.DataFrame(data[0])
        df_booking2 = pd.DataFrame(data[0])

        merged_bookings = df_booking1.merge(df_booking2, indicator=True, how='outer')
        booking_merge_diff = merged_bookings.loc[lambda x: x['_merge'] != 'both']
        print(booking_merge_diff)

    def test_merge_different_bookings(self):
        #data = json.loads(Path(CommonPaths.project_root().joinpath("tests").joinpath("resources").joinpath("booking_api_response_no_dates.json")).read_text())
        data1 = [
            {'account': 'Jones LLC', 'Jan': 150, 'Feb': 200, 'Mar': 140},
            {'account': 'Alpha Co', 'Jan': 200, 'Feb': 210, 'Mar': 215},
            {'account': 'Blue Inc', 'Jan': 50, 'Feb': 90, 'Mar': 95},
            {'account': 'Green', 'Jan': 50, 'Feb': 90, 'Mar': 95}
        ]
        data2 = [
            {'account': 'Jones LLC', 'Jan': 200, 'Feb': 200, 'Mar': 140},
            {'account': 'Alpha Co', 'Jan': 200, 'Feb': 210, 'Mar': 215},
            {'account': 'Blue Inc', 'Jan': 50, 'Feb': 90, 'Mar': 95},
            {'account': 'Yellow', 'Jan': 50, 'Feb': 90, 'Mar': 95}
        ]
        df_booking1 = pd.DataFrame(data1)
        df_booking2 = pd.DataFrame(data2)

        on_keys = ["account"]
        merged_bookings = df_booking1.merge(df_booking2, indicator=True, how='outer', on=on_keys, suffixes=("_src", "_tgt"))

        both = merged_bookings[merged_bookings["_merge"] == "both"]
        left_only = merged_bookings[merged_bookings["_merge"] == "left_only"]
        right_only = merged_bookings[merged_bookings["_merge"] == "right_only"]
        both = both.reset_index(drop=True)
        results = []

        for k in on_keys:
            results.append(pd.DataFrame({k: both[k]}))

        columns_to_compare = ["Jan", "Feb", "Mar"]

        for el in columns_to_compare:
            src_column = f'{el}_src'
            tgt_column = f'{el}_tgt'
            src_data = both[src_column]
            tgt_data = both[tgt_column]
            comparison_results = (src_data == tgt_data) | (src_data.isna() & tgt_data.isna()) | (src_data.isnull() & tgt_data.isnull())
            comparison_df = pd.DataFrame({src_column: src_data, tgt_column: tgt_data, f'{el}_valid': comparison_results})
            results.append(comparison_df)
        all_results = pd.concat(results, axis = 1)

        diffs_only = all_results.loc[~all_results[[f'{col}_valid' for col in columns_to_compare]].all(axis=1)]

        print(diffs_only)
        print(right_only)
        print(left_only)



