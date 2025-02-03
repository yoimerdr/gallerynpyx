from renpy.display.layout import Composite
from .resource import Resource
from ..sizes.size_int import SizeInt

try:
    from renpy.display.displayable import Displayable
except ImportError:
    from renpy.display.core import Displayable

__all__ = ('DisplayableResource',)


class DisplayableResource(Resource):
    __slots__ = ()

    def _is_supported_source(self, source):
        return source and isinstance(source, Displayable)

    def _is_compatible_resource(self, resource):
        return isinstance(resource, DisplayableResource)

    def _load(self, force):
        return self.source

    def scale(self, size):
        width, height = SizeInt.of(size)
        image = self.load(True)
        return Composite((width, height), (0, 0), image)
