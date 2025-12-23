from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    url: str = 'https://restful-booker.herokuapp.com/'
    username: str = 'admin'
    password: str = 'password123'

    # TODO - how to handle the settings specific to the QA/DEV environment here?
    # TODO - is is safe to store the creds in the model?