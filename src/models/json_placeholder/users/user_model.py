from typing import List

from pydantic import BaseModel, RootModel, ConfigDict, Field


class UserAddressGeoModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    lat: str = Field(alias = "latitude")
    lng: str = Field(alias = "longitude")

class UserAddressModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    street: str = Field(alias = "street")
    suite: str = Field(alias = "suite")
    city: str = Field(alias = "city")
    zipcode: str = Field(alias = "zipCode")
    geo: UserAddressGeoModel = Field(alias = "geo")

class UserCompanyModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(alias = "name")
    catchPhrase: str = Field(alias = "catchPhrase")
    bs: str = Field(alias = "bs")

class UserModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(alias = "id", default=None)
    name: str = Field(alias = "name")
    email: str = Field(alias = "email")
    address: UserAddressModel = Field(alias = "address")
    phone: str = Field(alias = "phone")
    website: str = Field(alias = "website")
    company: UserCompanyModel = Field(alias = "company")

class UserListingModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    userId: int = Field(alias = "userId")
    id: int = Field(alias = "id")
    title: str = Field(alias = "title")
    body: str = Field(alias = "body")

class UsersListingModel(RootModel[List[UserListingModel]]):
    pass


