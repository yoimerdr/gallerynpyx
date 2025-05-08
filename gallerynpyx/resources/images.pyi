from typing import Union, Any, AnyStr, Iterable

from renpy.display.im import Image, Composite, Scale
from .displayable import DisplayableResource


class ImageResource(DisplayableResource):
    """
    The class for image resources, whether named, the filepath or the object as such.
    """
    def __init__(self: Any, source: Union[AnyStr, Image, ImageResource]):
        """
        :param source: The image's name, the image filepath, the image itself or an image resource.
        """
        ...

    @property
    def source(self: Any) -> Union[AnyStr, Image]:
        """
        The image source (name, image filepath or image object).

        :getter: Gets the source.
        :setter: Sets a new source.
        """
        ...

    @source.setter
    def source(self: Any, value: Union[AnyStr, Image, ImageResource]): ...

    @property
    def ext(self: Any) -> Union[AnyStr, None]:
        """
        The image extension.

        :getter: Gets the image extension or None if the image is named.
        """
        ...

    def load(self: Any, force: bool = False) -> Union[Image, None]:
        """
        Loads the source.

        :raises UnsupportedSourceError: If the object retrieved from the name is not an image.
        :raises UnloadableSourceError: If the filepath is not loadable or is not from an image.

        :param force: Whether to force the load.
        :return: The loaded image object.
        """
        ...

    @property
    def is_named(self: Any) -> bool:
        """
        Whether the source is an image's name.
        """
        ...

    def scale(self: Any, size: Iterable[float]) -> Scale:
        """
        Loads the source and scales it.

        :notes: The load is make it with the force flag.
        :see: load
        :param size: The iterable object with width and height dimensions.
        :return: The Scale object.
        """
        ...

    def composite(self: Any, size: Iterable[float]) -> Composite:
        """
        Loads the source and composites it.

        :notes:
            * The load is make it with the force flag.
            * This method is an alternative to scale if you want to maintain the aspect ratio of the image.
        :see: load
        :param size: The iterable object with width and height dimensions.
        :return: The Composite object.
        """
        ...

    def displayable(self: Any, size: Iterable[int] = None) -> Union[Composite, Image]:
        """
        Creates a displayable from the source.

        :notes: The load is make it with the force flag.
        :see: load, composite
        :param size: Optional iterable object with width and height dimensions.
        :return: The Composite object if the size is given, else the loaded Image object.
        """

        ...
