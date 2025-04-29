from typing import Any

from .base import HandlerInteractive
from ..common.classes.objects import Registry, Singleton
from ..slides.slide import Slide


class NextPage(HandlerInteractive, Singleton):
    """
    Changes the page in the active ``slide``.
    """

    def __init__(self: Any):
        ...

    def get_sensitive(self: Any):
        ...

    def __call__(self: Any, *args, **kwargs):
        ...


class PreviousPage(HandlerInteractive, Singleton):
    """
    Changes the page in the active ``slide``.
    """

    def __init__(self: Any):
        ...

    def get_sensitive(self: Any):
        """
        Method used internally by renpy
        """
        ...

    def __call__(self: Any, *args, **kwargs):
        ...


class ChangeSlide(HandlerInteractive, Registry):
    """
    Changes the active ``slide``
    """

    def __init__(self: Any, slide: Slide):
        ...

    def get_selected(self: Any):
        """
        Method used internally by renpy
        """
        ...

    def get_sensitive(self: Any):
        """
        Method used internally by renpy
        """
        ...

    def __call__(self: Any, *args, **kwargs):
        ...


class ReturnSlide(HandlerInteractive, Registry):
    """
    Returns from inner slides or from the root slider.
    """

    def __init__(self: Any, has_animations: bool = False):
        """
        :param has_animations: Whether the active ``slide`` has any animations.
        """
        ...

    def __call__(self: Any, *args, **kwargs):
        ...
