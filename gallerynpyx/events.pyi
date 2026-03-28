from typing import Callable, Literal, overload

from .handler.base.base import BaseHandler
from .slides.items import Item
from .slides.slide import Slide
from .slides.slider import Slider


@overload
def on(event: Literal["gx-slide-change"],
       callback: Callable[[Literal["slide"], Slide, BaseHandler], None]) -> None:
    """
    Adds a listener for slide changes.

    :param event: The event name.
    :param callback: Listener called with the change kind, the target slide and the active handler.
    """
    ...


@overload
def on(event: Literal["gx-slide-change"],
       callback: Callable[[Literal["slider"], Slider, BaseHandler], None]) -> None:
    """
    Adds a listener for slider changes.

    :param event: The event name.
    :param callback: Listener called with the change kind, the target slider and the active handler.
    """
    ...


@overload
def on(event: Literal["gx-page-change"],
       callback: Callable[[int, int, BaseHandler], None]) -> None:
    """
    Adds a listener for page changes.

    :param event: The event name.
    :param callback: Listener called with the new page, the previous page and the active handler.
    """
    ...


@overload
def on(event: Literal["gx-item-show", "gx-item-hide"],
       callback: Callable[[Item], None]) -> None:
    """
    Adds a listener for item visibility events.

    :param event: The event name.
    :param callback: Listener called with the related item.
    """
    ...


def on(event: str, callback: Callable[..., None]) -> None:
    """
    Adds a listener for the given gallery event.

    :param event: The event name.
    :param callback: Listener function for that event.
    """
    ...


def off(event: str, callback: Callable[..., None]) -> None:
    """
    Removes a listener for the given gallery event.

    :param event: The event name.
    :param callback: The listener to remove.
    """
    ...
