from typing import Optional, Dict, Any, List

import requests

from src.clients.booking.auth_client import AuthClient
from src.configs.settings_management_model import Settings
from src.models.bookings.booking_model import Booking
from src.common.common_paths import get_qa_env_dir


class BookingClient:
    def __init__(self):
        settings = Settings.read_yaml(get_qa_env_dir().joinpath("qa_config.yaml"))
        self.host = settings.restful_booker_url

    def get_all_bookings(
        self,
        firstname: Optional[str] = None,
        lastname: Optional[str] = None,
        checkin: Optional[str] = None,
        checkout: Optional[str] = None,
    ):
        params = {"firstname": firstname, "lastname": lastname, "checkin": checkin, "checkout": checkout}

        params = {key: value for key, value in params.items() if value is not None}

        return requests.get(f"{self.host}/booking", params=params)

    def get_booking_by_id(self, booking_id):
        return requests.get(f"{self.host}/booking/{booking_id}")

    def create_booking(self, body: Booking):
        return requests.post(f"{self.host}/booking", json=body.model_dump())

    def update_booking(self, booking_id, body, headers=None):
        token = AuthClient().get_token()
        default_headers = {"Content-Type": "application/json", "Accept": "application/json", "Cookie": f"token={token}"}

        final_headers = default_headers if headers is None else headers

        return requests.put(f"{self.host}/booking/{booking_id}", json=body.model_dump(), headers=final_headers).json()

    def delete_booking(self, booking_id, headers=None):
        token = AuthClient().get_token()
        default_headers = {"Content-Type": "application/json", "Cookie": f"token={token}"}

        final_headers = default_headers if headers is None else headers

        return requests.delete(f"{self.host}/booking/{booking_id}", headers=final_headers)

    def compare_dicts(self, expected_results: Dict[str, Any], actual_results: Dict[str, Any]):
        """Compare two dictionaries and return a list of differences."""
        comparison_results = []
        for key, value in expected_results.items():
            if key not in actual_results:
                comparison_results.append(f"Key '{key}' is missing in actual results.")
                continue

            expected_value = expected_results[key]
            actual_value = actual_results[key]
            if isinstance(expected_value, dict) and isinstance(actual_value, dict):
                comparison_results.extend(self.compare_dicts(expected_value, actual_value))
            elif isinstance(expected_value, list) and isinstance(actual_value, list):
                comparison_results.extend(self.compare_lists(expected_value, actual_value))
            elif expected_value != actual_value:
                comparison_results.append(
                    f"Value mismatch for key '{key}': expected '{expected_value}', got '{actual_value}'."
                )

        return comparison_results

    def compare_lists(self, expected_results: List[Any], actual_results: List[Any]):
        """Compare two lists and return a list of differences."""
        comparison_results = []
        for index, expected_value in enumerate(expected_results):
            if index >= len(actual_results):
                comparison_results.append(f"Index '{index}' is missing in actual results.")
                continue
            actual_value = actual_results[index]
            if isinstance(expected_value, dict) and isinstance(actual_value, dict):
                comparison_results.extend(self.compare_dicts(expected_value, actual_value))
            elif isinstance(expected_value, list) and isinstance(actual_value, list):
                comparison_results.extend(self.compare_lists(expected_value, actual_value))
            elif expected_value != actual_value:
                comparison_results.append(
                    f"Value mismatch at index '{index}': expected '{expected_value}', got '{actual_value}'."
                )

        return comparison_results

    def compare_values(self, expected_results: Any, actual_results: Any):
        """Compare two values and return a list of differences."""
        if isinstance(expected_results, dict) and isinstance(actual_results, dict):
            return self.compare_dicts(expected_results, actual_results)
        elif isinstance(expected_results, list) and isinstance(actual_results, list):
            return self.compare_lists(expected_results, actual_results)
        else:
            if expected_results != actual_results:
                return [f"Value mismatch: expected '{expected_results}', got '{actual_results}'."]
            else:
                return []


