from typing import Dict, Literal

from pydantic_settings import BaseSettings
import yaml


class BookingEnvironmentConfig(BaseSettings):
    host: str
    username: str
    password: str


class AppConfig(BaseSettings):
    environments: Dict[Literal["dev", "qa"], BookingEnvironmentConfig]

    @classmethod
    def read_yaml(cls, path):
        with open(path, "r") as settings_file:
            content = yaml.safe_load(settings_file)
        return cls(**content)
