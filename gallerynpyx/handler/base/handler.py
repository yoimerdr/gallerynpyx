from .base import BaseHandler
from ...config import coerce_screens, coerce_styles, coerce_resources

__all__ = ('Handler',)


class Handler(BaseHandler):
    __slots__ = (
        '_rs_cfg',
        '_sty_cfg',
        '_res_cfg',
    )

    def __init__(self, resources_config=None, styles_config=None, screens_config=None):
        self.resources_config = resources_config
        self.styles_config = styles_config
        self.screens_config = screens_config
        super(Handler, self).__init__()

    @property
    def resources_config(self):
        return self._rs_cfg

    @resources_config.setter
    def resources_config(self, value):
        self._rs_cfg = coerce_resources(value)

    @property
    def styles_config(self):
        return self._sty_cfg

    @styles_config.setter
    def styles_config(self, value):
        self._sty_cfg = coerce_styles(value)

    @property
    def screens_config(self):
        return self._res_cfg

    @screens_config.setter
    def screens_config(self, value):
        self._res_cfg = coerce_screens(value)
