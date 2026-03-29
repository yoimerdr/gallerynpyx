from typing import Iterable, Union

from renpy.display.behavior import Button
from .sizes.size import Size
from .config.base.resources import ResourcesConfig
from .config.base.screens import ScreensConfig
from .slides.items import Item


def isvideo(source) -> bool:
    """
    Checks if value is an instance of ``VideoResource``

    :param source: The value to check
    """
    ...


def isimage(source) -> bool:
    """
    Checks if value is an instance of ``ImageResource``

    :param source: The value to check
    """
    ...


def isdisplayable(source) -> bool:
    """
    Checks if value is an instance of ``DisplayableResource``

    :param source: The value to check
    """
    ...


def isanimation(source) -> bool:
    """
    Checks if value is an instance of ``AnimationResource``

    :param source: The value to check
    """
    ...


def create_buttons(items: Iterable[Item],
                   size: Union[Iterable, Size],
                   resources_config: str | ResourcesConfig | None = None,
                   screens_config: str | ScreensConfig | None = None) -> Iterable[Button]:
    """
    Creates an iterable with ``Buttons`` for the given items.

    :notes:
        * The resource and screen configuration can come from the shared gallery or from a named local gallery.
        * The action of each button is ``ShowItem``.
    :param items: Iterable of items.
    :param size: Iterable with height and width dimension for thumbnails.
    :param resources_config: Optional resources configuration or gallery name.
    :param screens_config: Optional screens configuration or gallery name.
    """
    ...
