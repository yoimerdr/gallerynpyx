from renpy.display.image import get_registered_image
from renpy.display.transform import ATLTransform
from .exceptions import UnloadableSourceError, UnsupportedSourceError
from .resource import Resource
from ..common.helpers import isdefine
from ..common.compat import basestring

__all__ = ('AnimationResource',)


class AnimationResource(Resource):
    __slots__ = ()

    def _is_supported_source(self, source):
        return source and isinstance(source, (basestring, ATLTransform))

    def _is_supported_resource(self, resource):
        return isinstance(resource, AnimationResource)

    def _load(self, force):
        animation = source = self.source

        if not isinstance(source, ATLTransform):
            animation = get_registered_image(source)
            if isdefine(animation):
                if not isinstance(animation, ATLTransform):
                    raise UnsupportedSourceError(source, self)
            elif force:
                raise UnloadableSourceError(source)

        return animation
