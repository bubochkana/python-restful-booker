"""Configuration models for JsonPlaceholder client settings.

This module defines strongly typed configuration classes used to load
JsonPlaceholder-related environment and client configuration values via
Pydantic settings.
"""

from pydantic_settings import BaseSettings


class JsonPlaceholderEnvironmentConfig(BaseSettings):
    """Configuration for JsonPlaceholder environment.

    This class represents environment-specific settings required to connect to the JsonPlaceholder service.
    """

    host: str


class JsonPlaceholderClientConfig(BaseSettings):
    """Root configuration for the JsonPlaceholder client.

    This class groups all JsonPlaceholder-related configuration sections into a
    single client configuration model.
    """

    jsonPlaceholder: JsonPlaceholderEnvironmentConfig
