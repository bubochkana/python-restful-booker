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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest hook to log test execution results together with associated test case IDs.

    This hook is executed after each phase of a test run (setup, call, teardown).
    It wraps the default pytest behavior, waits for the test report to be created,
    and processes only the actual test execution phase ("call").

    For the executed test, it collects all ``test_case_id`` markers attached to the
    test item, including markers defined at the function level and those attached
    to individual parametrized cases via ``pytest.param(..., marks=...)``.

    The hook supports both positional and keyword marker arguments, for example:
        - ``@pytest.mark.test_case_id("1234")``
        - ``@pytest.mark.test_case_id(test_case_id="1234")``

    If no ``test_case_id`` marker is present, ``"N/A"`` is used as a fallback.

    The collected test case IDs, together with the test name and execution outcome
    (PASSED / FAILED / SKIPPED), are written to the framework logger. This allows
    consistent traceability between automated tests and external test management
    systems in local runs and CI pipelines.

    Args:
        item: Pytest test item representing the test function being executed,
              including its markers and parametrization context.
        call: Pytest CallInfo object describing the current execution phase.
    """
    with open(CommonPaths.log_config_file_path(), "r") as logs_config_file:
        logs_config = yaml.safe_load(logs_config_file)
    logging = LoggingManager.init_logger(logs_config)

    outcome = yield
    report = outcome.get_result()
    ids = []
    if report.when == "call":
        for m in item.iter_markers(name="test_case_id"):
            if "test_case_id" in m.kwargs:
                ids.append(str(m.kwargs["test_case_id"]))
            elif m.args:
                ids.append(str(m.args[0]))

        if not ids:
            ids = ["N/A"]

        logging.info(f'test_case_id={','.join(ids)} {report.head_line} {report.outcome.upper()}')