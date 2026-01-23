"""Action layer for JsonPlaceholder API test operations.

This module contains high-level, reusable actions for interacting with
the JsonPlaceholder API. It abstracts low-level endpoint calls, performs
response validation, and converts API responses into strongly-typed
domain models to keep test cases concise and maintainable.
"""
import logging
import random

from assertpy import assert_that
from faker import Faker
from requests import Response

from src.clients.json_placeholder.json_placeholder_client import JsonPlaceholderClient
from src.helpers.compare_models import CompareModel
from src.models.json_placeholder.comments.comment_model import CommentModel
from src.models.json_placeholder.posts.post_model import PostModel


class JsonPlaceholderActions:
    """High-level action layer for JsonPlaceholder API operations.

    This class provides reusable, test-oriented actions for interacting
    with the JsonPlaceholder API, including creating, retrieving, and
    deleting posts and comments. It abstracts low-level endpoint calls,
    performs response validation, and converts API responses into
    strongly-typed domain models.

    The action layer also includes helper methods for generating
    realistic random test data and selecting random existing resources,
    allowing tests to remain concise and focused on assertions rather
    than API mechanics.
    """

    def __init__(self):
        """Initialize JsonPlaceholderActions with API client and endpoints.

        Creates an instance of ``JsonPlaceholderClient`` and resolves the
        required endpoints for posts, comments, and users operations.
        """
        self.json_placeholder_client = JsonPlaceholderClient()
        self.comments_endpoint = self.json_placeholder_client.comments_endpoint()
        self.posts_endpoint = self.json_placeholder_client.posts_endpoint()
        self.users_endpoint = self.json_placeholder_client.users_endpoint()

    def add_post(self, post_post_model: PostModel = None) -> PostModel:
        """Create a new post.

        Sends a request to create a post using the provided post model.
        If no model is provided, a random post model is generated
        automatically. The created post is validated by comparing the
        request payload with the response payload.

        Args:
            post_post_model: Optional post model to use for creation.
                If not provided, a random post model is generated.

        Returns:
            PostModel: The created post represented as a domain model.

        Raises:
            Exception: If the response status code is not 201.
            AssertionError: If the created post does not match the request
                payload.
        """
        logging.info("Adding a new post")

        if post_post_model is None:
            post_post_model = self.build_random_post()

        response: Response = self.posts_endpoint.create_post(post_post_model)
        if response.status_code != 201:
            raise Exception(f"Expected status code 201, but got {response.status_code}")

        created_post_as_model = PostModel(**response.json())

        comparison_results = CompareModel().compare_values(
            post_post_model.model_dump(), created_post_as_model.booking.model_dump()
        )
        assert_that(comparison_results,
                    f"Following differences found: {comparison_results}").is_empty()

        logging.info('Post added successfully')

        return created_post_as_model

    def add_comment(self, post_id, comment_post_model: CommentModel = None) -> CommentModel:
        """Add a comment to a specific post.

        Sends a request to create a comment for the given post ID.
        If no comment model is provided, a random comment model is generated.
        The created comment is validated against the request payload.

        Args:
            post_id: Identifier of the post to which the comment will be added.
            comment_post_model: Optional comment model to use for creation.
                If not provided, a random comment model is generated.

        Returns:
            CommentModel: The created comment represented as a domain model.

        Raises:
            Exception: If the response status code is not 201.
            AssertionError: If the created comment does not match the request
                payload.
        """
        logging.info("Adding a comment to a post")

        if comment_post_model is None:
            comment_post_model = self.build_random_comment()

        response: Response = self.comments_endpoint.create_comment_for_post(comment_post_model, post_id)
        if response.status_code != 201:
            raise Exception(f"Expected status code 201, but got {response.status_code}")

        created_comment_as_model = CommentModel(**response.json())

        comparison_results = CompareModel().compare_values(
            comment_post_model.model_dump(), created_comment_as_model.booking.model_dump()
        )
        assert_that(comparison_results,
                    f"Following differences found: {comparison_results}").is_empty()

        logging.info('Comment added successfully')

        return created_comment_as_model

    def delete_post(self, post_id) -> None:
        """Delete an existing post.

        Sends a request to delete a post by its identifier and validates
        that the operation completed successfully.

        Args:
            post_id: Identifier of the post to delete.

        Raises:
            Exception: If the response status code is not 201.
        """
        logging.info("Deleting an existing post")

        response: Response = self.posts_endpoint.delete_post_by_id(post_id)
        if response.status_code != 201:
            raise Exception(f"Expected status code 201, but got {response.status_code}")

        logging.info("Post deleted successfully!")

    def delete_comment(self, comment_id) -> None:
        """Delete an existing comment.

        Sends a request to delete a comment by its identifier and validates
        that the operation completed successfully.

        Args:
            comment_id: Identifier of the comment to delete.

        Raises:
            Exception: If the response status code is not 201.
        """
        logging.info("Deleting an existing comment in a post")

        response: Response = self.comments_endpoint.delete_comment_by_id(comment_id)
        if response.status_code != 201:
            raise Exception(f"Expected status code 201, but got {response.status_code}")

        logging.info("Comment deleted successfully!")

    def get_post(self, post_id) -> PostModel:
        """Retrieve a post by its identifier.

        Sends a request to fetch a post by ID, validates the response
        status code, and converts the response payload into a ``PostModel``.

        Args:
            post_id: Identifier of the post to retrieve.

        Returns:
            PostModel: Retrieved post represented as a domain model.

        Raises:
            Exception: If the response status code is not 200.
        """
        logging.info(f"Getting a post by id: {post_id}")

        response: Response = self.posts_endpoint.get_post_by_id(post_id)
        if response.status_code != 200:
            raise Exception(f"Expected status code 200, but got {response.status_code}")

        post_as_model = PostModel(**response.json())

        return post_as_model

    def get_comment(self, comment_id) -> CommentModel:
        """Retrieve a comment by its identifier.

        Sends a request to fetch a comment by ID, validates the response
        status code, and converts the response payload into a
        ``CommentModel``.

        Args:
            comment_id: Identifier of the comment to retrieve.

        Returns:
            CommentModel: Retrieved comment represented as a domain model.

        Raises:
            Exception: If the response status code is not 200.
        """
        logging.info(f"Getting a post by id: {comment_id}")

        response: Response = self.comments_endpoint.get_comment(comment_id)
        if response.status_code != 200:
            raise Exception(f"Expected status code 200, but got {response.status_code}")

        comment_as_model = CommentModel(**response.json())

        return comment_as_model


    def pick_random_post_id(self) -> int:
        """Pick a random post identifier from existing posts.

        Returns:
            int: Randomly selected post identifier.
        """
        posts_ids_list = self.posts_endpoint.get_all_posts()
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

    def pick_random_comment_id_for_post(self, post_id) -> str:
        """Pick a random comment ID for a given post.

        Args:
            post_id: Identifier of the post whose comments are requested.

        Returns:
            str: Randomly selected comment identifier.
        """
        comments_for_post_id_list = self.comments_endpoint.get_all_comments_by_post_id(post_id)
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
        random_post_id = self.pick_random_post_id()
        return CommentModel(
            postId=random_post_id, name=faker.name(), email=faker.email(), body=faker.text(max_nb_chars=100)
        )