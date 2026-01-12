from typing import List

from pydantic import BaseModel, RootModel


class CommentModel(BaseModel):
    postId: int
    id: int = None
    name: str
    email: str
    body: str

class CommentsListingModel(RootModel[List[CommentModel]]):
    pass
