import requests

from src.common.common_paths import get_qa_env_dir
from src.configs.settings_management_model import Settings


class CommentsClient:
    def __init__(self):
        settings = Settings.read_yaml(get_qa_env_dir().joinpath("qa_config.yaml"))
        self.host = settings.json_placeholder_url

    def get_all_comments_by_pots_id(self, post_id):
        return requests.get(f"{self.host}/posts/{post_id}/comments")