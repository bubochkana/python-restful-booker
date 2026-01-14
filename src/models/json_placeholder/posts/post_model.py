from typing import List

from pydantic import BaseModel, RootModel, ConfigDict, Field


class PostModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    userId: int
    id: int  = Field(default = None)
    title: str
    body: str

class PostsListingModel(RootModel[List[PostModel]]):
    pass