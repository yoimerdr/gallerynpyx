from ...config.base.resources import ResourcesConfig
from ...config.base.screens import ScreensConfig
from ...config.base.styles import StylesConfig
from .base import BaseHandler

__all__ = ("Handler",)


class Handler(BaseHandler):
    """
    Gallery handler bound to a specific set of local or shared configurations.
    """

    def __init__(self,
                 resources_config: str | ResourcesConfig | None = None,
                 styles_config: str | StylesConfig | None = None,
                 screens_config: str | ScreensConfig | None = None) -> None:
        """
        :param resources_config: Resource configuration instance or gallery name.
        :param styles_config: Style configuration instance or gallery name.
        :param screens_config: Screen configuration instance or gallery name.
        """
        ...

    @property
    def resources_config(self) -> ResourcesConfig:
        """
        Resource configuration currently used by the handler.
        """
        ...

    @resources_config.setter
    def resources_config(self, value: str | ResourcesConfig | None) -> None:
        """
        :param value: Resources configuration instance or gallery name.
        """
        ...

    @property
    def styles_config(self) -> StylesConfig:
        """
        Style configuration currently used by the handler.
        """
        ...

    @styles_config.setter
    def styles_config(self, value: str | StylesConfig | None) -> None:
        """
        :param value: Styles configuration instance or gallery name.
        """
        ...

    @property
    def screens_config(self) -> ScreensConfig:
        """
        Screen configuration currently used by the handler.
        """
        ...

    @screens_config.setter
    def screens_config(self, value: str | ScreensConfig | None) -> None:
        """
        :param value: Screens configuration instance or gallery name.
        """
        ...
