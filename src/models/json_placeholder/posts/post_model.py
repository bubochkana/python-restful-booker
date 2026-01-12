from typing import List

from pydantic import BaseModel, RootModel


class PostModel(BaseModel):
    userId: int
    id: int = None
    title: str
    body: str

class PostsListingModel(RootModel[List[PostModel]]):
    pass