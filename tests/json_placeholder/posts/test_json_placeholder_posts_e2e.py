import requests
from assertpy import assert_that

from src.actions.json_placeholder_actions import JsonPlaceholderActions
from src.clients.json_placeholder.json_placeholder_client import JsonPlaceholderClient
from src.models.json_placeholder.comments.comment_model import CommentModel, CommentsListingModel


class TestJsonPlaceholderCommentsE2E:
    def test_add_post_add_comment_delete_post_e2e(self):
        actions = JsonPlaceholderActions()

        # add a post
        created_post = actions.add_post()
        post_id = created_post.id

        # get created post
        actions.get_post(post_id)

        # add a comment to a post
        created_comment = actions.add_comment(post_id)
        comment_id = created_comment.id

        # In reality, the comment and post instances are not created,
        # so the created post is not deleted
        actions.delete_post(post_id)

        # assert there is no post
        post_get_response = JsonPlaceholderClient().posts_endpoint().get_post_by_id(post_id)
        assert_that(post_get_response.status_code).is_equal_to(requests.codes.not_found)

        # assert there is no comment
        comment_get_response = JsonPlaceholderClient().comments_endpoint().get_comment(comment_id)
        assert_that(comment_get_response.status_code).is_equal_to(requests.codes.not_found)

    def test_add_post_no_comments_delete_post_e2e(self):
        actions = JsonPlaceholderActions()

        # add a post
        created_post = actions.add_post()
        post_id = created_post.id

        # confirm newly created post has 0 comments
        get_comments_response = JsonPlaceholderClient().comments_endpoint().get_all_comments_by_post_id(post_id)
        comments_list = CommentsListingModel.model_validate(get_comments_response.json())
        assert_that(comments_list.root).is_empty()

        # In reality, the comment and post instances are not created,
        # so the created post is not deleted
        actions.delete_post(post_id)

        # assert there is no post
        post_get_response = JsonPlaceholderClient().posts_endpoint().get_post_by_id(post_id)
        assert_that(post_get_response.status_code).is_equal_to(requests.codes.not_found)

    def test_add_post_add_comment_delete_comment_e2e(self):
        actions = JsonPlaceholderActions()

        # add a post
        created_post = actions.add_post()
        post_id = created_post.id

        # get created post
        actions.get_post(post_id)

        # add a comment to a post
        created_comment = actions.add_comment(post_id)
        comment_id = created_comment.id

        # In reality, the comment and post instances are not created,
        # so the created comment is not deleted
        actions.delete_comment(comment_id)

        # assert there is a post
        post_get_response = JsonPlaceholderClient().posts_endpoint().get_post_by_id(post_id)
        assert_that(post_get_response.status_code).is_equal_to(requests.codes.not_found)

        # assert there is no comment
        comment_get_response = JsonPlaceholderClient().comments_endpoint().get_comment(comment_id)
        assert_that(comment_get_response.status_code).is_equal_to(requests.codes.not_found)
