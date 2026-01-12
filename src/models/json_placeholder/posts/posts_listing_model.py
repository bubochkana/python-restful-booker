from typing import List

from pydantic import RootModel

from src.models.json_placeholder.posts.post_model import PostModel


class PostsListingModel(RootModel[List[PostModel]]):
    pass
