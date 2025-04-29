from typing import AnyStr, Iterable

from .items import Item
from .slide import Slide
from .slider import Slider


def slide(name: AnyStr, *names: AnyStr, label: AnyStr) -> Slide:
    """
    Creates a slide with the given parameters route.

    :param name: The first route part.
    :param names: The others route parts.
    :param label: A label text.
    """
    ...


def slider(name: AnyStr, *names: AnyStr, label: AnyStr) -> Slider:
    """
    Creates a slider with the given parameters route.

    :param name: The first route part.
    :param names: The others route parts.
    :param label: A label text.
    """
    ...


def has_animation(slide: Slide) -> bool:
    """
    Checks if the slide has any animation resource.

    :param slide: The slider source.
    """
    ...


def eachitem(slider: Slider) -> Iterable[Item]:
    """
    Iterates over each slide/slider and yield its items.

    :param slider: The slider root.
    """
    ...
