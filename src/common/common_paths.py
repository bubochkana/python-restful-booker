"""Common filesystem path utilities.

This module provides reusable helpers for resolving project-level paths,
such as the project root directory and environment-specific configuration
file locations.
"""

from pathlib import Path
from typing import Literal

EnvName = Literal["dev", "qa"]


class CommonPaths:
    """Utility class for resolving common filesystem paths.

    This class contains static helper methods for determining
    project paths, including the project root and environment-specific
    configuration files.
    """

    @staticmethod
    def project_root() -> Path:
        """Return the project root directory path.

        The project root is resolved dynamically based on the current file
        location to avoid hardcoding absolute paths.

        Returns:
            Path: Absolute path to the project root directory.
        """
        return Path(__file__).resolve().parent.parent.parent

    @staticmethod
    def env_config_file_path(env: EnvName) -> Path:
        """Return the path to the environment-specific configuration file.

        The configuration file is expected to be located under:
        `src/resources/<env>/<env>_configs.yaml`.

        Args:
            env (EnvName): Environment name (e.g., "dev" or "qa").

        Returns:
            Path: Absolute path to the environment configuration YAML file.
        """
        filename = f"{env}_configs.yaml"
        return CommonPaths.project_root().joinpath("src").joinpath("resources").joinpath(f"{env}").joinpath(filename)
