from typing import Any, Union, AnyStr, Iterable

from renpy.display.video import Movie
from .resource import Resource


class VideoResource(Resource):
    """
    The class for video resources, whether the filepath or the object Movie as such.
    """

    def __init__(self: Any, source: Union[AnyStr, Movie, VideoResource]):
        """
        :param source: The video filepath, the Movie itself or an video resource.
        """
        ...

    @property
    def source(self: Any) -> Union[str, Movie]:
        ...

    @source.setter
    def source(self: Any, value: Union[str, Movie, VideoResource]):
        ...

    @property
    def ext(self: Any) -> str:
        """
        The video extension.

        :getter: Gets the video extension.
        """
        ...

    def load(self: Any, force: bool = False) -> str:
        """
        Loads the source and returns the filepath.

        :param force: Whether to force the load.
        :return:
        """

    def displayable(self: Any, size: Iterable[int] = None) -> Movie:
        """
        Creates a displayable from the source.

        :param size: Optional iterable object with width and height dimensions.
        :returns: A ``Movie`` created from the source.
        """
        ...
