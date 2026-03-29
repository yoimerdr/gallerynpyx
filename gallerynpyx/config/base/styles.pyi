from typing import AnyStr

from .base import BaseConfig

__all__ = ("StylesConfig",)


class StylesConfig(BaseConfig):
    """
    Style configuration shared by the global gallery and named local galleries.
    """

    def __init__(self) -> None:
        """
        Creates the default style configuration for a gallery.
        """
        ...

    @property
    def root(self) -> str:
        """
        Base style used by the root gallery screen.
        """
        ...

    @root.setter
    def root(self, value: AnyStr | None) -> None:
        """
        :param value: New base style for the root gallery screen.
        """
        ...

    @property
    def tooltip(self) -> str:
        """
        Style used by the tooltip screen.
        """
        ...

    @tooltip.setter
    def tooltip(self, value: AnyStr | None) -> None:
        """
        :param value: New tooltip style name.
        """
        ...

    @property
    def navigation(self) -> str:
        """
        Style used by the navigation frame.
        """
        ...

    @navigation.setter
    def navigation(self, value: AnyStr | None) -> None:
        """
        :param value: New navigation frame style name.
        """
        ...

    @property
    def scrollbar(self) -> str:
        """
        Style used by the gallery scrollbar.
        """
        ...

    @scrollbar.setter
    def scrollbar(self, value: AnyStr | None) -> None:
        """
        :param value: New scrollbar style name.
        """
        ...

    @property
    def items(self) -> str:
        """
        Style used by the thumbnail grid.
        """
        ...

    @items.setter
    def items(self, value: AnyStr | None) -> None:
        """
        :param value: New thumbnail grid style name.
        """
        ...

    @property
    def slide_controls(self) -> str:
        """
        Style used by the slide controls viewport.
        """
        ...

    @slide_controls.setter
    def slide_controls(self, value: AnyStr | None) -> None:
        """
        :param value: New slide controls viewport style name.
        """
        ...

    @property
    def animation_controls(self) -> str:
        """
        Style used by the animation controls container.
        """
        ...

    @animation_controls.setter
    def animation_controls(self, value: AnyStr | None) -> None:
        """
        :param value: New animation controls style name.
        """
        ...

    @property
    def controls(self) -> str:
        """
        Style used by the general controls container.
        """
        ...

    @controls.setter
    def controls(self, value: AnyStr | None) -> None:
        """
        :param value: New general controls container style name.
        """
        ...
