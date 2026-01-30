import random

import pytest
import requests
from assertpy import assert_that

from src.clients.json_placeholder.json_placeholder_client import JsonPlaceholderClient


class TestPosts:
    @pytest.mark.smoke
    def test_get_comments_for_a_post(self):
        client = JsonPlaceholderClient()
        comments_endpoint = client.comments_endpoint()

        post_id = random.randint(1, 100)
        response = comments_endpoint.get_all_comments_by_post_id(post_id)
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
