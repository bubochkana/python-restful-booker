"""Posts endpoint client.

This module provides an API client for interacting with post-related
endpoints of the JsonPlaceholder service, including retrieving, creating,
updating, deleting posts, and generating random post test data.
"""

import random

from faker import Faker
from requests import Response

from src.clients.common.base_endpoint import AbstractionEndpoint
from src.clients.json_placeholder.endpoints.users_endpoint import UsersEndpoint
from src.models.json_placeholder.posts.post_model import PostModel


class PostsEndpoint(AbstractionEndpoint):
    """Client for post-related API operations.

    This class encapsulates HTTP interactions with post endpoints,
    providing CRUD operations and helper methods for generating
    random post data for testing purposes.
    """

    def __init__(self, host: str):
        """Initialize the PostsEndpoint.

        Args:
            host: Base URL of the JsonPlaceholder service.
        """
        super().__init__()

        self.host = host
        self.users_endpoint = UsersEndpoint(host)

    def get_all_posts(self) -> Response:
        """Retrieve all posts.

        Returns:
            Response: HTTP response containing a list of posts.
        """
        return self.get(f"{self.host}/posts")

    def get_post_by_id(self, post_id) -> Response:
        """Retrieve a post by its identifier.

        Args:
            post_id: Unique identifier of the post.

        Returns:
            Response: HTTP response containing post details.
        """
        return self.get(f"{self.host}/posts/{post_id}")

    def get_all_comments_for_the_post_id(self, post_id) -> Response:
        """Retrieve all comments for a specific post.

        Args:
            post_id: Identifier of the post whose comments should be retrieved.

        Returns:
            Response: HTTP response containing a list of comments for the post.
        """
        return self.get(f"{self.host}/posts/{post_id}/comments")

    def create_post(self, body: PostModel) -> Response:
        """Create a new post.

        Args:
            body: Post model containing post data.

        Returns:
            Response: HTTP response containing created post information.
        """
        return self.post(f"{self.host}/posts", json=body.model_dump())

    def delete_post_by_id(self, post_id) -> Response:
        """Delete a post by its identifier.

        Args:
            post_id: Unique identifier of the post to be deleted.

        Returns:
            Response: HTTP response indicating deletion status.
        """
        return self.delete(f"{self.host}/posts/{post_id}")

    def update_whole_post_by_id(self, body: PostModel, post_id) -> Response:
        """Update an entire post by its identifier.

        Args:
            body: Post model containing updated post data.
            post_id: Unique identifier of the post to be updated.

        Returns:
            Response: HTTP response containing updated post information.
        """
        return self.put(f"{self.host}/posts/{post_id}", json=body.model_dump())

    def update_partially_post_by_id(self, body: PostModel, post_id) -> Response:
        """Partially update a post by its identifier.

        Args:
            body: Post model containing fields to be updated.
            post_id: Unique identifier of the post to be updated.

        Returns:
            Response: HTTP response containing partially updated post information.
        """
        return self.patch(f"{self.host}/posts/{post_id}", json=body)

    def pick_random_post_id(self) -> int:
        """Pick a random post identifier from existing posts.

        Returns:
            int: Randomly selected post identifier.
        """
        posts_ids_list = self.get_all_posts()
        my_obj_list: list[PostModel] = [PostModel(**dict_item) for dict_item in posts_ids_list.json()]
        return random.choice(my_obj_list).id

    def build_random_post(self) -> PostModel:
        """Build a random post model for testing purposes.

        Uses Faker to generate realistic random post data and associates
        the post with a randomly selected user.

        Returns:
            PostModel: Randomly generated post model.
        """
        faker: Faker = Faker()
        random_user_id = self.users_endpoint.pick_random_user_id()
        return PostModel(title=faker.text(max_nb_chars=20), body=faker.text(max_nb_chars=100), userId=random_user_id)
