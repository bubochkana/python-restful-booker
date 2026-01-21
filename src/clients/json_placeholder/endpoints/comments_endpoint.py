"""Comments endpoint client.

This module provides an API client for interacting with comment-related
endpoints of the JsonPlaceholder service, including retrieving, creating,
deleting comments, and generating random comment test data.
"""

import random

from faker import Faker
from requests import Response

from src.clients.common.base_endpoint import AbstractionEndpoint
from src.clients.json_placeholder.endpoints.posts_endpoint import PostsEndpoint
from src.models.json_placeholder.comments.comment_model import CommentModel


class CommentsEndpoint(AbstractionEndpoint):
    """Client for comment-related API operations.

    This class encapsulates HTTP interactions with comment endpoints,
    allowing retrieval, creation, deletion of comments, and generation
    of random comment data for testing purposes.
    """
    def __init__(self, host: str):
        """Initialize the CommentsEndpoint.

        Args:
            host: Base URL of the JsonPlaceholder service.
        """
        super().__init__()

        self.host = host
        self.posts_endpoint = PostsEndpoint(host)

    def get_all_comments_by_post_id(self, post_id) -> Response:
        """Retrieve all comments associated with a specific post.

        Args:
            post_id: Identifier of the post whose comments should be retrieved.

        Returns:
            Response: HTTP response containing a list of comments for the given post.
        """
        return self.get(f"{self.host}/comments?postId={post_id}")

    def get_comment(self, comment_id) -> Response:
        """Retrieve a comment by its identifier.

        Args:
            comment_id: Unique identifier of the comment.

        Returns:
            Response: HTTP response containing comment details.
        """
        return self.get(f"{self.host}/comments?comment_id={comment_id}")

    def create_comment_for_post(self, body: CommentModel, post_id) -> Response:
        """Create a new comment for a specific post.

        Args:
            body: Comment model containing comment data.
            post_id: Identifier of the post to which the comment belongs.

        Returns:
            Response: HTTP response containing created comment information.
        """
        return self.post(f"{self.host}/posts/{post_id}/comments", json=body.model_dump())

    def delete_comment_by_id(self, post_id) -> Response:
        """Delete a comment by its identifier.

        Args:
            post_id: Identifier of the comment to be deleted.

        Returns:
            Response: HTTP response indicating deletion status.
        """
        return self.delete(f"{self.host}/comments/{post_id}")

    def pick_random_comment_id_for_post(self, post_id) -> str:
        """Pick a random comment ID for a given post.

        Args:
            post_id: Identifier of the post whose comments are requested.

        Returns:
            str: Randomly selected comment identifier.
        """
        comments_for_post_id_list = self.get_all_comments_by_post_id(post_id)
        my_obj_list: list[CommentModel] = [CommentModel(**dict_item) for dict_item in comments_for_post_id_list.json()]
        return str(random.choice(my_obj_list).id)

    def build_random_comment(self) -> CommentModel:
        """Build a random comment model for testing purposes.

        Uses Faker to generate realistic random comment data and associates
        the comment with a randomly selected post.

        Returns:
            CommentModel: Randomly generated comment model.
        """
        faker: Faker = Faker()
        random_post_id = self.posts_endpoint.pick_random_post_id()
        return CommentModel(
            postId=random_post_id, name=faker.name(), email=faker.email(), body=faker.text(max_nb_chars=100)
        )
