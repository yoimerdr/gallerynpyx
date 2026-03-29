from .base.manager import ConfigManager
from .base.styles import StylesConfig as BaseStylesConfig

__all__ = (
    "StylesConfig",
    "get_styles",
)


class StylesConfig(BaseStylesConfig):
    """
    Shared styles configuration used by the unnamed gallery.
    """
    ...


manager: ConfigManager
"""Manager used to retrieve shared or named styles configurations."""


def get_styles(name: str | None = None, override: bool = False) -> BaseStylesConfig:
    """
    Returns the shared styles configuration or a named local one.

    :param name: Optional gallery name.
    :param override: Recreates the named local configuration when ``True``.
    """
    ...
