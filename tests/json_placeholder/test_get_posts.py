import requests
from assertpy import assert_that

from src.models.posts.post_model import PostModel
from src.models.posts.posts_listing_model import PostsListingModel


class TestPosts:
    def test_get_all_posts(self, posts_client):
        response = posts_client.get_all_posts()
        assert_that(response.status_code).is_equal_to(requests.codes.ok)

        payload = response.json()
        assert_that(payload).is_instance_of(list)
        assert_that(payload).is_not_empty()

        posts = PostsListingModel.model_validate(payload)

        # first = posts.root[0]
        # assert_that(first.userId).is_instance_of(int)
        # assert_that(first.id).is_instance_of(int)
        # assert_that(first.title).is_instance_of(str)
        # assert_that(first.body).is_instance_of(str)

    def get_post_by_id(self, posts_client):
        random_post_id = posts_client.pick_random_post_id()
        response = posts_client.get_post_by_id(random_post_id)

        payload = response.json()
        assert_that(payload).is_instance_of(PostModel)

        posts = PostModel.model_validate(payload)
        assert_that('userId').is_instance_of(int)
        assert_that('id').is_instance_of(int)
        assert_that('title').is_instance_of(str)
        assert_that('body').is_instance_of(str)
