from src.endpoints.json_placeholder.comments_endpoint import CommentsEndpoint
from src.endpoints.json_placeholder.posts_endpoint import PostsEndpoint
from src.utils.env_loader import EnvLoader


class JsonPlaceholderClient:
    def __init__(self):
        self.config = EnvLoader().json_placeholder_config

    def posts_endpoint(self) -> PostsEndpoint:
        return PostsEndpoint(self.config.host)

    def comments_endpoint(self) -> CommentsEndpoint:
        return CommentsEndpoint(self.config.host)

    def albums_endpoint(self):
        pass

    def photos_endpoint(self):
        pass

    def todos_endpoint(self):
        pass

    def users_endpoint(self):
        pass
