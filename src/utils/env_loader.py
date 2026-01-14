from typing import Literal

from src.common.common_paths import CommonPaths
from src.configs.booking_config_model import BookingEnvironmentConfig
from src.configs.env_config_model import EnvConfig
from src.configs.jsonplaceholder_config_model import JsonPlaceholderEnvironmentConfig
from src.utils.singleton_meta import SingletonMeta

EnvName = Literal["dev", "qa"]

class EnvLoader(metaclass=SingletonMeta):
    """Singleton that loads env_configs.yaml once
    and issues the selected env config.
    """
    def __init__(self, test_env: EnvName = "qa"):
        self._test_env: EnvName = test_env

        config_path = CommonPaths.env_config_file_path(self._test_env)
        env_config: EnvConfig = EnvConfig.read_yaml(config_path)

        self._booking_env_config: BookingEnvironmentConfig = env_config.clients.booking
        self._json_env_config: JsonPlaceholderEnvironmentConfig = env_config.clients.jsonPlaceholder


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





