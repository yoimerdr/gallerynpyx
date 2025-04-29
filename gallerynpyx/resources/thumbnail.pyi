from typing import Any, Union, AnyStr, Iterable

from renpy.display.displayable import Displayable
from renpy.display.im import Scale, Composite, Image
from renpy.display.transform import ATLTransform
from renpy.display.video import Movie
from .displayable import DisplayableResource
from .images import ImageResource
from .resource import Resource

__all__ = ('Thumbnail', 'creates')


def creates(resource: Union[DisplayableResource, ImageResource], size: Iterable[int]) -> Union[Scale, Composite]:
    """
    Scales o composites the resource to the given size.

    :notes: Use scale() method for displayable resources.
    :notes: Use composite() method for image resources.
    :raises IncompatibleResourceError: If the resource is not displayable or image.
    :param resource: The displayable or image resource.
    :param size: The iterable object with width and height dimensions.
    :return: The scale or composite object.
    """
    ...

def creates_raw(source, size: Iterable[int]) -> Union[Scale, Composite]:
    """
    Creates a thumbnail and scales or composites the loaded object.

    :param source: Any valid source or a resource.
    :param size: The iterable object with width and height dimensions.
    :return: The scale or composite object.
    """
    ...

class Thumbnail(object):
    """
    The wrapper class for create thumbnails from resources.
    """
    def __init__(self: Any, resource):
        """
        :param resource: Any valid source or a resource.
        """
        ...

    @property
    def resource(self: Any) -> Resource:
        """
        The current active resource.

        :notes: If you set a custom resource, the active resource will be that.
        :getter: Returns the active resource.
        """
        ...

    def set_custom(self: Any, resource: Union[Resource, AnyStr, Displayable, Movie, ATLTransform, Image]):
        """
        Sets a custom resource for create the thumbnail.

        :param resource: Any valid source or a resource.
        """
        ...

    def prepare(self: Any, allow_animation_thumbnail: bool = False, video_thumbnails_folder: AnyStr = None) -> Union[ImageResource, DisplayableResource]:
        """
        Prepares the active resource for create the thumbnail.

        :notes: If the active resource is not displayable or image, it will be modified in accordance with the arguments given.
        :raises IncompatibleResourceError: If the active resource is not displayable or image.
        :param allow_animation_thumbnail: Whether to try to get the first image from the animation.
        :param video_thumbnails_folder: The folder where to search for video thumbnails.
        :return: A displayable or image resource.
        """
        ...

    def create(self: Any, size, allow_animation_thumbnail: bool = False, video_thumbnails_folder: AnyStr = None) -> Union[Scale, Composite]:
        """
        Prepares and creates the thumbnail from the active resource.

        :param size: The iterable object with width and height dimensions.
        :param allow_animation_thumbnail: Whether to try to get the first image from the animation.
        :param video_thumbnails_folder: The folder where to search for video thumbnails.
        :return:
        """
        ...
