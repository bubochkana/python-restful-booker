import requests


class CommentsEndpoint:
    def __init__(self, host: str):
        self.host = host

    def ger_all_comments_by_post_id(self, post_id):
        return requests.get(f"{self.host}/comments?postId={post_id}")
