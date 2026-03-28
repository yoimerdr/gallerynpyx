from .base import ResourcesConfig as BaseResourcesConfig, ConfigManager
from ..common.classes import add_metaclass, SingletonRegistryMeta

__all__ = (
    'ResourcesConfig',
    'get_resources',
)


@add_metaclass(SingletonRegistryMeta)
class ResourcesConfig(BaseResourcesConfig):
    pass


manager = ConfigManager(ResourcesConfig, BaseResourcesConfig)

get_resources = manager.get
