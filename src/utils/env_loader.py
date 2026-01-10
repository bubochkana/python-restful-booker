from pathlib import Path
from typing import Optional

from src.common.common_paths import CommonPaths
from src.configs.booking_config_model import (AppConfig,
                                              BookingEnvironmentConfig)
from src.configs.jsonplaceholder_config_model import \
    JsonPlaceholderEnvironmentConfig
from src.utils.singleton_meta import SingletonMeta


class EnvLoader(metaclass=SingletonMeta):
    """Singleton that loads env_configs.yaml once
    and issues the selected env config."""

    def __init__(self, test_env: str = "qa",
                 config_path: Optional[str | Path] = None):
        if getattr(self, "_initialized", False):
            return

        self._test_env = test_env

        if config_path is None:
            config_path = CommonPaths.env_config_path()
        else:
            config_path = Path(config_path)

        # TODO - not sure how to switch between BookingEnvironmentConfig and JsonPlaceholderConfig
        self._app_config: AppConfig = AppConfig.read_yaml(config_path)
        self._env_config: BookingEnvironmentConfig \
            = self._app_config.environments[self._test_env]

    @property
    def env_name(self) -> str:
        return self._test_env

    @property
    def booking_config(self) -> BookingEnvironmentConfig:
        """Selected Booking environment config (strongly typed)."""
        return self._env_config

    @property
    def json_placeholder_config(self) -> JsonPlaceholderEnvironmentConfig:
        """Selected JsonPlaceholder environment config (strongly typed)."""
        return self._env_config




