from typing import List

from pydantic import BaseModel, RootModel, ConfigDict, Field


class UserAddressGeoModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    lat: str = Field(alias = "latitude")
    lng: str = Field(alias = "longitude")

class UserAddressModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    street: str
    suite: str
    city: str
    zipcode: str = Field(alias = "zipCode")
    geo: UserAddressGeoModel

class UserCompanyModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    catchPhrase: str
    bs: str

class UserModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int = None
    name: str
    email: str
    address: UserAddressModel
    phone: str
    website: str
    company: UserCompanyModel

class UserListingModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    userId: int
    id: int
    title: str
    body: str

class UsersListingModel(RootModel[List[UserListingModel]]):
    pass


