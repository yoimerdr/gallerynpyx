import os

from renpy.display.video import Movie
from .resource import Resource, VIDEOS
from ..common.compat import basestring
from ..common.memoized import Memoized
from ..path import isloadable, normpath

__all__ = ('VideoResource',)


class VideoResource(Resource):
    __slots__ = (
        '_ext',
        '_dmem',
    )

    def __init__(self, source):
        self._dmem = Memoized(self._displayable)
        super(VideoResource, self).__init__(source)

    def _is_supported_source(self, source):
        if not source:
            return False

        if isinstance(source, basestring):
            return isloadable(source, extensions=VIDEOS)

        return self._is_supported_source(getattr(source, '_original_play', None))

    def _is_supported_resource(self, resource):
        return isinstance(resource, VideoResource)

    def _init_from_raw(self, source):
        ext = None
        if isinstance(source, basestring):
            source = normpath(source)
            ext = os.path.splitext(source)[1] or None
        self._ext = ext
        return super(VideoResource, self)._init_from_raw(source)

    def _load(self, force):
        source = self.source
        return getattr(source, '_original_play', source)

    def _displayable(self, source):
        return source if not self.ext else Movie(play=source)

    def displayable(self, *args):
        return self._dmem.evaluate(self.source)

    @property
    def ext(self):
        return self._ext
