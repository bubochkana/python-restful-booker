from pydantic_settings import BaseSettings


class JsonPlaceholderEnvironmentConfig(BaseSettings):
    host: str

class JsonPlaceholderClientConfig(BaseSettings):
    jsonPlaceholder: JsonPlaceholderEnvironmentConfig