from typing import Literal, Callable, override

from gallerynpyx.slides.items import Item
from gallerynpyx.slides.slide import Slide
from gallerynpyx.slides.slider import Slider


def on(event: Literal['gx-slide-change'],
       callback: Callable[[Literal['slide'], Slide], None]):
    """
    Adds a listener for the given event.

    :param event: The event's name.
    :param callback: A listener function.
    """
    ...


@override
def on(event: Literal['gx-slide-change'],
       callback: Callable[[Literal['slider'], Slider], None]):
    ...


@override
def on(event: Literal['gx-page-change'], callback: Callable[[int, int], None]):
    ...


@override
def on(event: Literal['gx-item-show', 'gx-item-hide'], callback: Callable[[Item], None]):
    ...


def off(event: Literal['gx-slide-change', 'gx-page-change', 'gx-item-show', 'gx-item-hide'], callback: Callable):
    """
    Removes a listener for the given event.

    :param event: The event's name.
    :param callback: The listener to remove.
    """
    ...
