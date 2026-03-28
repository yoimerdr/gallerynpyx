from .base import HandlerManager, BaseHandler, Handler as LocalHandler
from ..common.classes import add_metaclass, SingletonRegistryMeta
from ..config import ResourcesConfig, StylesConfig, ScreensConfig

__all__ = (
    "Handler",
    "get_handler"
)


@add_metaclass(SingletonRegistryMeta)
class Handler(BaseHandler):
    __slots__ = ()

    def __init__(self):
        super(Handler, self).__init__()

    @property
    def resources_config(self):
        return ResourcesConfig.get_instance()

    @property
    def styles_config(self):
        return StylesConfig.get_instance()

    @property
    def screens_config(self):
        return ScreensConfig.get_instance()


def _create_local_handler(name):
    return LocalHandler(
        resources_config=name,
        styles_config=name,
        screens_config=name
    )


manager = HandlerManager(Handler, _create_local_handler)

get_handler = manager.get
