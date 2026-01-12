import random

import requests
from faker import Faker
from requests import Response

from src.endpoints.json_placeholder.users_endpoint import UsersEndpoint
from src.models.json_placeholder.posts.post_model import PostModel


class PostsEndpoint:
    def __init__(self, host: str):
        self.host = host
        self.users_endpoint = UsersEndpoint(host)

    def get_all_posts(self) -> Response:
        return requests.get(f"{self.host}/posts")

    def get_post_by_id(self, post_id) -> Response:
        return requests.get(f"{self.host}/posts/{post_id}")

    def get_all_comments_for_the_post_id(self, post_id) -> Response:
        return requests.get(f"{self.host}/posts/{post_id}/comments")

    def create_post(self, body: PostModel) -> Response:
        return requests.post(f"{self.host}/posts", json=body.model_dump())

    def delete_post_by_id(self, post_id) -> Response:
        return requests.delete(f"{self.host}/posts/{post_id}")

    def update_whole_post_by_id(self, body: PostModel, post_id) -> Response:
        return requests.put(
            f"{self.host}/posts/{post_id}",
            json=body.model_dump())

    def update_partially_post_by_id(self, body: PostModel, post_id) -> Response:
        return requests.patch(f"{self.host}/posts/{post_id}", json=body)

    def pick_random_post_id(self) -> int:
        posts_ids_list = self.get_all_posts()
        my_obj_list: list[PostModel] \
            = [PostModel(**dict_item) for dict_item in posts_ids_list.json()]
        return random.choice(my_obj_list).id

    def build_random_post(self) -> PostModel:
        faker: Faker = Faker()
        random_user_id = self.users_endpoint.pick_random_user_id()
        return PostModel(
            title=faker.text(max_nb_chars=20),
            body=faker.text(max_nb_chars=100),
            userId=random_user_id)
