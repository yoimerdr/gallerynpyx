from typing import Any

from renpy.ui import Action
from ..handler.base.base import BaseHandler


class Interactive(Action):
    """
    An action that can restart the interaction.
    """

    def __call__(self: Any, *args, **kwargs) -> None:
        """
        :param args: Positional arguments forwarded by Ren'Py.
        :param kwargs: Keyword arguments forwarded by Ren'Py.
        """
        ...


class HandlerInteractive(Interactive):
    """
    An action that can restart the interaction and resolve any gallery handler.
    """

    def __init__(self: Any, handler: str | BaseHandler | None = None) -> None:
        """
        :param handler: Optional handler instance or gallery name to resolve.
        """
        ...

    @property
    def handler(self: Any) -> BaseHandler:
        """
        Handler resolved for the current action.
        """
        ...
