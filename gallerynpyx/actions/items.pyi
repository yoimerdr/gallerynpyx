from typing import Any, TypeVar

from renpy.ui import Action
from ..common.classes.objects import Registry
from ..resources.resource import Resource
from ..slides.items import Item

_R = TypeVar('_R', bound=Resource)


def prepare_resource(resource: _R) -> _R:
    """
    Prepares the resource for display.

    :notes: For non-animation resources, create a displayable with the same size as the screen.
    :notes: For animation resources, assign the animation speed if it's allowed.
    :param resource: Any resource
    :return: The prepared resource.
    """
    ...


class ShowItem(Action, Registry):
    """
    An action to display the resource of an item.
    """

    def __init__(self: Any, item: Item):
        """
        :param item: The item instance.
        """
        ...

    def get_selected(self: Any) -> bool:
        """
        Method used internally by renpy
        """
        ...

    def get_tooltip(self: Any) -> bool:
        """
        Method used internally by renpy
        """
        ...

    def show(self: Any):
        """
        Shows the resource of the item.
        """
        ...

    def __call__(self: Any, *args, **kwargs):
        ...
