import configparser
from pathlib import Path

configFileDir = 'config'
configFile = 'restful_booker_config.ini'

config = configparser.ConfigParser()

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(configFileDir).joinpath(configFile)

config.read(CONFIG_FILE)


def get_restful_booker_api_url():
    return config['restful-booker']['url']


def get_username():
    return config['authentication']['username']


def get_password():
    return config['authentication']['password']
