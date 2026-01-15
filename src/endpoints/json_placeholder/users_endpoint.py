"""Users endpoint client.

This module provides an API client for interacting with user-related
endpoints of the JsonPlaceholder service, including retrieving users
and helping method to select a random user for testing purposes.
"""

import random

import requests
from requests import Response

from src.models.json_placeholder.users.user_model import UserModel


class UsersEndpoint:
    """Client for user-related API operations.

    This class encapsulates HTTP interactions with user endpoints and
    provides helper methods for retrieving user data and selecting
    random users for test scenarios.
    """

    def __init__(self, host: str):
        """Initialize the UsersEndpoint.

        Args:
            host: Base URL of the JsonPlaceholder service.
        """
        self.host = host

    def get_all_users(self) -> Response:
        """Retrieve all users.

        Returns:
            Response: HTTP response containing a list of users.
        """
        return requests.get(f"{self.host}/users")

    def pick_random_user_id(self) -> int:
        """Pick a random user identifier from existing users.

        Returns:
            int: Randomly selected user identifier.
        """
        users_ids_list = self.get_all_users()
        my_obj_list: list[UserModel] = [UserModel(**dict_item) for dict_item in users_ids_list.json()]
        return random.choice(my_obj_list).id
