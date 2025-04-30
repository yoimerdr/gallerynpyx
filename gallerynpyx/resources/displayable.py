from renpy.display.layout import Composite
from .resource import Resource
from ..common.memoized import Memoized
from ..sizes.size_int import SizeInt

try:
    from renpy.display.displayable import Displayable
except ImportError:
    from renpy.display.core import Displayable

__all__ = ('DisplayableResource',)


class DisplayableResource(Resource):
    __slots__ = (
        '_smem',
    )

    def __init__(self, source):
        self._smem = Memoized(self._scale)
        super(DisplayableResource, self).__init__(source)

    def _is_supported_source(self, source):
        return source and isinstance(source, Displayable)

    def _is_compatible_resource(self, resource):
        return isinstance(resource, DisplayableResource)

    def _load(self, force):
        return self.source

    def _scale(self, size, *args):
        width, height = size
        image = self.load(True)
        return Composite((width, height), (0, 0), image)

    def scale(self, size):
        return self._smem.evaluate(SizeInt.of(size), self.source)

    def _displayable(self, size, *args):
        return self.load(True) if size is None else self._scale(size)

    def dispose(self):
        self._smem.dispose()
        super(DisplayableResource, self).dispose()
