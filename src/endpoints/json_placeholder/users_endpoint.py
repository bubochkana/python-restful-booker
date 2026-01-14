import random

import requests
from requests import Response

from src.models.json_placeholder.users.user_model import UserModel


class UsersEndpoint:
    def __init__(self, host: str):
        self.host = host

    def get_all_users(self) -> Response:
        return requests.get(f"{self.host}/users")

    def pick_random_user_id(self) -> int:
        users_ids_list = self.get_all_users()
        my_obj_list: list[UserModel] \
            = [UserModel(**dict_item) for dict_item in users_ids_list.json()]
        return random.choice(my_obj_list).id