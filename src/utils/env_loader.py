"""Environment configuration loader.

This module provides a singleton-based loader responsible for resolving
and exposing environment-specific configuration for different API
clients, such as booking and JsonPlaceholder services.
"""

from typing import Literal

from src.common.common_paths import CommonPaths
from src.configs.booking_config_model import BookingEnvironmentConfig
from src.configs.env_config_model import EnvConfig
from src.configs.jsonplaceholder_config_model import JsonPlaceholderEnvironmentConfig
from src.utils.singleton_meta import SingletonMeta

EnvName = Literal["dev", "qa"]


class EnvLoader(metaclass=SingletonMeta):
    """Environment configuration loader.

    This module provides a singleton-based loader responsible for resolving
    and exposing environment-specific configuration for different API
    clients, such as booking and JsonPlaceholder services.
    """

    def __init__(self, test_env: EnvName = "qa"):
        """Initialize the environment loader.

        Loads configuration for the specified environment and initializes
        strongly typed configuration objects for supported API clients.

        Args:
            test_env: Target environment name (e.g., "dev" or "qa").
        """
        self._test_env: EnvName = test_env

        config_path = CommonPaths.env_config_file_path(self._test_env)
        env_config: EnvConfig = EnvConfig.read_yaml(config_path)

        self._booking_env_config: BookingEnvironmentConfig = env_config.clients.booking
        self._json_env_config: JsonPlaceholderEnvironmentConfig = env_config.clients.jsonPlaceholder

    @property
    def env_name(self) -> str:
        """Return the name of the currently selected environment.

        Returns:
            str: Environment name (e.g., "dev" or "qa").
        """
        return self._test_env

    @property
    def booking_config(self) -> BookingEnvironmentConfig:
        """Return the booking service configuration.

        Returns:
            BookingEnvironmentConfig: Strongly typed booking environment
            configuration for the selected environment.
        """
        return self._booking_env_config

    @property
    def json_placeholder_config(self) -> JsonPlaceholderEnvironmentConfig:
        """Return the JSONPlaceholder service configuration.

        Returns:
            JsonPlaceholderEnvironmentConfig: Strongly typed JSONPlaceholder
            environment configuration for the selected environment.
        """
        return self._json_env_config
