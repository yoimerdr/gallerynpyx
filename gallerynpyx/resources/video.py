import os

from renpy.display.video import Movie
from .resource import Resource, VIDEOS
from ..common.helpers import isdefine
from ..common.compat import basestring
from ..common.memoized import Memoized
from ..path import isloadable, normpath
from ..sizes.size_int import SizeInt

__all__ = ('VideoResource',)


class VideoResource(Resource):
    __slots__ = (
        '_ext',
    )

    @property
    def ext(self):
        return self._ext

    def _is_supported_source(self, source):
        if not source:
            return False

        if isinstance(source, basestring):
            return isloadable(source, extensions=VIDEOS)

        return self._is_supported_source(getattr(source, '_original_play', None))

    def _is_supported_resource(self, resource):
        return isinstance(resource, VideoResource)

    def _init_from_raw(self, source):
        if isinstance(source, basestring):
            source = normpath(source)
            self._ext = os.path.splitext(source)[1] or None
        elif isdefine(source):
            self._ext = None
            self._init_from_raw(getattr(source, '_original_play'))
        return super(VideoResource, self)._init_from_raw(source)

    def _load(self, force):
        source = self.source
        return getattr(source, '_original_play', source)

    def _displayable(self, size, *args):
        source = self.load(True)
        return Movie(play=source, size=size)
