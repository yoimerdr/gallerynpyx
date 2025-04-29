from typing import Union, Any, Iterable

from renpy.display.displayable import Displayable
from renpy.display.im import Composite
from .resource import Resource


class DisplayableResource(Resource):
    """
    The class for basic displayable resources (e.g., Solid, Displayable, etc.).
    """

    def __init__(self: Any, source: Union[Displayable, DisplayableResource]):
        """
        :param source: A displayable object or a displayable resource.
        """
        ...

    @property
    def source(self: Any) -> Displayable:
        """
        The displayable source object.

        :getter: Gets the source.
        :setter: Sets a new source.
        """
        ...

    @source.setter
    def source(self: Any, value: Union[Displayable, DisplayableResource]): ...

    def load(self: Any, force: bool = False) -> Displayable:
        """
        Loads the source.

        :notes: This has the same behavior as the **source** property.
        :param force: Whether to force the load.
        :return: The loaded object from the source.
        """
        ...

    def scale(self: Any, size: Iterable[int]) -> Composite:
        """
        Composites the displayable with the given size.

        :param size: The iterable object with width and height dimensions.
        :return: The Composite object.
        """
        ...

    def displayable(self: Any, size: Iterable[int] = None) -> Union[Composite, Displayable]:
        """
        Creates a displayable from the source.

        :param size: Optional iterable object with width and height dimensions.
        :return: The Composite object if the size is given, otherwise the Displayable.
        """
        ...

