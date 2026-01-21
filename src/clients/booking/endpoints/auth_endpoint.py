"""Authentication endpoint client.

This module provides an endpoint wrapper responsible for authenticating
against the booking service and retrieving an authorization token.
"""
from src.clients.common.base_endpoint import AbstractionEndpoint


class AuthEndpoint(AbstractionEndpoint):
    """Authentication endpoint client.

    This class handles authentication requests to the booking service
    using provided user credentials and returns an authorization token.
    """

    def __init__(self, host: str, username: str, password: str):
        """Initialize the AuthEndpoint.

        Args:
            host: Base URL of the booking service.
            username: Username used for authentication.
            password: Password used for authentication.
        """
        super().__init__()

        self.host = host
        self.username = username
        self.password = password

    def get_token(self) -> str:
        """Authenticate and retrieve an authorization token.

        Sends a POST request to the authentication endpoint with the
        configured credentials and returns the token from the response.

        Returns:
            str: Authentication token returned by the booking service.
        """
        headers = {"Content-Type": "application/json"}
        body = {"username": self.username, "password": self.password}
        response = self.post(f"{self.host}/auth", json=body, headers=headers)
        return response.json()["token"]
