"""Logging utilities for masking sensitive data in log output."""
import logging
import re

sensitive_keys = (
    "headers",
    "credentials",
    "Authorization",
    "token",
    "password",
)
regex_patterns = [
    # JSON: {"token": "value"}
    (re.compile(r'("token"\s*:\s*")[^"]+(")'), r'\1*****\2'),
    # Cookie: token=value (inside headers)
    (re.compile(r'(\btoken=)[^;,\s]+'), r'\1*****'),
]


class SensitiveDataFilter(logging.Filter):
    """Logging filter that masks sensitive information in log records.

    This filter intercepts log records and replaces sensitive values
    such as authentication tokens, credentials, and authorization data
    before they are emitted. Masking is applied both to structured
    arguments (e.g. dictionaries) and to string messages using
    configurable regular-expression patterns.

    The filter is designed to prevent accidental leakage of sensitive
    data in application logs while preserving log structure and
    readability.
    """
    patterns = regex_patterns
    sensitive_keys = sensitive_keys

    def __init__(self):
        """Initialize the sensitive data filter.

        Calls the base ``logging.Filter`` initializer and prepares the
        filter instance for use with configured handlers.
        """
        super().__init__()

    def filter(self, record):
        """Apply masking to a log record.

        This method is called by the logging framework for each log
        record. It masks sensitive information in both the message and
        the arguments of the record before it is emitted.

        Args:
            record: The log record to be processed and potentially
                modified.

        Returns:
            bool: Always returns ``True`` so that the record is not
            filtered out, only sanitized.
        """
        try:
            record.args = self.mask_sensitive_args(record.args)
            record.msg = self.mask_sensitive_msg(record.msg)
            return True
        except Exception:
            return True

    def mask_sensitive_args(self, args):
        """Mask sensitive values inside the record's argument container.

        If the arguments are provided as a dictionary, keys listed in
        ``sensitive_keys`` are fully masked and other values are passed
        through ``mask_sensitive_msg`` for recursive masking. If the
        arguments are a tuple or other iterable, each element is
        processed individually.

        Args:
            args: The log record arguments, typically a dict or tuple,
                which may contain sensitive data.

        Returns:
            Any: A new arguments container (dict or tuple) with
            sensitive values masked.
        """
        if isinstance(args, dict):
            new_args = args.copy()
            for key in args.keys():
                if key in sensitive_keys:
                    new_args[key] = "******"
                else:
                    new_args[key] = self.mask_sensitive_msg(args[key])
            return new_args
        return tuple([self.mask_sensitive_msg(arg) for arg in args])

    def mask_sensitive_msg(self, message):
        """Mask sensitive data inside a message value.

        If the message is a dictionary, it is delegated to
        ``mask_sensitive_args`` for key-based masking. If the message is
        a string, regular-expression patterns and configured
        ``sensitive_keys`` are used to replace sensitive substrings
        (such as tokens, cookies, and passwords) with masked values.

        Args:
            message: The message to inspect and mask. Can be a dict,
                string, or any other type.

        Returns:
            Any: The masked message. The original type is preserved
            where possible (e.g. dict remains dict, str remains str).
        """
        if isinstance(message, dict):
            return self.mask_sensitive_args(message)
        if isinstance(message, str):
            for pattern, repl in self.patterns:
                message = pattern.sub(repl, message)
            for key in self.sensitive_keys:
                pattern_str = rf"'{key}': '[^']+'"
                replace = f"'{key}': '******'"
                message = re.sub(pattern_str, replace, message)
        return message

