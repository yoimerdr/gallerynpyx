from .helpers import add_metaclass, not_instantiable
from .meta import SingletonMeta, RegistryMeta, NotInstantiableMeta, NotExtensibleMeta, AbstractClassMeta
from .meta import StaticsMeta, SingletonRegistryMeta, SimpleEnumMeta

__all__ = (
    'Singleton', 'SingletonRegistry', 'Registry',
    'NotInstantiable', 'NotExtensible', 'Statics',
    'SimpleEnum', 'AbstractClass'
)


@add_metaclass(SingletonMeta)
class Singleton(object):
    __slots__ = ()
    __init__ = not_instantiable

    @classmethod
    def get_instance(cls, *args, **kwargs):
        return cls.__call__(*args, **kwargs)


@add_metaclass(RegistryMeta)
class Registry(object):
    __slots__ = ()
    __init__ = not_instantiable


@add_metaclass(SingletonRegistryMeta)
class SingletonRegistry(object):
    __slots__ = ()
    __init__ = not_instantiable

    @classmethod
    def get_instance(cls, *args, **kwargs):
        return cls.__call__(*args, **kwargs)


@add_metaclass(NotInstantiableMeta)
class NotInstantiable(object):
    pass


@add_metaclass(NotExtensibleMeta)
class NotExtensible(object):
    __slots__ = ()
    __init__ = not_instantiable


@add_metaclass(AbstractClassMeta)
class AbstractClass(object):
    __slots__ = ()


@add_metaclass(StaticsMeta)
class Statics(object):
    pass


@add_metaclass(SimpleEnumMeta)
class SimpleEnum(object):
    pass
