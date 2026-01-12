from typing import Optional

from pydantic import BaseModel


class CommentModel(BaseModel):
    postId: int
    id: Optional[int] = None
    name: str
    email: str
    body: str
