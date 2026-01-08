import pytest
from src.clients.booking_client import BookingClient
from src.utils.env_loader import EnvLoader


def pytest_addoption(parser):
    """Add options to the parser.

    :param parser: The parser.
    :return: None
    """
    parser.addoption("--env",
                     action="store",
                     default="qa",
                     help="Environment name")


def pytest_configure(config):
    """Pytest function: pytest_configure.
    Used to set configuration before all tests."""
    testing_env = config.getoption("env")
    EnvLoader(test_env=testing_env)
