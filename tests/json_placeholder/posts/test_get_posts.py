import requests
from assertpy import assert_that

from src.clients.json_placeholder_client import JsonPlaceholderClient
from src.models.json_placeholder.posts.post_model import PostModel


class TestPosts:
    def test_get_all_posts(self):
        client = JsonPlaceholderClient()
        posts_endpoint = client.posts_endpoint()

        response = posts_endpoint.get_all_posts()
        assert_that(response.status_code).is_equal_to(requests.codes.ok)

    def test_all_posts_schema_validation(self):
        client = JsonPlaceholderClient()
        posts_endpoint = client.posts_endpoint()

        response = posts_endpoint.get_all_posts()
        for post in response.json():
            PostModel.model_validate(post)

    def test_get_post_by_id(self):
        client = JsonPlaceholderClient()
        posts_endpoint = client.posts_endpoint()

        random_post_id = posts_endpoint.pick_random_post_id()
        response = posts_endpoint.get_post_by_id(random_post_id)

        PostModel.model_validate(response.json())
