from .base import BaseConfig, ResourcesConfig, ScreensConfig, StylesConfig
from . import resources, screens, styles

__all__ = (
    "coerce",
    "coerce_resources",
    "coerce_screens",
    "coerce_styles",
)


def coerce(manager, name=None, cls=BaseConfig):
    if isinstance(name, cls):
        return name

    return manager.get(name)


def coerce_resources(name=None):
    return coerce(
        manager=resources.manager,
        name=name,
        cls=ResourcesConfig
    )


def coerce_screens(name=None):
    return coerce(
        manager=screens.manager,
        name=name,
        cls=ScreensConfig
    )


def coerce_styles(name=None):
    return coerce(
        manager=styles.manager,
        name=name,
        cls=StylesConfig
    )
