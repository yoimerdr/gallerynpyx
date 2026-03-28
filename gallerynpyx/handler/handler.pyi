from ..config.resources import ResourcesConfig
from ..config.screens import ScreensConfig
from ..config.styles import StylesConfig
from .base.base import BaseHandler
from .base.manager import HandlerManager

__all__ = (
    "Handler",
    "get_handler",
)


class Handler(BaseHandler):
    """
    Shared gallery handler used when no gallery name is provided.
    """

    def __init__(self) -> None:
        """
        Creates the shared gallery handler.
        """
        ...

    @property
    def resources_config(self) -> ResourcesConfig:
        """
        Shared resources configuration bound to the default gallery.
        """
        ...

    @property
    def styles_config(self) -> StylesConfig:
        """
        Shared styles configuration bound to the default gallery.
        """
        ...

    @property
    def screens_config(self) -> ScreensConfig:
        """
        Shared screens configuration bound to the default gallery.
        """
        ...


manager: HandlerManager
"""Manager used to retrieve the shared handler or named local handlers."""


def get_handler(name: str | None = None, override: bool = False) -> BaseHandler:
    """
    Returns the shared gallery handler or a named local handler.

    :param name: Optional gallery name.
    :param override: Recreates the named local handler when ``True``.
    """
    ...
