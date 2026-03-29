from typing import Any, AnyStr, Union

from renpy.display.displayable import Displayable
from renpy.display.im import Image
from renpy.display.transform import ATLTransform
from renpy.display.video import Movie

from ...resources.resource import Resource
from ...resources.thumbnail import Thumbnail
from .base import BaseConfig

__all__ = ("ScreensConfig",)


class ScreensConfig(BaseConfig):
    """
    Screen configuration shared by the global gallery and named local galleries.
    """

    def __init__(self) -> None:
        """
        Creates the default screen configuration for a gallery.
        """
        ...

    @property
    def images_screen(self) -> str:
        """
        Screen name used to display a selected resource.
        """
        ...

    @images_screen.setter
    def images_screen(self, value: AnyStr | None) -> None:
        """
        :param value: New screen name for displayed resources.
        """
        ...

    @property
    def root_screen(self) -> str:
        """
        Root screen name for the gallery shell.
        """
        ...

    @root_screen.setter
    def root_screen(self, value: AnyStr | None) -> None:
        """
        :param value: New root screen name.
        """
        ...

    @property
    def navigation_screen(self) -> str:
        """
        Screen name used to render slide navigation.
        """
        ...

    @navigation_screen.setter
    def navigation_screen(self, value: AnyStr | None) -> None:
        """
        :param value: New navigation screen name.
        """
        ...

    @property
    def items_screen(self) -> str:
        """
        Screen name used to render thumbnail items.
        """
        ...

    @items_screen.setter
    def items_screen(self, value: AnyStr | None) -> None:
        """
        :param value: New items screen name.
        """
        ...

    @property
    def animation_controls_screen(self) -> str:
        """
        Screen name used to render animation controls.
        """
        ...

    @animation_controls_screen.setter
    def animation_controls_screen(self, value: AnyStr | None) -> None:
        """
        :param value: New animation controls screen name.
        """
        ...

    @property
    def controls_screen(self) -> str:
        """
        Screen name used to render item controls.
        """
        ...

    @controls_screen.setter
    def controls_screen(self, value: AnyStr | None) -> None:
        """
        :param value: New controls screen name.
        """
        ...

    @property
    def slide_controls_screen(self) -> str:
        """
        Screen name used to render page and slide controls.
        """
        ...

    @slide_controls_screen.setter
    def slide_controls_screen(self, value: AnyStr | None) -> None:
        """
        :param value: New page and slide controls screen name.
        """
        ...

    @property
    def tooltip_screen(self) -> str:
        """
        Screen name used for gallery tooltips.
        """
        ...

    @tooltip_screen.setter
    def tooltip_screen(self, value: AnyStr | None) -> None:
        """
        :param value: New tooltip screen name.
        """
        ...

    @property
    def foreground(self) -> Thumbnail:
        """
        Foreground thumbnail shown by the root gallery screen.
        """
        ...

    @foreground.setter
    def foreground(self,
                   value: Union[Resource, AnyStr, Displayable, Movie, ATLTransform, Image]) -> None:
        """
        :param value: New foreground resource source.
        """
        ...

    @property
    def background(self) -> Thumbnail:
        """
        Background thumbnail shown by the root gallery screen.
        """
        ...

    @background.setter
    def background(self,
                   value: Union[Resource, AnyStr, Displayable, Movie, ATLTransform, Image]) -> None:
        """
        :param value: New background resource source.
        """
        ...

    @property
    def show_scrollbar(self) -> bool:
        """
        Whether the default slide controls screen shows its scrollbar.
        """
        ...

    @show_scrollbar.setter
    def show_scrollbar(self, value: Any) -> None:
        """
        :param value: Truthy value to show the default scrollbar.
        """
        ...
