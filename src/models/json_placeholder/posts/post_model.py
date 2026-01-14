from typing import List

from pydantic import BaseModel, RootModel, ConfigDict, Field


class PostModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    userId: int = Field(alias = "userId")
    id: int  = Field(alias="id", default = None)
    title: str = Field(alias = "title")
    body: str = Field(alias = "body")

class PostsListingModel(RootModel[List[PostModel]]):
    pass