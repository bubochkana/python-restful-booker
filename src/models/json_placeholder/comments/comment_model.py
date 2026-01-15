"""Pydantic models for comment-related API data.

This module defines Pydantic models representing comment entities and
collections of comments returned by the JsonPlaceholder API.
"""

from typing import List

from pydantic import BaseModel, ConfigDict, Field, RootModel


class CommentModel(BaseModel):
    """Model representing a single comment.

    This model maps comment-related fields between Python attribute
    names and API field aliases.
    """

    model_config = ConfigDict(populate_by_name=True)

    postId: int = Field(alias="postId")
    id: int = Field(alias="id", default=None)
    name: str = Field(alias="name")
    email: str = Field(alias="email")
    body: str = Field(alias="body")


class CommentsListingModel(RootModel[List[CommentModel]]):
    """Model representing a list of comments.

    This root model wraps a list of CommentModel instances returned by
    the API when multiple comments are retrieved.
    """

    pass
