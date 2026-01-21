"""Base abstraction for HTTP endpoint clients.

This module provides a common base class for API endpoint implementations.
It centralizes HTTP request execution, logging, and masking of sensitive
data in request and response payloads.
"""
import json
import logging.config

import requests
from requests import Response

from src.common.sensitive_data_filter import SensitiveDataFilter


class AbstractionEndpoint:
    """Base abstraction for HTTP endpoint clients.

    This module provides a common base class for API endpoint implementations.
    It centralizes HTTP request execution, logging, and masking of sensitive
    data in request and response payloads.
    """
    def __init__(self):
        """Base class for API endpoint implementations.

        This class provides common HTTP verb helpers and a unified request
        handler that includes logging and masking of sensitive information
        such as authentication tokens.
        """
        self.logger = logging.getLogger(self.__class__.__name__)

    def post(self, *args, **kwargs) -> Response:
        """Send an HTTP POST request.

        This method delegates to the generic request handler using the
        POST HTTP method.

        Args:
            *args: Positional arguments forwarded to the request handler.
            **kwargs: Keyword arguments forwarded to the request handler.

        Returns:
            Response: HTTP response returned by the request.
        """
        return self.request('POST', *args, **kwargs)

    def get(self, url, *args, **kwargs) -> Response:
        """Send an HTTP GET request.

        This method delegates to the generic request handler using the
        GET HTTP method.

        Args:
            url: Target URL for the request.
            *args: Positional arguments forwarded to the request handler.
            **kwargs: Keyword arguments forwarded to the request handler.

        Returns:
            Response: HTTP response returned by the request.
        """
        return self.request('GET', url, *args, **kwargs)

    def put(self, url, *args, **kwargs) -> Response:
        """Send an HTTP PUT request.

        This method delegates to the generic request handler using the
        PUT HTTP method.

        Args:
            url: Target URL for the request.
            *args: Positional arguments forwarded to the request handler.
            **kwargs: Keyword arguments forwarded to the request handler.

        Returns:
            Response: HTTP response returned by the request.
        """
        return self.request('PUT', url, *args, **kwargs)

    def patch(self, url, *args, **kwargs) -> Response:
        """Send an HTTP PATCH request.

        This method delegates to the generic request handler using the
        PATCH HTTP method.

        Args:
            url: Target URL for the request.
            *args: Positional arguments forwarded to the request handler.
            **kwargs: Keyword arguments forwarded to the request handler.

        Returns:
            Response: HTTP response returned by the request.
        """
        return self.request('PATCH', url, *args, **kwargs)

    def delete(self, url, *args, **kwargs) -> Response:
        """Send an HTTP DELETE request.

        This method delegates to the generic request handler using the
        DELETE HTTP method.

        Args:
            url: Target URL for the request.
            *args: Positional arguments forwarded to the request handler.
            **kwargs: Keyword arguments forwarded to the request handler.

        Returns:
            Response: HTTP response returned by the request.
        """
        return self.request('DELETE', url, *args, **kwargs)

    def request(self, method, url, expected_status_code=None, *args, **kwargs):
        """Execute an HTTP request and log request/response details.

        Sends an HTTP request using the specified method, optionally
        validates the response status code, masks sensitive data, and
        logs formatted request and response information.

        Args:
            method: HTTP method to use (e.g., "GET", "POST").
            url: Target URL for the request.
            expected_status_code: Optional expected HTTP status code.
                If provided and the actual status code differs, an
                exception is raised.
            *args: Positional arguments forwarded to ``requests.request``.
            **kwargs: Keyword arguments forwarded to ``requests.request``.

        Returns:
            Response: HTTP response returned by the request.

        Raises:
            Exception: If an expected status code is provided and the
                response status code does not match.
        """
        response = requests.request(method, url, *args, **kwargs)
        if expected_status_code and response.status_code != expected_status_code:
            raise Exception(
                f"Expected status code {expected_status_code}, but got {response.status_code}")

        request_headers = dict(response.request.headers)
        masked_request_headers = SensitiveDataFilter().mask_token_in_headers(request_headers)

        if response.request.body is None:
            formatted_request_body = ""
            return formatted_request_body
        else:
            formatted_request_body = json.dumps(json.loads(response.request.body), indent=4)
        # formatted_request_body = JsonFormatter.format_request_body(response.request.body)

        response_headers = dict(response.headers)
        masked_response_headers = SensitiveDataFilter().mask_token_in_headers(response_headers)

        response_body = dict(response.json())
        masked_response_body = SensitiveDataFilter().mask_token_in_response(response_body)
        formatted_response_body = json.dumps(masked_response_body, indent=4)

        self.logger.info(f"{method} {url} - {response.status_code}")

        self.logger.debug(f"Request Headers: {masked_request_headers}")
        # [DEBUG] Request Body: {response.request.body}  --  pretty json
        # self.logger.debug(f"Request Body: {response.request.body}")
        self.logger.debug(f"Request Body: {formatted_request_body}")

        self.logger.debug(f"`Response` Headers: {masked_response_headers}")
        # [DEBUG] Response Body: {response.text}  -- pretty json
        # self.logger.debug(f"Response Body: {response.text}")
        # self.logger.debug(f"Response Body: {masked_response_body}")
        self.logger.debug(f"Response Body: {formatted_response_body}")

        return response



