from .base import BaseHandler
from ...config.base import ResourcesConfig, ScreensConfig, StylesConfig
from ...config import coerce as coerce_config, resources as resources_cfg
from ...config import screens as screens_cfg, styles as styles_cfg

__all__ = ('Handler',)


def _create_config(value, module, coerce_cls, ):
    if value is not None:
        module.manager.flush(value)

    return coerce_config(
        manager=module.manager,
        name=value,
        cls=coerce_cls
    )


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
        self._rs_cfg = _create_config(
            value=value,
            module=resources_cfg,
            coerce_cls=ResourcesConfig
        )

    @property
    def styles_config(self):
        return self._sty_cfg

    @styles_config.setter
    def styles_config(self, value):
        self._sty_cfg = _create_config(
            value=value,
            module=styles_cfg,
            coerce_cls=StylesConfig
        )

    @property
    def screens_config(self):
        return self._res_cfg

    @screens_config.setter
    def screens_config(self, value):
        self._res_cfg = _create_config(
            value=value,
            module=screens_cfg,
            coerce_cls=ScreensConfig
        )
