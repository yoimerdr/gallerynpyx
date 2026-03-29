from .base.manager import ConfigManager
from .base.screens import ScreensConfig as BaseScreensConfig

__all__ = (
    "ScreensConfig",
    "get_screens",
)


class ScreensConfig(BaseScreensConfig):
    """
    Shared screens configuration used by the unnamed gallery.
    """
    ...


manager: ConfigManager
"""Manager used to retrieve shared or named screens configurations."""


def get_screens(name: str | None = None, override: bool = False) -> BaseScreensConfig:
    """
    Returns the shared screens configuration or a named local one.

    :param name: Optional gallery name.
    :param override: Recreates the named local configuration when ``True``.
    """
    ...
