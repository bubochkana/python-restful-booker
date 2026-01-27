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
        """Initialize the client with an environment-specific configuration.

        This constructor dynamically resolves and loads a configuration
        attribute from :class:`EnvLoader` based on the provided configuration
        name. The abstraction layer remains decoupled from concrete
        configuration implementations by relying on dynamic attribute access.

        Args:
            client_config (str): Name of the configuration attribute to load
                from ``EnvLoader`` (e.g. ``"booking_config"``,
                ``"json_placeholder_config"``).

        Raises:
            AttributeError: If the specified configuration attribute does not
                exist on ``EnvLoader``.
        """
        env_loader = EnvLoader()
        try:
            self.config = getattr(env_loader, client_config)
        except AttributeError:
            raise AttributeError(f"Unknown config: {client_config}")