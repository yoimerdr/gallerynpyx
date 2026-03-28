from .base import BaseHandler
from . import handler

__all__ = (
    "coerce",
)


def coerce(manager=None, name=None, cls=BaseHandler):
    if isinstance(name, cls):
        return name

    if manager is None:
        manager = handler.manager

    return manager.get(name)
