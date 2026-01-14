from typing import List

from pydantic import BaseModel, RootModel, ConfigDict, Field


class CommentModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    postId: int
    id: int = Field(default = None)
    name: str
    email: str
    body: str

class CommentsListingModel(RootModel[List[CommentModel]]):
    pass
