from .base.screens import ScreensConfig as BaseScreensConfig
from .base.manager import ConfigManager
from ..common.classes import add_metaclass, SingletonRegistryMeta

__all__ = (
    'ScreensConfig',
    'get_screens',
)


@add_metaclass(SingletonRegistryMeta)
class ScreensConfig(BaseScreensConfig):
    __slots__ = ()


manager = ConfigManager(ScreensConfig, BaseScreensConfig)


get_screens = manager.get