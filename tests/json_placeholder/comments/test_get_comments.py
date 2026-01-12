import random

import requests
from assertpy import assert_that

from src.clients.json_placeholder_client import JsonPlaceholderClient


class TestPosts:
    def test_get_comments_for_a_post(self):
        post_id = random.randint(1, 100)
        response = (JsonPlaceholderClient().get_comments_endpoint()
                    .get_all_comments_by_post_id(post_id))
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
