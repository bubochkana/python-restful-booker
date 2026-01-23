"""Base abstraction for HTTP endpoint clients.

This module provides a common base class for API endpoint implementations.
It centralizes HTTP request execution, logging, and masking of sensitive
data in request and response payloads.
"""
import json
import logging.config

import requests
from requests import Response


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

    def _pretty_json_or_text(self, body) -> str:
        """Convert a request or response body into a human-readable string.

        The return value is suitable for logging. If the body is a dictionary
        or list, it attempts to serialize it into a pretty-printed JSON string
        with indentation. If serialization fails, it falls back to a simple
        string representation.

        If the body is empty (``None`` or an empty string), a placeholder
        message is returned.

        Args:
        body: The request or response body. Can be a dict, list, string,
            or None.

        Returns:
        str: A formatted string representation of the body that is safe to
        include in logs.
        """
        if body is None or body == "":
            return ""

        if isinstance(body, (dict, list)):
            try:
                return json.dumps(body, indent=4)
            except (TypeError, ValueError) as e:
                self.logger.debug("Failed to serialize", e)
                return ""
        return str(body)

    def request(self, method, url, expected_status_code=None, *args, **kwargs):
        """Execute an HTTP request and log request and response details.

            This method sends an HTTP request using the ``requests`` library,
            optionally validates the response status code, formats request and
            response bodies into a human-readable form, and logs headers and
            bodies for debugging and traceability.

            Request and response bodies are safely formatted for logging:
            - JSON objects and arrays are pretty-printed
            - Empty bodies are handled gracefully
            - Non-JSON content is logged as plain text

        Args:
                method: HTTP method to use (e.g. ``"GET"``, ``"POST"``, ``"PUT"``,
                    ``"DELETE"``).
                url: Target URL for the request.
                expected_status_code: Optional expected HTTP status code. If
                    provided and the actual response status code differs, an
                    exception is raised.
                *args: Positional arguments forwarded to ``requests.request``.
                **kwargs: Keyword arguments forwarded to ``requests.request``
                    (e.g. headers, params, json, data).

        Returns:
                requests.Response: The HTTP response object returned by
                ``requests.request``.

        Raises:
        Exception: If ``expected_status_code`` is provided and the actual
        response status code does not match the expected value.
        """
        response = requests.request(method, url, *args, **kwargs)

        if expected_status_code is not None and response.status_code != expected_status_code:
            raise Exception(
                f"Expected status code {expected_status_code}, but got {response.status_code}"
            )

        request_headers = dict(response.request.headers or {})
        response_headers = dict(response.headers or {})

        formatted_request_body = self._pretty_json_or_text(response.request.body)
        try:
            response_obj = response.json()
            formatted_response_body = self._pretty_json_or_text(response_obj)
        except Exception:
            formatted_response_body = self._pretty_json_or_text(response.text)


        self.logger.info(f"{method} {url} - {response.status_code}")
        # TODO - mask sensitive information
        self.logger.debug(f"Request Headers: {request_headers}")
        #TODO - mask sensitive information
        self.logger.debug(f"Request Body: {formatted_request_body}")
        self.logger.debug(f"`Response` Headers: {response_headers}")
        # TODO - mask sensitive information
        self.logger.debug(f"Response Body: {formatted_response_body}")
        return response


