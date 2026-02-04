"""Authenticated HTTP session for booking API access.

This module defines an authenticated HTTP session that extends
``requests.Session`` to support token-based authentication against the
booking API. The session is responsible for acquiring, caching, and
injecting authentication tokens into outgoing requests transparently.

Authentication is performed via the ``/auth`` endpoint using configured
credentials, and the resulting token is attached to subsequent requests
as an HTTP cookie. The session is designed to be shared across endpoint
clients that require authenticated access.
"""
from datetime import datetime

import requests
from requests import PreparedRequest, Request, Session

from src.configs.booking_config_model import BookingEnvironmentConfig


class AuthEndpoint(Session):
    """Authenticated HTTP session for booking API requests.

    This class extends ``requests.Session`` to handle authentication against the
    booking service using a token obtained from the ``/auth`` endpoint. The token
    is retrieved using configured credentials and stored internally for reuse
    across subsequent requests.

    The authentication token is injected into outgoing requests by updating the
    session headers with a cookie entry (``Cookie: token=<value>``). Token
    generation and refresh are handled transparently before requests are sent.
    """
    def __init__(self, config: BookingEnvironmentConfig):
        """Initialize the authenticated session.

        Stores authentication credentials and API host information from the
        provided environment configuration. No authentication request is made
        during initialization; the token is generated lazily when the first
        authenticated request is prepared.

        Args:
            config: Booking environment configuration containing the API host,
                username, and password required for authentication.
        """
        super().__init__()

        self._host = config.host
        self._username = config.username
        self._password = config.password
        self._token = None
        self._expiration = None
        self._auth_url = f"{self._host}/auth"

    def _generate_token(self) -> str:
        """Generate a new authentication token.

        Sends a POST request to the authentication endpoint using the configured
        credentials. The returned token is cached and added to the session headers
        as a cookie so it is automatically included in subsequent requests.

        Returns:
            str: The generated authentication token.
        """
        headers = {"Content-Type": "application/json"}
        body = {"username": self._username, "password": self._password}

        response = requests.post(
            url=self._auth_url,
            json=body,
            headers=headers)

        try:
            self._token = response.json()["token"]
        except Exception as e:
            raise RuntimeError(f'Auth token not found in response: {response.json()["reason"]}') from e

        self._token = response.json()["token"]
        self.headers.update({"Cookie": f'token={self._token}'})

        return self._token

    def _is_token_refresh_needed(self):
        """Determine whether the authentication token must be refreshed.

        A refresh is required if no token has been generated yet, if no expiration
        time is set, or if the current time is past the stored expiration.

        Returns:
            bool: ``True`` if a new token should be generated, otherwise ``False``.
        """
        if self._token is None:
            return True
        return False

    def prepare_request(self, request: Request) -> PreparedRequest:
        """Prepare an outgoing HTTP request.

        Ensures that a valid authentication token is available before the request
        is sent. If necessary, a new token is generated and injected into the
        session headers. The request is then prepared using the base
        ``requests.Session`` implementation.

        Args:
            request: The request object to be prepared.

        Returns:
            PreparedRequest: The prepared request ready to be sent.
        """
        if self._is_token_refresh_needed():
            self._token = self._generate_token()
        return super().prepare_request(request)

