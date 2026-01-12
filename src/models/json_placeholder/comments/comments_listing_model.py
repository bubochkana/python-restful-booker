from typing import List

from pydantic import RootModel

from src.models.json_placeholder.comments.comment_model import CommentModel

class CommentsListingModel(RootModel[List[CommentModel]]):
    pass
