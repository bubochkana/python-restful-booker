"""Json Placeholder client module.

This module provides a client facade for accessing JsonPlaceholder-related API
endpoints.
"""

from src.endpoints.json_placeholder.comments_endpoint import CommentsEndpoint
from src.endpoints.json_placeholder.posts_endpoint import PostsEndpoint
from src.utils.env_loader import EnvLoader


class JsonPlaceholderClient:
    """Client facade for JsonPlaceholder-related API endpoints.

    This class acts as an entry point for interacting with the JsonPlaceholder system.
    It initializes configuration and provides access to JsonPlaceholder-related endpoints.
    """

    def __init__(self):
        """Initialize the JsonPlaceholderClient.

        Loads JsonPlaceholder configuration from the environment.
        """
        self.config = EnvLoader().json_placeholder_config

    def posts_endpoint(self) -> PostsEndpoint:
        """Return the Posts endpoint.

        Returns:
            PostsEndpoint: An initialized post endpoint instance.
        """
        return PostsEndpoint(self.config.host)

    def comments_endpoint(self) -> CommentsEndpoint:
        """Return the Comments endpoint.

        Returns:
            CommentsEndpoint: An initialized comments endpoint instance.
        """
        return CommentsEndpoint(self.config.host)
