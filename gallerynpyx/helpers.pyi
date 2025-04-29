from typing import Iterable, Union

from renpy.display.behavior import Button
from .sizes.size import Size
from .slides.items import Item


def create_buttons(items: Iterable[Item], size: Union[Iterable, Size]) -> Iterable[Button]:
    """
    Creates an iterable with ``Buttons`` for the given items.

    :notes: Here we use the resources assigned in ``ResourcesConfig`` for the different button's and item's states (e.g., idle, hover, locked).
    :notes: The action of each button is ``ShowItem``.
    :param items: Iterable of items.
    :param size: Iterable with height and width dimension for thumbnails.
    """
    ...
