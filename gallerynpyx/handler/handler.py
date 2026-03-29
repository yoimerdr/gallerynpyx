from .base.base import BaseHandler
from .base.handler import Handler as LocalHandler
from .base.manager import HandlerManager

from ..common.classes import add_metaclass, SingletonRegistryMeta
from ..config import resources as resources_config, styles as styles_config, screens as screens_config

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
        return resources_config.manager.get()

    @property
    def styles_config(self):
        return styles_config.manager.get()

    @property
    def screens_config(self):
        return screens_config.manager.get()


def _create_local_handler(name):
    return LocalHandler(
        resources_config=name,
        styles_config=name,
        screens_config=name
    )


manager = HandlerManager(Handler, _create_local_handler)

get_handler = manager.get
