from pydantic_settings import BaseSettings
import yaml

from src.configs.booking_config_model import BookingEnvironmentConfig
from src.configs.jsonplaceholder_config_model import JsonPlaceholderEnvironmentConfig


class ClientsConfig(BaseSettings):
    booking: BookingEnvironmentConfig
    jsonPlaceholder: JsonPlaceholderEnvironmentConfig


class EnvConfig(BaseSettings):
    clients: ClientsConfig

    @classmethod
    def read_yaml(cls, path):
        with open(path, "r") as settings_file:
            content = yaml.safe_load(settings_file)
        return cls(**content)
