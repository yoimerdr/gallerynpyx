from .base.resources import ResourcesConfig as BaseResourcesConfig
from .base.manager import ConfigManager
from ..common.classes import add_metaclass, SingletonRegistryMeta

__all__ = (
    'ResourcesConfig',
    'get_resources',
)


@add_metaclass(SingletonRegistryMeta)
class ResourcesConfig(BaseResourcesConfig):
    __slots__ = ()

manager = ConfigManager(ResourcesConfig, BaseResourcesConfig)

get_resources = manager.get
