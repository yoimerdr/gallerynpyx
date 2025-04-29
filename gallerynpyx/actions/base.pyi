from typing import Any

from ..handler import Handler
from renpy.ui import Action


class Interactive(Action):
    """
    An action that can restart the interaction.
    """

    def __call__(self: Any, *args, **kwargs):
        ...


class HandlerInteractive(Interactive):
    """
    An action that can restart the interaction and interact with the ``Handler``.
    """

    @property
    def handler(self: Any) -> Handler:
        ...
