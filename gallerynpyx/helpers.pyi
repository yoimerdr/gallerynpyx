from typing import Iterable, Union

from renpy.display.behavior import Button
from .sizes.size import Size
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


def create_buttons(items: Iterable[Item], size: Union[Iterable, Size]) -> Iterable[Button]:
    """
    Creates an iterable with ``Buttons`` for the given items.

    :notes: Here we use the resources assigned in ``ResourcesConfig`` for the different button's and item's states (e.g., idle, hover, locked).
    :notes: The action of each button is ``ShowItem``.
    :param items: Iterable of items.
    :param size: Iterable with height and width dimension for thumbnails.
    """
    ...
