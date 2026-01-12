import random

import requests
from faker import Faker

from src.endpoints.json_placeholder.posts_endpoint import PostsEndpoint
from src.models.json_placeholder.comments.comment_model import CommentModel


class CommentsEndpoint:
    def __init__(self, host: str):
        self.host = host
        self.posts_endpoint = PostsEndpoint(host)

    def get_all_comments_by_post_id(self, post_id):
        return requests.get(f"{self.host}/comments?postId={post_id}")

    def get_comment(self, comment_id):
        return requests.get(f"{self.host}/comments?comment_id={comment_id}")

    def create_comment_for_post(self, body: CommentModel, post_id):
        return requests.post(
            f"{self.host}/posts/{post_id}/comments",
            json=body.model_dump())

    def delete_post_by_id(self, post_id):
        return requests.delete(f"{self.host}/posts/{post_id}")

    def pick_random_comment_id_for_post(self, post_id) -> str:
        comments_for_post_id_list = self.get_all_comments_by_post_id(post_id)
        my_obj_list: list[CommentModel] \
            = [CommentModel(**dict_item) for dict_item in comments_for_post_id_list.json()]
        return str(random.choice(my_obj_list).id)

    def build_random_comment(self) -> CommentModel:
        faker: Faker = Faker()
        random_post_id = self.posts_endpoint.pick_random_post_id()
        return CommentModel(
            postId=random_post_id,
            name=faker.name(),
            email=faker.email(),
            body=faker.text(max_nb_chars=100))
