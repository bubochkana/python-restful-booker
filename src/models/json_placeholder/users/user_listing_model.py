from pydantic import BaseModel


class UserListingModel(BaseModel):
    userId: int
    id: int
    title: str
    body: str