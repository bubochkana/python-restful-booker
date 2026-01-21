"""Pytest configuration and custom command-line options.

This module defines custom pytest hooks for extending command-line
options and initializing environment-specific configuration before
test execution.
"""
import yaml

from src.common.common_paths import CommonPaths
from src.common.logging_manager import LoggingManager
from src.utils.env_loader import EnvLoader


def pytest_addoption(parser):
    """Add custom command-line options to pytest.

    This hook adds the ``--env`` option, allowing the user to specify
    the target environment for test execution.

    Args:
        parser: Pytest command-line option parser.
    """
    parser.addoption("--env", action="store", default="qa", help="Environment name")


def pytest_configure(config):
    """Configure pytest before test execution.

    This hook initializes the environment configuration based on the
    value of the ``--env`` command-line option. The configuration is
    loaded once and shared across the test session.

    Args:
        config: Pytest configuration object.
    """
    with open(CommonPaths.log_config_file_path(), "r") as logs_config_file:
        logs_config = yaml.safe_load(logs_config_file)
    LoggingManager.init_logger(logs_config)

    testing_env = config.getoption("env")
    EnvLoader(test_env=testing_env)
