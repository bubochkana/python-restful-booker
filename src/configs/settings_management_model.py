from pydantic_settings import BaseSettings
import yaml


class Settings(BaseSettings):
    url: str
    username: str
    password: str

    @classmethod
    def read_yaml(cls, path):
        with open(path, "r") as settings_file:
            content = yaml.safe_load(settings_file)
        return cls(**content)
