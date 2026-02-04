import json
import logging.config
from requests import Response, Session


class AbstractionEndpoint:
    def __init__(self, session: Session = None):
        self.session = session
        self.logger = logging.getLogger(self.__class__.__name__)

    def post(self, *args, **kwargs) -> Response:
        return self.request('POST', *args, **kwargs)

    def get(self, url, *args, **kwargs) -> Response:
        return self.request('GET', url, *args, **kwargs)

    def put(self, url, *args, **kwargs) -> Response:
        return self.request('PUT', url, *args, **kwargs)

    def patch(self, url, *args, **kwargs) -> Response:
        return self.request('PATCH', url, *args, **kwargs)

    def delete(self, url, *args, **kwargs) -> Response:
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




