"""Json Placeholder client module.

This module provides a client facade for accessing JsonPlaceholder-related API
endpoints.
"""
from src.clients.common.base_client import AbstractionClient
from src.clients.json_placeholder.endpoints.comments_endpoint import CommentsEndpoint
from src.clients.json_placeholder.endpoints.posts_endpoint import PostsEndpoint
from src.clients.json_placeholder.endpoints.users_endpoint import UsersEndpoint


class JsonPlaceholderClient(AbstractionClient):
    """Client facade for JsonPlaceholder-related API endpoints.

    This class acts as an entry point for interacting with the JsonPlaceholder system.
    It initializes configuration and provides access to JsonPlaceholder-related endpoints.
    """

    def __init__(self):
        """Initialize the JsonPlaceholderClient.

        Loads JsonPlaceholder configuration from the environment.
        """
        super().__init__(client_config="json_placeholder_config")

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

    def users_endpoint(self) -> UsersEndpoint:
        """Return the Users endpoint.

        Returns:
            UsersEndpoint: An initialized users endpoint instance.
        """
        return UsersEndpoint(self.config.host)
