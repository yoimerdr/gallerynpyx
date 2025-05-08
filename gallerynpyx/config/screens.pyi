from typing import Any, AnyStr, Union

from renpy.display.displayable import Displayable
from renpy.display.im import Image
from renpy.display.transform import ATLTransform
from renpy.display.video import Movie
from ..common.classes.objects import SingletonRegistry, _T
from ..resources.resource import Resource
from ..resources.thumbnail import Thumbnail


class ScreensConfig(SingletonRegistry):
    """
    Common configuration for screens-related properties.

    :notes:
        * There will be only one instance
        * You can register a custom configuration by using the ``register`` class method before the first use of the class.
    """

    def __init__(self: Any):
        ...

    @classmethod
    def register(cls: Any, target: type[ScreensConfig]):
        """
        Registers a target class in the registry.

        :param target: The class to register.
        """
        ...

    @classmethod
    def get_instance(cls: Any, *args, **kwargs) -> ScreensConfig:
        """
        Creates or returns the singleton instance.

        :param args: Init class arguments.
        :param kwargs: Init class keyword arguments.
        """
        ...

    @property
    def images_screen(self: Any) -> str:
        """
        The screen name where the images are displayed.

        :getter: Gets the screen name.
        :setter: Sets a new screen name.
        """
        ...

    @images_screen.setter
    def images_screen(self: Any, value: AnyStr):
        ...

    @property
    def root_screen(self: Any) -> str:
        """
        The screen name for the root screen.

        :getter: Gets the screen name.
        :setter: Sets a new screen name.
        """
        ...

    @root_screen.setter
    def root_screen(self: Any, value: AnyStr):
        ...

    @property
    def navigation_screen(self: Any) -> str:
        """
        The screen name for the navigation.

        :getter: Gets the screen name.
        :setter: Sets a new screen name.
        """
        ...

    @navigation_screen.setter
    def navigation_screen(self: Any, value: AnyStr):
        ...

    @property
    def items_screen(self: Any) -> str:
        """
        The screen name for the items (thumbnails).

        :getter: Gets the screen name.
        :setter: Sets a new screen name.
        """
        ...

    @items_screen.setter
    def items_screen(self: Any, value: AnyStr):
        ...

    @property
    def animation_controls_screen(self: Any) -> str:
        """
        The screen name for the speed controls.

        :notes:
            * This is a special screen, it is used to display the speed controls if it's allowed.
            * It is used only when there is any animation in the active slide.
        :getter: Gets the screen name.
        :setter: Sets a new screen name.
        """
        ...

    @animation_controls_screen.setter
    def animation_controls_screen(self: Any, value: AnyStr):
        ...

    @property
    def controls_screen(self: Any) -> str:
        """
        The screen name for the action controls.

        :getter: Gets the screen name.
        :setter: Sets a new screen name.
        """
        ...

    @controls_screen.setter
    def controls_screen(self: Any, value: AnyStr):
        ...

    @property
    def slide_controls_screen(self: Any) -> str:
        """
        The screen name for the slide/slider (actions)

        :getter: Gets the screen name.
        :setter: Sets a new screen name.
        """
        ...

    @slide_controls_screen.setter
    def slide_controls_screen(self: Any, value: AnyStr):
        ...

    @property
    def tooltip_screen(self: Any) -> str:
        """
        The screen name for the tooltips.

        :getter: Gets the screen name.
        :setter: Sets a new screen name.
        """
        ...

    @tooltip_screen.setter
    def tooltip_screen(self: Any, value: AnyStr):
        ...

    @property
    def foreground(self: Any) -> Thumbnail:
        """
        Thumbnail for the foreground on the screen.

        :notes: This is added on the main screen, before using the ``root_screen`` and after the ``background``.
        :getter: Gets the thumbnail for foreground.
        :setter: Sets a new resource for the idle thumbnail.
        """
        ...

    @foreground.setter
    def foreground(self: Any, value: Union[Resource, AnyStr, Displayable, Movie, ATLTransform, Image]):
        ...

    @property
    def background(self: Any) -> Thumbnail:
        """
        Thumbnail for the background on the screen.

        :notes: This is added on the main screen, before using the ``root_screen``.
        :getter: Gets the thumbnail for foreground.
        :setter: Sets a new resource for the idle thumbnail.
        """
        ...

    @background.setter
    def background(self: Any, value: Union[Resource, AnyStr, Displayable, Movie, ATLTransform, Image]):
        ...

    @property
    def show_scrollbar(self: Any) -> bool:
        """
        Whether to show the scrollbar on the ``slide_controls_screen``.

        :notes: It is only used in the default ``slide_controls_screen``, unless this value is used in the new screen.
        :getter: Gets the scrollbar state.
        :setter: Sets a new scrollbar state.
        """
        ...

    @show_scrollbar.setter
    def show_scrollbar(self: Any, value):
        ...
