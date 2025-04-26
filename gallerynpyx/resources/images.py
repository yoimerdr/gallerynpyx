import os

from renpy.display import im
from renpy.display.im import Image, Composite, Scale
from renpy.display.image import get_registered_image
from .displayable import DisplayableResource
from .exceptions import UnsupportedSourceError, UnloadableSourceError
from .resource import IMAGES
from ..common.compat import basestring
from ..common.memoized import Memoized
from ..path import isloadable, normpath
from ..sizes.size_int import SizeInt

__all__ = ('ImageResource',)


class ImageResource(DisplayableResource):
    __slots__ = (
        '_ext', '_cmem'
    )

    def __init__(self, source):
        self._cmem = Memoized(self._composite)
        super(ImageResource, self).__init__(source)

    def _is_supported_source(self, source):
        if not source:
            return False

        if isinstance(source, basestring):
            source = normpath(source)
            ext = os.path.splitext(source)[1]
            return isloadable(source, extensions=IMAGES) if ext else True

        return isinstance(source, Image)

    def _init_from_self(self, resource):
        self._ext = resource.ext
        super(ImageResource, self)._init_from_raw(resource.source)

    def _init_from_raw(self, source):
        ext = None
        if isinstance(source, basestring):
            source = normpath(source)
            ext = os.path.splitext(source)[1] or None
        self._ext = ext
        super(ImageResource, self)._init_from_raw(source)

    def _init(self, source):
        self._cmem.dispose()
        super(ImageResource, self)._init(source)

    def _load(self, force):
        source = self.source
        if isinstance(source, Image):
            return source

        ext = self.ext

        if not ext:
            image = get_registered_image(source)
            if image and not isinstance(image, Image):
                raise UnsupportedSourceError(source, self)
        else:
            image = Image(source)

        if image is None and force:
            raise UnloadableSourceError(source)

        return image

    @property
    def ext(self):
        return self._ext

    @property
    def is_named(self):
        return not self.ext and isinstance(self.source, basestring)

    def _scales(self, size):
        image = self.load(True)
        surfer = im.cache.get(image)

        source = SizeInt.of(surfer.get_size())
        xsize = size.scale(source.aspect_ratio)

        return Scale(image, xsize.width, xsize.height), xsize, size

    def _scale(self, size, *args):
        return self._scales(SizeInt.of(size))[0]

    def _composite(self, size, *args):
        image, xsize, size = self._scales(size)
        x = int(size.width / 2.0 - xsize.width / 2.0)
        y = int(size.height / 2.0 - xsize.height / 2.0)
        return Composite(tuple(size), (x, y), image)

    def _displayable(self, size, *args):
        return self._load(True) if size is None else self._composite(size)

    def dispose(self):
        self._cmem.dispose()
        super(ImageResource, self).dispose()

    def composite(self, size):
        return self._cmem.evaluate(SizeInt.of(size), self.source)
