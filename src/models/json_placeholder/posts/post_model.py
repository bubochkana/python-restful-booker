from typing import Optional

from pydantic import BaseModel


class PostModel(BaseModel):
    userId: int
    id: Optional[int] = None
    title: str
    body: str
