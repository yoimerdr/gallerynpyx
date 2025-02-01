import os

from .animation import AnimationResource
from .displayable import DisplayableResource
from .exceptions import IncompatibleResourceError
from .helpers import guess
from .images import ImageResource
from .resource import IMAGES
from .video import VideoResource
from ..anim import get_images
from ..common.classes.helpers import representation
from ..common.iters import first
from ..path import isloadable, join

__all__ = ('Thumbnail', 'creates')


def creates(resource, size):
    return Thumbnail(resource).create(size)


class Thumbnail(object):
    __slots__ = (
        '_res', '_cus'
    )

    def __init__(self, resource):
        self._res = guess(resource)
        self._cus = None

    @property
    def resource(self):
        return self._res if self._cus is None else self._cus

    def set_custom(self, resource):
        if resource is None:
            self._cus = None
            return
        self._cus = guess(resource)

    def create(self, size, allow_animation_thumbnail=False, video_thumbnails_folder=None):
        resource = self.resource
        custom = None

        if isinstance(resource, ImageResource):
            return resource.composite(size)
        elif isinstance(resource, DisplayableResource):
            return resource.scale(size)

        if video_thumbnails_folder and isinstance(resource, VideoResource):
            path = os.path.splitext(resource.load(True))[0]
            paths = (join(video_thumbnails_folder, path + ext) for ext in IMAGES)
            custom = first(paths, key=isloadable)
        elif allow_animation_thumbnail and isinstance(resource, AnimationResource):
            custom = first(get_images(resource.load(True)))

        if not custom:
            raise IncompatibleResourceError(resource)

        self.set_custom(custom)
        return self.create(size)

    def __repr__(self):
        return representation(
            self,
            resource=self._res
        )
