import requests
from assertpy import assert_that

from src.clients.json_placeholder_client import JsonPlaceholderClient


class TestJsonPlaceholderCommentsE2E:
    def test_posts_e2e(self):
        client = JsonPlaceholderClient()
        posts_endpoint = client.get_posts_endpoint()
        comments_endpoint = client.get_comments_endpoint()

        # add a post
        post_request_body = posts_endpoint.build_random_post()
        post_response_body = (posts_endpoint
                              .create_post(body=post_request_body))
        created_post_id = post_response_body.json()['id']
        post_get_response = posts_endpoint.get_post_by_id(created_post_id)
        (assert_that(post_get_response.status_code)
         .is_equal_to(requests.codes.ok))

        # add a comment to a post
        comment_request_body = comments_endpoint.build_random_comment()
        comment_response_body = (comments_endpoint.create_comment_for_post(
            body=comment_request_body, post_id=created_post_id))
        created_comment_id = comment_response_body.json()['id']
        comment_get_response = (comments_endpoint.get_comment(
            comment_id=created_comment_id))
        (assert_that(comment_get_response.status_code)
         .is_equal_to(requests.codes.ok))

        # TODO - In reality, the comment and post instance are not created,
        #  so not sure how to complete the e2e test and delete the created resources
        # delete a post
        posts_endpoint.delete_post_by_id(created_post_id)

        # assert there is no post
        post_get_response = (posts_endpoint
                             .get_post_by_id(created_post_id))
        (assert_that(post_get_response.status_code)
         .is_equal_to(requests.codes.not_found))

        # assert there is no comment
        comment_get_response = (comments_endpoint
                                .get_comment(created_comment_id))
        (assert_that(comment_get_response.status_code)
        .is_equal_to(requests.codes.not_found))




