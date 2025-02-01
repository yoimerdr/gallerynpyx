from .exceptions import UnsupportedSourceError, IncompatibleResourceError
from ..common.classes.helpers import not_implemented, representation
from ..common.classes.objects import AbstractClass
from ..common.helpers import noact

__all__ = ('Resource', 'IMAGES', 'VIDEOS', 'AUDIO')

IMAGES = ('.png', '.jpg', '.web', '.jpeg', '.webp')

VIDEOS = ('.webm', '.avi', '.mp4', '.wav', '.mkv', '.ogv')

AUDIO = ('.mp3', '.ogg', '.opus', ".mp2")


class Resource(AbstractClass):
    __slots__ = (
        '_src',
    )

    def __init__(self, source):
        if isinstance(source, Resource):
            if source.__class__ is self.__class__:
                self._init_from_self(source)
            elif not self._is_compatible_resource(source):
                raise IncompatibleResourceError(source, self)
            else:
                self._init_from_res(source)
        elif not self._is_supported_source(source):
            raise UnsupportedSourceError(source, self)
        else:
            self._init_from_raw(source)

    def _init_from_res(self, res):
        self._init_from_raw(res.source)

    def load(self, force=False, **kwargs):
        if force:
            self._force_load_init()
        return self._load(force, **kwargs)

    def _init_from_raw(self, raw):
        self._src = raw

    @property
    def source(self):
        return self._src

    @source.setter
    def source(self, value):
        self.__init__(value)

    def __repr__(self):
        return representation(self, source=self.source)

    @classmethod
    def __copy__(cls, resource=None):
        if resource is None:
            return None
        return cls(resource.source)

    _load = not_implemented
    _force_load_init = noact
    _init_from_self = _init_from_res
    _is_supported_source = _is_compatible_resource = bool
