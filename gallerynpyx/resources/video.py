import os

from renpy.display.video import Movie
from .resource import Resource, VIDEOS
from ..common.compat import basestring
from ..path import isloadable, normpath

__all__ = ('VideoResource',)


class VideoResource(Resource):
    __slots__ = (
        '_ext',
    )

    def _is_supported_source(self, source):
        if not source:
            return False

        if isinstance(source, basestring):
            return isloadable(source, extensions=VIDEOS)

        return self._is_supported_source(getattr(source, '_original_play'))

    def _is_supported_resource(self, resource):
        return isinstance(resource, VideoResource)

    def _init_from_raw(self, source):
        if isinstance(source, basestring):
            source = normpath(source)
            self._ext = os.path.splitext(source)[1] or None
            return super(VideoResource, self)._init_from_raw(source)

        return self._init_from_raw(getattr(source, '_original_play'))

    def _load(self, force):
        source = self.source
        if isinstance(source, Movie):
            return getattr(source, '_original_play')

        return source

    @property
    def ext(self):
        return self._ext
