"""Configuration models for booking client settings.

This module defines strongly typed configuration classes used to load
booking-related environment and client configuration values via
Pydantic settings.
"""

from pydantic_settings import BaseSettings


class BookingEnvironmentConfig(BaseSettings):
    """Configuration for booking environment credentials.

    This class represents environment-specific settings required to
    authenticate and connect to the booking service.
    """

    host: str
    username: str
    password: str


class BookingClientConfig(BaseSettings):
    """Root configuration for the booking client.

    This class groups all booking-related configuration sections into a
    single client configuration model.
    """

    booking: BookingEnvironmentConfig
