import os

from renpy.display.im import Image, Composite, Scale
from renpy.display.image import get_registered_image
from .displayable import DisplayableResource
from .exceptions import UnsupportedSourceError, UnloadableSourceError
from .resource import IMAGES
from ..common.compat import basestring
from ..path import isloadable, normpath
from ..sizes.size_int import SizeInt

__all__ = ('ImageResource',)


class ImageResource(DisplayableResource):
    __slots__ = (
        '_ext',
    )

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
        size = SizeInt.of(size)
        image = self.load(True)

        source = SizeInt.of(image.load().get_size())
        xsize = size.scale(source.aspect_ratio)

        return Scale(image, xsize.width, xsize.height), xsize, size

    def scale(self, size):
        return self._scales(size)[0]

    def composite(self, size):
        image, xsize, size = self._scales(size)
        x = int(size.width / 2.0 - xsize.width / 2.0)
        y = int(size.height / 2.0 - xsize.height / 2.0)
        return Composite(tuple(size), (x, y), image)
