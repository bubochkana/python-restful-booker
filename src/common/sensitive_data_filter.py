"""Sensitive data masking utilities for logging.

This module provides a logging filter responsible for masking sensitive
data, such as authentication tokens, in request headers and response
payloads before they are written to logs.
"""
import logging
import re
from typing import Any, Dict


class SensitiveDataFilter(logging.Filter):
    """Logging filter for masking sensitive data.

    This filter provides helper methods to sanitize sensitive values
    (e.g., authentication tokens) found in HTTP request headers and
    response bodies before logging.
    """
    _cookie_token_request_headers = re.compile(r"(token=)[^;,\s]+", flags=re.IGNORECASE)
    _response_token = re.compile(r".+")

    def mask_token_in_headers(self, headers: Dict[str, Any]) -> Dict[str, Any]:
        """Mask authentication tokens in HTTP request headers.

        Specifically masks token values inside the ``Cookie`` header
        (e.g., ``token=abc123`` → ``token=******``), while preserving
        all other headers unchanged.

        Args:
            headers: Dictionary containing HTTP request headers.

        Returns:
            Dict[str, Any]: Copy of the headers with sensitive token
            values masked.
        """
        masked = {}
        for k, v in headers.items():
            if k.lower() == "cookie":
                masked[k] = self._cookie_token_request_headers.sub(r"\1******", v)
            else:
                masked[k] = v
        return masked

    def mask_token_in_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """Mask authentication tokens in a response payload.

        Replaces values of keys named ``token`` with asterisks to prevent
        sensitive data from being logged.

        Args:
            response: Dictionary representing a JSON response body.

        Returns:
            Dict[str, Any]: Copy of the response with token values masked.
        """
        masked = {}
        for k, v in response.items():
            if k.lower() == "token":
                masked[k] = self._response_token.sub("******", v)
            else:
                masked[k] = v
        return masked
