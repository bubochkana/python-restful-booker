"""Action layer for building and managing API request payloads.

This package contains action classes responsible for constructing
request bodies and test data used by API endpoints. Each module
encapsulates logic for a specific API domain, such as Booking or
JsonPlaceholder resources, and provides reusable helpers for creating
valid and randomized payloads to be used in end-to-end tests.

The action layer helps keep test logic clean by separating data
preparation from endpoint interaction and assertions.
"""