"""Pytest configuration and custom command-line options.

This module defines custom pytest hooks for extending command-line
options and initializing environment-specific configuration before
test execution.
"""

import pytest
import yaml

from src.common.common_paths import CommonPaths
from src.common.logging_manager import LoggingManager
from src.utils.env_loader import EnvLoader


def _init_logger(config) -> None:
    """Initialize and store the framework logger on the pytest config object."""
    if getattr(config, "_framework_logger", None) is not None:
        return

    with open(CommonPaths.log_config_file_path(), "r") as f:
        logs_config = yaml.safe_load(f)

    config._framework_logger = LoggingManager.init_logger(logs_config)

def pytest_addoption(parser):
    """Add custom command-line options to pytest.

    This hook adds the ``--env`` option, allowing the user to specify
    the target environment for test execution.

    Args:
        parser: Pytest command-line option parser.
    """
    parser.addoption("--env", action="store", default="qa", help="Environment name")


def pytest_configure(config):
    """Configure the pytest test session before any tests are collected or executed.

    This hook is executed once at the start of the pytest session. It is responsible
    for initializing the framework-wide logger and loading environment-specific
    configuration based on the ``--env`` command-line option.

    The logger configuration is read from the logging configuration file and
    initialized only once for the entire test run. The selected test environment
    is then loaded via ``EnvLoader`` so that tests, fixtures, and hooks can rely
    on the correct environment setup throughout the session.

    Args:
        config: Pytest configuration object providing access to command-line
                options and session-level state.
    """
    _init_logger(config)

    with open(CommonPaths.log_config_file_path(), "r") as logs_config_file:
        logs_config = yaml.safe_load(logs_config_file)
    LoggingManager.init_logger(logs_config)

    testing_env = config.getoption("env")
    EnvLoader(test_env=testing_env)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    logging = getattr(item.config, "_framework_logger", None)

    ids = []
    if report.when == "call":
        for m in item.iter_markers(name="test_case_id"):
            if "test_case_id" in m.kwargs:
                ids.append(str(m.kwargs["test_case_id"]))
            elif isinstance(m.args, list) and len(m.args) > 0:
                ids.append(str(m.args[0]))

        if not ids:
            ids = ["N/A"]

        logging.info(f'test_case_id={','.join(ids)} {report.head_line} {report.outcome.upper()}')