class SingletonMeta(type):
    """A metaclass to ensure that only one instance of class is created."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call the class and ensure that only one instance is created.

        :param args: The arguments.
        :param kwargs: The keyword arguments.
        :return: The instance of the class.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
