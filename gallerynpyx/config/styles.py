from .base import StylesConfig as BaseStylesConfig, ConfigManager
from ..common.classes import add_metaclass, SingletonRegistryMeta

__all__ = (
    'StylesConfig',
    'get_styles',
)


@add_metaclass(SingletonRegistryMeta)
class StylesConfig(BaseStylesConfig):
    __slots__ = ()


manager = ConfigManager(StylesConfig, BaseStylesConfig)

get_styles = manager.get
