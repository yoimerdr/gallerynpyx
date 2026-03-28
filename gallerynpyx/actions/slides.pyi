from typing import Any

from .base import HandlerInteractive
from ..handler.base.base import BaseHandler
from ..slides.base import SlideBase


class NextPage(HandlerInteractive):
    """
    Changes the page in the active ``slide``.
    """

    def __init__(self: Any, handler: str | BaseHandler | None = None) -> None:
        """
        :param handler: Optional handler instance or gallery name.
        """
        ...

    @classmethod
    def register(cls, target: type[NextPage]) -> None:
        """
        Registers the subclass that should be instantiated for this action.

        :param target: Class that inherits from ``NextPage`` and should replace it when instantiated.
        """
        ...

    def get_sensitive(self: Any) -> bool:
        """
        Method used internally by renpy
        """
        ...

    def __call__(self: Any, *args, **kwargs) -> None:
        """
        :param args: Positional arguments forwarded by Ren'Py.
        :param kwargs: Keyword arguments forwarded by Ren'Py.
        """
        ...

    def predict(self: Any) -> None:
        """
        Predicts the displayables that would be shown on the next page.
        """
        ...


class PreviousPage(HandlerInteractive):
    """
    Changes the page in the active ``slide``.
    """

    def __init__(self: Any, handler: str | BaseHandler | None = None) -> None:
        """
        :param handler: Optional handler instance or gallery name.
        """
        ...

    @classmethod
    def register(cls, target: type[PreviousPage]) -> None:
        """
        Registers the subclass that should be instantiated for this action.

        :param target: Class that inherits from ``PreviousPage`` and should replace it when instantiated.
        """
        ...

    def get_sensitive(self: Any) -> bool:
        """
        Method used internally by renpy
        """
        ...

    def __call__(self: Any, *args, **kwargs) -> None:
        """
        :param args: Positional arguments forwarded by Ren'Py.
        :param kwargs: Keyword arguments forwarded by Ren'Py.
        """
        ...

    def predict(self: Any) -> None:
        """
        Predicts the displayables that would be shown on the previous page.
        """
        ...


class ChangeSlide(HandlerInteractive):
    """
    Changes the active ``slide``
    """

    def __init__(self: Any,
                 slide: SlideBase,
                 handler: str | BaseHandler | None = None) -> None:
        """
        :param slide: Target slide or slider.
        :param handler: Optional handler instance or gallery name.
        """
        ...

    @classmethod
    def register(cls, target: type[ChangeSlide]) -> None:
        """
        Registers the subclass that should be instantiated for this action.

        :param target: Class that inherits from ``ChangeSlide`` and should replace it when instantiated.
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

    def __call__(self: Any, *args, **kwargs) -> None:
        """
        :param args: Positional arguments forwarded by Ren'Py.
        :param kwargs: Keyword arguments forwarded by Ren'Py.
        """
        ...

    def predict(self: Any) -> None:
        """
        Predicts the displayables that would be shown after changing slide.
        """
        ...


class ReturnSlide(HandlerInteractive):
    """
    Returns from inner slides or from the root slider.
    """

    def __init__(self: Any,
                 has_animations: bool = False,
                 handler: str | BaseHandler | None = None) -> None:
        """
        :param has_animations: Whether the active ``slide`` has any animations.
        :param handler: Optional handler instance or gallery name.
        """
        ...

    @classmethod
    def register(cls, target: type[ReturnSlide]) -> None:
        """
        Registers the subclass that should be instantiated for this action.

        :param target: Class that inherits from ``ReturnSlide`` and should replace it when instantiated.
        """
        ...

    def __call__(self: Any, *args, **kwargs) -> Any:
        """
        :param args: Positional arguments forwarded by Ren'Py.
        :param kwargs: Keyword arguments forwarded by Ren'Py.
        """
        ...
