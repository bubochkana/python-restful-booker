"""Base client abstraction for API client facades.

This module provides a base client class responsible for loading and
exposing environment-specific configuration for concrete API clients.
"""
from src.utils.env_loader import EnvLoader


class AbstractionClient:
    """Base class for API client facades.

    This class centralizes environment configuration loading logic for
    different API clients. Concrete clients specify which configuration
    section should be used (e.g., booking or JSONPlaceholder).
    """
    def __init__(self, client_config):
        """Initialize the client with the specified environment configuration.

        Based on the provided configuration key, the appropriate
        environment-specific configuration is loaded via EnvLoader.

        Args:
            client_config: Name of the environment configuration to load.
                Supported values are ``"booking_config"`` and
                ``"json_placeholder_config"``.

        Raises:
            AttributeError: If an unsupported configuration key is provided.
        """
        if client_config == 'booking_config':
            self.config = EnvLoader().booking_config
        elif client_config == 'json_placeholder_config':
            self.config = EnvLoader().json_placeholder_config
        else:
            raise AttributeError("Provide the environment configuration file")