from typing import Any, AnyStr
from .base import SlideBase


class NameAlreadyExistsError(ValueError):
    """
    A name already exists in the slider.
    """
    def __init__(self: Any, name: AnyStr, slider: SlideBase = None):
        """
        :param name: The name string.
        :param slider: The object where the name exists.
        """
        ...


class InvalidRouteError(ValueError):
    """
    A route is invalid (type or value)
    """
    def __init__(self: Any, reason: AnyStr):
        """
        :param reason: The reason why the route is invalid.
        """
        ...
