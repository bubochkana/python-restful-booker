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

        # add a comment to a post
        comment_request_body = comments_endpoint.build_random_comment()
        comment_response_body = (comments_endpoint.create_comment_for_post(
            body=comment_request_body, post_id=created_post_id))
        created_comment_id = comment_response_body.json()['id']




