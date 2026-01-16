"""Singleton metaclass implementation.

This module provides a metaclass that enforces the singleton pattern,
ensuring that only one instance of a class exists during the application
lifecycle.
"""


class SingletonMeta(type):
    """Metaclass implementing the singleton pattern.

    Classes using this metaclass will only ever have one instance.
    Subsequent instantiations will return the same instance.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Create or return a singleton instance of the class.

        If an instance of the class does not already exist, it is created
        and stored. Subsequent calls return the existing instance.

        Args:
            *args: Positional arguments passed to the class constructor.
            **kwargs: Keyword arguments passed to the class constructor.

        Returns:
            object: The singleton instance of the class.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
