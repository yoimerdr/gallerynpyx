from .base.manager import ConfigManager
from .base.resources import ResourcesConfig as BaseResourcesConfig

__all__ = (
    "ResourcesConfig",
    "get_resources",
)


class ResourcesConfig(BaseResourcesConfig):
    """
    Shared resources configuration used by the unnamed gallery.
    """
    ...


manager: ConfigManager
"""Manager used to retrieve shared or named resources configurations."""


def get_resources(name: str | None = None, override: bool = False) -> BaseResourcesConfig:
    """
    Returns the shared resources configuration or a named local one.

    :param name: Optional gallery name.
    :param override: Recreates the named local configuration when ``True``.
    """
    ...
