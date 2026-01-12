from typing import Optional

from pydantic import BaseModel


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
    id: Optional[int] = None
    name: str
    email: str
    address: UserAddressModel
    phone: str
    website: str
    company: UserCompanyModel


