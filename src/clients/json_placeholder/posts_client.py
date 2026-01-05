import requests

from src.common.common_paths import get_qa_env_dir
from src.configs.settings_management_model import Settings


class PostsClient:
    def __init__(self):
        settings = Settings.read_yaml(get_qa_env_dir().joinpath("qa_config.yaml"))
        self.host = settings.json_placeholder_url

    def get_all_posts(self):
        return requests.get(f"{self.host}/posts")
