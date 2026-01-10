from random import random

import requests

from src.models.posts.post_model import PostModel


class PostsEndpoint:
    def __init__(self, host: str):
        self.host = host

    def get_all_posts(self):
        return requests.get(f"{self.host}/posts")

    def get_post_by_id(self, post_id):
        return requests.get(f"{self.host}/posts/{post_id}")

    def get_all_comments_for_the_post_id(self, post_id):
        return requests.get(f"{self.host}/posts/{post_id}/comments")

    def create_post(self, post_model: PostModel):
        return requests.post(f"{self.host}/posts")

    def delete_post_by_id(self, post_id):
        return requests.delete(f"{self.host}/posts/{post_id}")

    def update_whole_post_by_id(self, post_id):
        return requests.put(f"{self.host}/posts/{post_id}")

    def update_partially_post_by_id(self, post_id):
        return requests.patch(f"{self.host}/posts/{post_id}")

    def pick_random_post_id(self) -> str:
        posts_ids_list = self.get_all_posts()
        my_obj_list: list[PostModel] \
            = [PostModel(**dict_item) for dict_item in posts_ids_list.json()]
        return str(random.choice(my_obj_list).id)
