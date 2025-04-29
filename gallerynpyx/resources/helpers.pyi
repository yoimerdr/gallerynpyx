from typing import TypeVar, Union, AnyStr

from renpy.display.displayable import Displayable
from renpy.display.im import Image
from renpy.display.transform import ATLTransform
from renpy.display.video import Movie
from .animation import AnimationResource
from .displayable import DisplayableResource
from .images import ImageResource
from .resource import Resource
from .video import VideoResource

_T = TypeVar("_T", bound=Resource)


def guess(source: _T, allow_same: bool = True) -> _T:
    """
    Guess the resource type from the source.

    :notes: If the source is named and a None object is retrieved, is assumed to be an image source.
    :param source: Any valid source for the defined resources.
    :param allow_same: Whether to return the same source if it's already a resource.
    :return: The guessed resource.
    """
    ...


def guess(source: ATLTransform, allow_same: bool = True) -> AnimationResource: ...


def guess(source: Movie, allow_same: bool = True) -> VideoResource: ...


def guess(source: Image, allow_same: bool = True) -> ImageResource: ...


def guess(source: Displayable, allow_same: bool = True) -> DisplayableResource: ...


def guess(source: AnyStr, allow_same: bool = True) -> Union[ImageResource, AnimationResource, VideoResource]: ...
