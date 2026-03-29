from .base.base import BaseConfig
from .base.manager import ConfigManager
from .base.resources import ResourcesConfig as BaseResourcesConfig
from .base.screens import ScreensConfig as BaseScreensConfig
from .base.styles import StylesConfig as BaseStylesConfig

__all__ = (
    "coerce",
    "coerce_resources",
    "coerce_screens",
    "coerce_styles",
)


def coerce(manager: ConfigManager,
           name: str | BaseConfig | None = None,
           cls: type[BaseConfig] = BaseConfig) -> BaseConfig:
    """
    Returns a configuration object, accepting either a name or an existing instance.

    :param manager: Manager used to resolve named configurations.
    :param name: Configuration instance or gallery name.
    :param cls: Expected configuration base type.
    """
    ...


def coerce_resources(name: str | BaseResourcesConfig | None = None) -> BaseResourcesConfig:
    """
    Returns a resources configuration from a name or an existing instance.

    :param name: Resources configuration instance or gallery name.
    """
    ...


def coerce_screens(name: str | BaseScreensConfig | None = None) -> BaseScreensConfig:
    """
    Returns a screens configuration from a name or an existing instance.

    :param name: Screens configuration instance or gallery name.
    """
    ...


def coerce_styles(name: str | BaseStylesConfig | None = None) -> BaseStylesConfig:
    """
    Returns a styles configuration from a name or an existing instance.

    :param name: Styles configuration instance or gallery name.
    """
    ...
