from typing import List

from pydantic import RootModel

from src.models.json_placeholder.users.user_listing_model import \
    UserListingModel


class UsersListingModel(RootModel[List[UserListingModel]]):
    pass