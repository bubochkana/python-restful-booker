from typing import List

from pydantic import BaseModel, ConfigDict, Field, RootModel


class CommentModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    postId: int = Field(alias = "postId")
    id: int = Field(alias="id", default = None)
    name: str = Field(alias = "name")
    email: str = Field(alias = "email")
    body: str = Field(alias = "body")

class CommentsListingModel(RootModel[List[CommentModel]]):
    pass
