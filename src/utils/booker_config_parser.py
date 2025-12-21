import configparser
from src.common.common_paths import root_dir


class ConfigurationParser:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(
            root_dir.joinpath('src').joinpath('config').joinpath('restful_booker_config.ini'))

    def get_restful_booker_api_url(self):
        return self.config['restful-booker']['url']

    def get_username(self):
        return self.config['authentication']['username']

    def get_password(self):
        return self.config['authentication']['password']
