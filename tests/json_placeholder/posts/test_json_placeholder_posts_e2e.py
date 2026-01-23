import requests
from assertpy import assert_that

from src.actions.json_placeholder_actions import JsonPlaceholderActions
from src.clients.json_placeholder.json_placeholder_client import JsonPlaceholderClient
from src.models.json_placeholder.comments.comment_model import CommentModel, CommentsListingModel
from src.models.json_placeholder.posts.post_model import PostModel


class TestJsonPlaceholderCommentsE2E:
    def test_add_post_add_comment_delete_post_e2e(self):
        # client = JsonPlaceholderClient()
        # posts_endpoint = client.posts_endpoint()
        # comments_endpoint = client.comments_endpoint()
        actions = JsonPlaceholderActions()

        # add a post
        # post_request_body = posts_endpoint.build_random_post()
        # post_response_body = posts_endpoint.create_post(body=post_request_body)
        # created_post_model = PostModel(**post_response_body.json())
        # created_post_id = created_post_model.id
        created_post = actions.add_post()
        post_id = created_post.id

        # get created post
        post_get_response = actions.posts_endpoint.get_post_by_id(post_id)
        assert_that(post_get_response.status_code).is_equal_to(requests.codes.ok)

        # add a comment to a post
        created_comment = actions.add_comment(post_id)
        comment_id = created_comment.id

        # In reality, the comment and post instances are not created,
        # so the created post is not deleted
        actions.delete_post(post_id)

        # assert there is no post
        post_get_response = actions.posts_endpoint.get_post_by_id(post_id)
        assert_that(post_get_response.status_code).is_equal_to(requests.codes.not_found)

        # assert there is no comment
        comment_get_response = actions.comments_endpoint.get_comment(comment_id)
        assert_that(comment_get_response.status_code).is_equal_to(requests.codes.not_found)

    def test_add_post_no_comments_delete_post_e2e(self):
        # client = JsonPlaceholderClient()
        # posts_endpoint = client.posts_endpoint()
        # comments_endpoint = client.comments_endpoint()
        actions = JsonPlaceholderActions()

        # add a post
        # post_request_body = posts_endpoint.build_random_post()
        # post_response_body = posts_endpoint.create_post(body=post_request_body)
        # created_post_model = PostModel(**post_response_body.json())
        # created_post_id = created_post_model.id
        created_post = actions.add_post()
        post_id = created_post.id

        # confirm new create post has 0 comments
        get_comments_response = actions.comments_endpoint.get_all_comments_by_post_id(post_id)
        comments_list = CommentsListingModel.model_validate(get_comments_response.json())
        assert_that(comments_list.root).is_empty()

        # In reality, the comment and post instances are not created,
        # so the created post is not deleted
        actions.delete_post(post_id)

        # assert there is no post
        post_get_response = actions.posts_endpoint.get_post_by_id(post_id)
        assert_that(post_get_response.status_code).is_equal_to(requests.codes.not_found)

    def test_add_post_add_comment_delete_comment_e2e(self):
        # client = JsonPlaceholderClient()
        # posts_endpoint = client.posts_endpoint()
        # comments_endpoint = client.comments_endpoint()
        actions = JsonPlaceholderActions()

        # add a post
        # post_request_body = posts_endpoint.build_random_post()
        # post_response_body = posts_endpoint.create_post(body=post_request_body)
        # created_post_model = PostModel(**post_response_body.json())
        # created_post_id = created_post_model.id
        created_post = actions.add_post()
        post_id = created_post.id

        # get created post
        post_get_response = actions.posts_endpoint.get_post_by_id(post_id)
        assert_that(post_get_response.status_code).is_equal_to(requests.codes.ok)

        # add a comment to a post
        # comment_request_body = comments_endpoint.build_random_comment()
        # comment_response_body = comments_endpoint.create_comment_for_post(
        #     body=comment_request_body, post_id=created_post_id
        # )
        # created_comment_model = CommentModel(**comment_response_body.json())
        # created_comment_id = created_comment_model.id
        # comment_get_response = comments_endpoint.get_comment(comment_id=created_comment_id)
        # assert_that(comment_get_response.status_code).is_equal_to(requests.codes.ok)
        created_comment = actions.add_comment(post_id)
        comment_id = created_comment.id

        # In reality, the comment and post instances are not created,
        # so the created comment is not deleted
        actions.delete_comment(comment_id)

        # assert there is a post
        post_get_response = actions.posts_endpoint.get_post_by_id(post_id)
        assert_that(post_get_response.status_code).is_equal_to(requests.codes.ok)

        # assert there is no comment
        comment_get_response = actions.comments_endpoint.get_comment(comment_id)
        assert_that(comment_get_response.status_code).is_equal_to(requests.codes.not_found)
