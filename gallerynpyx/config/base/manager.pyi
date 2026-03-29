from typing import Callable

from .base import BaseConfig


class ConfigManager(object):
    """
    Resolves the global or named local gallery configurations.

    :notes:
        * Only named local configurations are cached by this manager.
        * The unnamed global configuration is obtained by calling ``global_builder()`` on each access.
        * In the default implementation this still behaves like a shared object because
          ``ResourcesConfig``, ``ScreensConfig`` and ``StylesConfig`` inherit from cached registry types.
        * If you provide another class that does not inherit from the built-in cached bases
          (for example ``SingletonRegistry``), the global cache must be handled externally.
    """

    def __init__(self,
                 global_builder: Callable[[], BaseConfig],
                 local_builder: Callable[[], BaseConfig]) -> None:
        """
        :param global_builder: Builder used for the unnamed global configuration.
            Its result is not cached by this manager.
        :param local_builder: Builder used for each named local configuration.
        """
        ...

    def get(self, name: str | None = None, override: bool = False) -> BaseConfig:
        """
        Returns the global configuration or a named local one.

        :notes:
            * When ``name`` is empty, the manager calls ``global_builder()`` directly.
            * Only named local configurations participate in the manager cache.
            * If the global builder does not return a cached type, the caller must keep that cache.

        :param name: Optional gallery name.
        :param override: Recreates the named configuration when ``True``.
        """
        ...

    def flush(self, name: str | None = None) -> None:
        """
        Clears one cached configuration or every local configuration.

        :param name: Optional gallery name to flush.
        """
        ...
