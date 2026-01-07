from src.endpoints.json_placeholder.comments_endpoint import CommentsEndpoint
from src.endpoints.json_placeholder.posts_endpoint import PostsEndpoint
from src.utils.env_loader import EnvLoader


class JsonPlaceholderClient:
    def __init__(self):
        env = EnvLoader().config

        self.host = str(env.restful_booker_url)

    def get_posts_endpoint(self) -> PostsEndpoint:
        return PostsEndpoint(self.host)

    def get_comments_endpoint(self) -> CommentsEndpoint:
        return CommentsEndpoint(self.host)

    def get_albums_endpoint(self):
        pass

    def get_photos_endpoint(self):
        pass

    def get_todos_endpoint(self):
        pass

    def get_users_endpoint(self):
        pass
