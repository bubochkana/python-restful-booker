"""Logging configuration manager.

This module provides a centralized utility for initializing and
configuring application-wide logging using a dictionary-based
configuration.
"""
import logging.config
from logging import Logger


class LoggingManager:
    """Utility class for initializing application logging.

    This class encapsulates logging configuration logic and applies
    dictionary-based logging settings to the Python logging framework.
    """
    @staticmethod
    def init_logger(configurations: dict) -> Logger:
        """Initialize and configure the logging system.

        Applies the provided logging configuration using
        ``logging.config.dictConfig`` and returns a logger instance.

        Args:
            configurations: Dictionary containing logging configuration
                compatible with ``logging.config.dictConfig``.

        Returns:
            Logger: Configured logger instance.
        """
        logging.config.dictConfig(configurations)
        return logging.getLogger(__name__)


