from typing import Callable

from .base import BaseHandler


class HandlerManager(object):
    """
    Resolves the global handler or named local handlers.

    :notes:
        * Only named local handlers are cached by this manager.
        * The unnamed global handler is obtained by calling ``global_builder()`` on each access.
        * In the default implementation this still behaves like a shared handler because
          ``gallerynpyx.handler.Handler`` inherits from a cached singleton type.
        * If you provide another handler class that does not inherit from the built-in cached bases
          (for example ``Singleton``), the global cache must be handled externally.
    """

    def __init__(self,
                 global_builder: Callable[[], BaseHandler],
                 local_builder: Callable[[str], BaseHandler]) -> None:
        """
        :param global_builder: Builder used for the unnamed global handler.
            Its result is not cached by this manager.
        :param local_builder: Builder used for each named local handler.
        """
        ...

    def get(self, name: str | None = None, override: bool = False) -> BaseHandler:
        """
        Returns the global handler or a named local handler.

        :notes:
            * When ``name`` is empty, the manager calls ``global_builder()`` directly.
            * Only named local handlers participate in the manager cache.
            * If the global builder does not return a cached type, the caller must keep that cache.

        :param name: Optional gallery name.
        :param override: Recreates the named handler when ``True``.
        """
        ...

    def flush(self, name: str | None = None) -> None:
        """
        Clears one cached handler or every named handler.

        :param name: Optional gallery name to flush.
        """
        ...
