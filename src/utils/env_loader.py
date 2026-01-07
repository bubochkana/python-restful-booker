from pathlib import Path
from typing import Optional

from src.common.common_paths import CommonPaths
from src.configs.configs_management_model import AppConfig, EnvironmentConfig
from src.utils.singleton_meta import SingletonMeta


class EnvLoader(metaclass=SingletonMeta):
    """Singleton that loads env_configs.yaml once and issues the selected env config."""

    def __init__(self, test_env: str = "qa", config_path: Optional[str | Path] = None):
        if getattr(self, "_initialized", False):
            return
        self._initialized = True

        self._test_env = test_env

        if config_path is None:
            config_path = CommonPaths.env_config_path()
        else:
            config_path = Path(config_path)

        self._app_config: AppConfig = AppConfig.read_yaml(config_path)
        self._env_config: EnvironmentConfig = self._app_config.environments[self._test_env]

    @property
    def env_name(self) -> str:
        return self._test_env

    @property
    def config(self) -> EnvironmentConfig:
        """Selected environment config (strongly typed)."""
        return self._env_config

    @property
    def restful_booker_url(self) -> str:
        return self._env_config.restful_booker_url

    @property
    def username(self) -> str:
        return self._env_config.username

    @property
    def password(self) -> str:
        return self._env_config.password

    @property
    def json_placeholder_url(self) -> str:
        return self._env_config.json_placeholder_url
