from typing import Any


class UnsupportedSourceError(ValueError):
    """
    Inappropriate source value (of correct type).
    """
    def __init__(self: Any, source, target=None):
        """
        :param source: The source value.
        :param target: The target class or instance.
        """
        ...


class IncompatibleResourceError(ValueError):
    """
    Inappropriate resource value (of correct type).
    """
    def __init__(self: Any, resource, target=None):
        """
        :param resource: The resource value.
        :param target: The target resource class or instance.
        """
        ...


class UnloadableSourceError(ValueError):
    """
    Source is not loadable.
    """
    def __init__(self: Any, source):
        """
        :param source: The not loadable source.
        """
        ...
