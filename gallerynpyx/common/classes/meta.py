from .exceptions import NotExtensibleError, NotSubclassOfError
from .helpers import not_instantiable
from ..iters import first

__all__ = (
    'SingletonMeta', 'RegistryMeta', 'SingletonRegistryMeta',
    'NotInstantiableMeta', 'NotExtensibleMeta', 'StaticsMeta',
    'SimpleEnumMeta'
)


class SingletonMeta(type):

    def __init__(cls, what, bases=None, dict=None):
        super(SingletonMeta, cls).__init__(what, bases, dict)
        cls.__instance = None

    @property
    def __cls__(cls):
        return cls

    @property
    def __instance__(cls):
        return cls.__instance

    def __call__(cls, *args, **kwargs):
        cls = cls.__cls__
        instance = cls.__instance__
        if instance is None:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls.__instance = instance

        return instance


class RegistryMeta(type):
    def __init__(cls, name, bases=None, dict=None):
        super(RegistryMeta, cls).__init__(name, bases, dict)
        cls.__active = cls

    @property
    def __cls__(cls):
        return cls.__active

    def register(cls, target):
        if not issubclass(target, cls):
            raise NotSubclassOfError(target, cls)
        cls.__active = target

    def __call__(cls, *args, **kwargs):
        return super(RegistryMeta, cls.__cls__).__call__(*args, **kwargs)


class SingletonRegistryMeta(RegistryMeta, SingletonMeta):
    def __init__(cls, name, bases=None, dict=None):
        RegistryMeta.__init__(cls, name, bases, dict)
        SingletonMeta.__init__(cls, name, bases, dict)


class NotInstantiableMeta(type):
    __call__ = not_instantiable


class NotExtensibleMeta(type):

    def __init__(cls, name, bases=None, dict=None):
        super(NotExtensibleMeta, cls).__init__(name, bases, dict)
        meta = first(bases or (), key=NotExtensibleMeta.__issubclass__)
        if meta:
            from .objects import NotExtensible, Statics, SimpleEnum
            if not meta in (NotExtensible, Statics, SimpleEnum):
                raise NotExtensibleError(meta)

    @classmethod
    def __issubclass__(cls, it):
        return issubclass(it.__class__, cls)


class StaticsMeta(NotExtensibleMeta):
    __call__ = not_instantiable


class SimpleEnumMeta(StaticsMeta):
    def __iter__(cls):
        return iter(cls.items())

    def keys(cls):
        return (k for k, _ in cls.items())

    def values(cls):
        return (v for _, v in cls.items())

    def items(cls):
        source = getattr(cls, "__dict__", ())
        return ((k, source[k]) for k in source if not k.startswith("_"))
