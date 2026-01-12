from typing import List

from pydantic import BaseModel, RootModel


class UserAddressGeoModel(BaseModel):
    lat: str
    lng: str

class UserAddressModel(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: UserAddressGeoModel

class UserCompanyModel(BaseModel):
    name: str
    catchPhrase: str
    bs: str

class UserModel(BaseModel):
    id: int = None
    name: str
    email: str
    address: UserAddressModel
    phone: str
    website: str
    company: UserCompanyModel

class UserListingModel(BaseModel):
    userId: int
    id: int
    title: str
    body: str

class UsersListingModel(RootModel[List[UserListingModel]]):
    pass


