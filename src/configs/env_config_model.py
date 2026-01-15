"""Environment configuration models and loader.

This module defines Pydantic models used to represent environment-level
configuration loaded from YAML files, including configuration for
multiple API clients.
"""

import yaml
from pydantic_settings import BaseSettings

from src.configs.booking_config_model import BookingEnvironmentConfig
from src.configs.jsonplaceholder_config_model import JsonPlaceholderEnvironmentConfig


class ClientsConfig(BaseSettings):
    """Configuration for all supported API clients.

    This model groups configuration sections for individual API clients,
    such as the booking service and the JsonPlaceholder service.
    """

    booking: BookingEnvironmentConfig
    jsonPlaceholder: JsonPlaceholderEnvironmentConfig


class EnvConfig(BaseSettings):
    """Root environment configuration model.

    This model represents the top-level configuration structure loaded
    from an environment-specific YAML file.
    """

    clients: ClientsConfig

    @classmethod
    def read_yaml(cls, path):
        """Load environment configuration from a YAML file.

        Reads the provided YAML configuration file and initializes an
        EnvConfig instance with its contents.

        Args:
            path: Path to the YAML configuration file.

        Returns:
            EnvConfig: Parsed environment configuration instance.
        """
        with open(path, "r") as settings_file:
            content = yaml.safe_load(settings_file)
        return cls(**content)
