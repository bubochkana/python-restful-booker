"""Pydantic models for post-related API data.

This module defines Pydantic models representing post entities and
collections of posts returned by the JsonPlaceholder API.
"""

from typing import List

from pydantic import BaseModel, ConfigDict, Field, RootModel


class PostModel(BaseModel):
    """Model representing a single post.

    This model maps post-related fields between Python attribute
    names and API field aliases.
    """

    model_config = ConfigDict(populate_by_name=True)

    userId: int = Field(alias="userId")
    id: int = Field(alias="id", default=None)
    title: str = Field(alias="title")
    body: str = Field(alias="body")


class PostsListingModel(RootModel[List[PostModel]]):
    """Model representing a list of posts.

    This root model wraps a list of PostModel instances returned by
    the API when multiple posts are retrieved.
    """

    pass
