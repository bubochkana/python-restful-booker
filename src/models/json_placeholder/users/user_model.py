"""Pydantic models for user-related API data.

This module defines Pydantic models representing users and related
entities returned by the JsonPlaceholder API, including user addresses,
geographic information, company details, and user listings.
"""

from typing import List

from pydantic import BaseModel, ConfigDict, Field, RootModel


class UserAddressGeoModel(BaseModel):
    """Model representing geographic coordinates of a user address.

    This model maps latitude and longitude values associated with a
    user's address.
    """

    model_config = ConfigDict(populate_by_name=True)

    lat: str = Field(alias="latitude")
    lng: str = Field(alias="longitude")


class UserAddressModel(BaseModel):
    """Model representing a user's address.

    This model contains address details such as street, city, zip code,
    and associated geographic coordinates.
    """

    model_config = ConfigDict(populate_by_name=True)

    street: str = Field(alias="street")
    suite: str = Field(alias="suite")
    city: str = Field(alias="city")
    zipcode: str = Field(alias="zipCode")
    geo: UserAddressGeoModel = Field(alias="geo")


class UserCompanyModel(BaseModel):
    """Model representing a user's company information.

    This model contains company-related details associated with a user,
    including company name, catchphrase, and business description.
    """

    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(alias="name")
    catchPhrase: str = Field(alias="catchPhrase")
    bs: str = Field(alias="businessDescription")


class UserModel(BaseModel):
    """Model representing a single user.

    This model aggregates user identity information, contact details,
    address data, and company information.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(alias="id", default=None)
    name: str = Field(alias="name")
    email: str = Field(alias="email")
    address: UserAddressModel = Field(alias="address")
    phone: str = Field(alias="phone")
    website: str = Field(alias="website")
    company: UserCompanyModel = Field(alias="company")


class UserListingModel(BaseModel):
    """Model representing a user-related listing entry.

    This model is typically used for listing-style API responses that
    include references to user identifiers and related content.
    """

    model_config = ConfigDict(populate_by_name=True)

    userId: int = Field(alias="userId")
    id: int = Field(alias="id")
    title: str = Field(alias="title")
    body: str = Field(alias="body")


class UsersListingModel(RootModel[List[UserListingModel]]):
    """Model representing a list of user listings.

    This root model wraps a list of UserListingModel instances returned
    by the API when multiple user listings are retrieved.
    """

    pass
