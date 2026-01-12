from pydantic_settings import BaseSettings


class BookingEnvironmentConfig(BaseSettings):
    host: str
    username: str
    password: str


class BookingClientConfig(BaseSettings):
    booking: BookingEnvironmentConfig

