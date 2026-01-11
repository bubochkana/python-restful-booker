from src.common.common_paths import CommonPaths
from src.configs.booking_config_model import (
    AppConfig as BookingAppConfig,
    BookingEnvironmentConfig,
)
from src.configs.jsonplaceholder_config_model import (
    AppConfig as JsonPlaceholderAppConfig,
    JsonPlaceholderEnvironmentConfig,
)
from src.utils.singleton_meta import SingletonMeta


class EnvLoader(metaclass=SingletonMeta):
    """Singleton that loads env_configs.yaml once
    and issues the selected env config."""
    def __init__(self, test_env: str = "qa"):
        self._test_env = test_env
        booking_path = CommonPaths.env_booking_config_path()
        json_path = CommonPaths.env_json_placeholder_config_path()

        booking_app_config: (
            BookingAppConfig) = BookingAppConfig.read_yaml(booking_path)
        self._booking_env_config: BookingEnvironmentConfig = \
        booking_app_config.environments[self._test_env]

        json_app_config: (
            JsonPlaceholderAppConfig) \
            = JsonPlaceholderAppConfig.read_yaml(json_path)
        self._json_env_config: JsonPlaceholderEnvironmentConfig = \
        json_app_config.environments[self._test_env]

    @property
    def env_name(self) -> str:
        return self._test_env

    @property
    def booking_config(self) -> BookingEnvironmentConfig:
        """Selected Booking environment config (strongly typed)."""
        return self._booking_env_config


    @property
    def json_placeholder_config(self) -> JsonPlaceholderEnvironmentConfig:
        """Selected JsonPlaceholder environment config (strongly typed)."""
        return self._json_env_config





