from renpy.display.im import Scale, FactorScale
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
        if isinstance(image, Scale):
            image.width = width
            image.height = height
            return image
        elif isinstance(image, FactorScale):
            image = image.image
        return Scale(image, width, height)
