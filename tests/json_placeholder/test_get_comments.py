import random

import requests
from assertpy import assert_that


class TestPosts:
    def test_get_comments_for_a_post(self, comments_client):
        post_id = random.randint(1, 100)
        response = comments_client.get_all_comments_by_post_id(post_id)
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
