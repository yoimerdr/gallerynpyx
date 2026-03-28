from .base import BaseConfig

__all__ = (
    "coerce",
)

def coerce(manager, name=None, cls=BaseConfig):
    if isinstance(name, cls):
        return name

    return manager.get(name)
