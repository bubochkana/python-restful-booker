import requests
from assertpy import assert_that

from src.clients.json_placeholder_client import JsonPlaceholderClient
from src.models.json_placeholder.posts.post_model import PostModel


class TestPosts:
    def test_get_all_posts(self):
        response = JsonPlaceholderClient().get_posts_endpoint().get_all_posts()
        assert_that(response.status_code).is_equal_to(requests.codes.ok)

    def test_all_posts_schema_validation(self):
        response = JsonPlaceholderClient().get_posts_endpoint().get_all_posts()
        for post in response.json():
            PostModel.model_validate(post)

    def test_get_post_by_id(self, posts_client):
        random_post_id = posts_client.pick_random_post_id()
        response = posts_client.get_post_by_id(random_post_id)

        payload = response.json()
        assert_that(payload).is_instance_of(PostModel)

        posts = PostModel.model_validate(payload)
        assert_that('userId').is_instance_of(int)
        assert_that('id').is_instance_of(int)
        assert_that('title').is_instance_of(str)
        assert_that('body').is_instance_of(str)
