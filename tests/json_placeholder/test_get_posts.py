import requests
from assertpy import assert_that


class TestPosts:
    def test_get_all_posts(self, posts_client):
        response = posts_client.get_all_posts()
        assert_that(response.status_code).is_equal_to(requests.codes.ok)