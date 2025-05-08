from typing import Any, TypeVar, Tuple, Iterable

from gallerynpyx.common.classes import AbstractClass
from renpy.display.displayable import Displayable

_T = TypeVar("_T")

IMAGES: Tuple[str, ...]
"""
List of image extensions that renpy can load.
"""

VIDEOS: Tuple[str, ...]
"""
List of video extensions that renpy can load.
"""

AUDIO: Tuple[str, ...]
"""
List of audio extensions that renpy can load.
"""


class Resource(AbstractClass):
    """
    The base class for resources.
    """

    def __init__(self: Any, source):
        """
        :param source: The source.
        """
        ...

    @property
    def source(self: Any) -> Any:
        """
        The source object.

        :getter: Gets the source.
        :setter: Sets a new source.
        """
        ...

    @source.setter
    def source(self: Any, value: Any): ...

    def load(self: Any, force: bool = False) -> Any:
        """
        Loads the source.

        :param force: Whether to force the load.
        :return: The loaded object from the source.
        """
        ...

    def displayable(self: Any, size: Iterable[int] = None, ) -> Displayable:
        """
        Creates a displayable from the source.

        :param size: Optional iterable object with width and height dimensions.
        """
        ...

    def dispose(self: Any):
        """
        Disposes memoized values.
        """
        ...

    @classmethod
    def __copy__(cls: type[_T], resource=None) -> _T: ...
