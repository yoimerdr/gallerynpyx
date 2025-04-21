import copy
import os

try:
    from renpy.display.displayable import Displayable
except ImportError:
    from renpy.display.core import Displayable
from renpy.display.im import Image
from renpy.display.image import Solid
from renpy.display.transform import ATLTransform
from renpy.display.video import Movie
from .animation import AnimationResource
from .displayable import DisplayableResource
from .exceptions import UnsupportedSourceError
from .images import ImageResource
from .resource import Resource, IMAGES, VIDEOS
from .video import VideoResource
from ..color import ishex
from ..common.compat import basestring

__all__ = (
    'guess',
)


def guess(source, allow_same=True):
    if not source:
        raise UnsupportedSourceError(source)

    builder = None

    if isinstance(source, Resource):
        return source if allow_same else copy.copy(source)
    if isinstance(source, basestring):
        ext = os.path.splitext(source)[1]
        if not ext:
            builder = ImageResource
            if ishex(source, True):
                builder = DisplayableResource
                source = Solid(source)
        elif ext in IMAGES:
            builder = ImageResource
        elif ext in VIDEOS:
            builder = VideoResource
    elif isinstance(source, Image):
        builder = ImageResource
    elif isinstance(source, Movie):
        builder = VideoResource
    elif isinstance(source, ATLTransform):
        builder = AnimationResource
    elif isinstance(source, Displayable):
        builder = DisplayableResource

    if not builder:
        raise UnsupportedSourceError(source)

    return builder(source)
