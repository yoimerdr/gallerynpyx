from typing import Any

from .base import HandlerInteractive
from ..common.classes.objects import Registry, Singleton
from ..slides.slide import Slide


class NextPage(HandlerInteractive):
    """
    Changes the page in the active ``slide``.
    """

    def __init__(self: Any):
        ...

    @classmethod
    def get_instance(cls, *args, **kwargs) -> NextPage:
        """
        Creates or returns the singleton instance.

        :param args: Init class arguments.
        :param kwargs: Init class keyword arguments.
        """
        ...

    def get_sensitive(self: Any) -> bool:
        """
        Method used internally by renpy
        """
        ...

    def __call__(self: Any, *args, **kwargs):
        ...


class PreviousPage(HandlerInteractive):
    """
    Changes the page in the active ``slide``.
    """

    def __init__(self: Any):
        ...

    @classmethod
    def get_instance(cls, *args, **kwargs) -> PreviousPage:
        """
        Creates or returns the singleton instance.

        :param args: Init class arguments.
        :param kwargs: Init class keyword arguments.
        """
        ...

    def get_sensitive(self: Any) -> bool:
        """
        Method used internally by renpy
        """
        ...

    def __call__(self: Any, *args, **kwargs):
        ...


class ChangeSlide(HandlerInteractive):
    """
    Changes the active ``slide``
    """

    def __init__(self: Any, slide: Slide):
        ...

    @classmethod
    def register(cls, target: type[ChangeSlide]):
        """
        Registers a target class in the registry.

        :param target: The class to register.
        """
        ...

    def get_selected(self: Any) -> bool:
        """
        Method used internally by renpy
        """
        ...

    def get_sensitive(self: Any) -> bool:
        """
        Method used internally by renpy
        """
        ...

    def __call__(self: Any, *args, **kwargs):
        ...


class ReturnSlide(HandlerInteractive):
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
