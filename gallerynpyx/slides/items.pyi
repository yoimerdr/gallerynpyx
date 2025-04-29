from typing import Any, Union, AnyStr, Callable

from renpy.display.displayable import Displayable
from renpy.display.im import Image
from renpy.display.transform import ATLTransform
from renpy.display.video import Movie
from ..resources.resource import Resource
from ..resources.thumbnail import Thumbnail


def isitem(value):
    """
    Checks if value is an instance of ``Item``
    :param value: The value to check
    """
    ...


class Item(object):
    """
    Dataclass for an item in a ``Slide``.
    """

    def __init__(self: Any, resource: Union[Resource, AnyStr, Movie, ATLTransform, Image, Displayable],
                 song: AnyStr = None, condition: Callable[[Item], bool] = None, tooltip: AnyStr = None, locked_tooltip: AnyStr = None):
        """
        :param resource: Any valid source or a ``Resource`` instance.
        :param song: A filepath for a song.
        :param condition: A callable to evaluate.
        :param tooltip: A text for a tooltip.
        :param locked_tooltip: A text for a tooltip.
        """
        ...

    @property
    def resource(self: Any) -> Resource:
        """
        The resource associated with this item.

        :notes: The ``resource`` instance is the same as the ``thumbnail`` resource.
        :getter: Returns the resource associated with this item.
        """
        ...

    @property
    def thumbnail(self: Any) -> Thumbnail:
        """
        The thumbnail associated with this item.

        :notes: The ``resource`` instance is the same as the ``thumbnail`` resource.
        :getter: Returns the thumbnail associated with this item.
        """
        ...

    @property
    def locked(self: Any) -> bool:
        """
        Evaluates if the item is locked. That is, it does not meet the given ``condition``.
        """
        ...

    @property
    def song(self: Any) -> Union[AnyStr, None]:
        """
        The song filepath.

        :getter: Returns the song filepath.
        :setter: Sets a new song filepath.
        """
        ...

    @song.setter
    def song(self: Any, song: Union[AnyStr, None]):
        ...

    @property
    def condition(self: Any) -> Union[Callable[[Item], bool], None]:
        """
        The unlocking condition.

        :getter: Returns the unlocking condition.
        :setter: Sets a new unlocking condition.
        """
        ...

    @condition.setter
    def condition(self: Any, condition: Union[Callable[[Item], bool], None]):
        ...

    @property
    def tooltip(self: Any) -> Union[AnyStr, None]:
        """
        The tooltip text.

        :getter: Returns the tooltip text.
        :setter: Sets a new tooltip text.
        """
        ...

    @tooltip.setter
    def tooltip(self: Any, tooltip: Union[AnyStr, None]):
        ...

    @property
    def locked_tooltip(self: Any) -> Union[AnyStr, None]:
        """
        The locked tooltip text.

        :getter: Returns the locked tooltip text.
        :setter: Sets a new locked tooltip text.
        """
        ...

    @locked_tooltip.setter
    def locked_tooltip(self: Any, tooltip: Union[AnyStr, None]):
        ...

    def __repr__(self: Any) -> str:
        ...

    def __hash__(self: Any) -> int:
        ...
