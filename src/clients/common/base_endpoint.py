"""Base abstractions for HTTP API endpoint clients.

This module defines a common base class used by API endpoint implementations
to perform HTTP requests via ``requests.Session``. It centralizes request
execution, optional status-code validation, and structured logging of request
and response metadata to support debugging and test diagnostics.

Endpoint-specific clients should inherit from the provided base class and
use its helper methods instead of calling ``requests`` directly.
"""
import json
import logging.config

from requests import Response, Session


class AbstractionEndpoint:
    """Base abstraction for HTTP API endpoint clients.

    This class provides a common foundation for implementing API endpoint
    wrappers on top of ``requests.Session``. It centralizes HTTP request
    execution, optional status-code validation, and structured logging of
    request and response data.

    Endpoint-specific classes should inherit from this base class and use
    its request helpers rather than calling ``requests`` directly.
    """
    def __init__(self, session: Session = None):
        """Base abstraction for HTTP API endpoint clients.

        This class provides a common foundation for implementing API endpoint
        wrappers on top of ``requests.Session``. It centralizes HTTP request
        execution, optional status-code validation, and structured logging of
        request and response data.

        Endpoint-specific classes should inherit from this base class and use
        its request helpers rather than calling ``requests`` directly.
        """
        self.session = session or Session()
        self.logger = logging.getLogger(self.__class__.__name__)

    def post(self, *args, **kwargs) -> Response:
        """Send an HTTP POST request.

        This is a convenience wrapper around the generic ``request`` method.

        Args:
            *args: Positional arguments forwarded to ``request``.
            **kwargs: Keyword arguments forwarded to ``request``.

        Returns:
            Response: The HTTP response returned by the server.
        """
        return self.request('POST', *args, **kwargs)

    def get(self, url, *args, **kwargs) -> Response:
        """Send an HTTP GET request.

        Args:
            url: Target URL for the request.
            *args: Additional positional arguments forwarded to ``request``.
            **kwargs: Additional keyword arguments forwarded to ``request``.

        Returns:
            Response: The HTTP response returned by the server.
        """
        return self.request('GET', url, *args, **kwargs)

    def put(self, url, *args, **kwargs) -> Response:
        """Send an HTTP PUT request.

        Args:
            url: Target URL for the request.
            *args: Additional positional arguments forwarded to ``request``.
            **kwargs: Additional keyword arguments forwarded to ``request``.

        Returns:
            Response: The HTTP response returned by the server.
        """
        return self.request('PUT', url, *args, **kwargs)

    def patch(self, url, *args, **kwargs) -> Response:
        """Send an HTTP PATCH request.

        Args:
            url: Target URL for the request.
            *args: Additional positional arguments forwarded to ``request``.
            **kwargs: Additional keyword arguments forwarded to ``request``.

        Returns:
            Response: The HTTP response returned by the server.
        """
        return self.request('PATCH', url, *args, **kwargs)

    def delete(self, url, *args, **kwargs) -> Response:
        """Send an HTTP DELETE request.

        Args:
            url: Target URL for the request.
            *args: Additional positional arguments forwarded to ``request``.
            **kwargs: Additional keyword arguments forwarded to ``request``.

        Returns:
            Response: The HTTP response returned by the server.
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
        """Execute an HTTP request using the configured session.

        This method sends the request via the underlying session, optionally
        validates the expected HTTP status code, and logs request and response
        details for diagnostic purposes.

        Args:
            method: HTTP method name (e.g. ``"GET"``, ``"POST"``).
            url: Target URL for the request.
            expected_status_code: Optional expected HTTP status code. If
                provided and the response status does not match, an exception
                is raised.
            *args: Additional positional arguments forwarded to
                ``requests.Session.request``.
            **kwargs: Additional keyword arguments forwarded to
                ``requests.Session.request``.

        Returns:
            Response: The HTTP response returned by the server.

        Raises:
            Exception: If ``expected_status_code`` is provided and the actual
                response status code does not match.
        """
        response = self.session.request(method, url, *args, **kwargs)

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
        self.logger.debug(f"Request Headers: {request_headers}")
        self.logger.debug(f"Request Body: {formatted_request_body}")
        self.logger.debug(f"`Response` Headers: {response_headers}")
        self.logger.debug(f"Response Body: {formatted_response_body}")
        return response




