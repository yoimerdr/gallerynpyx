from .base.base import BaseHandler
from .base.manager import HandlerManager

__all__ = ("coerce",)


def coerce(name: str | BaseHandler | None = None,
           manager: HandlerManager | None = None,
           cls: type[BaseHandler] = BaseHandler) -> BaseHandler:
    """
    Returns a handler from a name or an existing handler instance.

    :param name: Handler instance or gallery name.
    :param manager: Manager used to resolve named handlers.
    :param cls: Expected handler base type.
    """
    ...
