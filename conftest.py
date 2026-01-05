import pytest

from src.clients.booking.booking_client import BookingClient
from src.clients.json_placeholder.comments_client import CommentsClient
from src.clients.json_placeholder.posts_client import PostsClient
from src.helpers.booking_helper import BookingHelper


@pytest.fixture
def booking_client():
    return BookingClient()


@pytest.fixture
def booking_helper():
    return BookingHelper()

@pytest.fixture
def posts_client():
    return PostsClient()

@pytest.fixture
def comments_client():
    return CommentsClient()

