from typing import TypeVar, Any, Iterable


_T = TypeVar('_T')


class Singleton(object):
    """
    Base class for singleton pattern implementation.

    Ensures only one instance of the class exists and provides
    access to that instance through class methods.
    """
    __slots__ = ()

    @classmethod
    @property
    def __cls__(cls: type[_T]) -> _T:
        """
        Returns the singleton class.
        """
        ...

    @classmethod
    def __instance__(cls: type[_T]) -> _T:
        """
        Returns the singleton instance.
        """
        ...

    @classmethod
    def get_instance(cls: type[_T], *args, **kwargs) -> _T:
        """
        Creates or returns the singleton instance.

        :param args: Init class arguments.
        :param kwargs: Init class keyword arguments.
        """
        ...


class Registry(object):
    """
    Base class for implementing a registry pattern.

    Provides functionality to register and manage class implementations.
    """

    __slots__ = ()

    @classmethod
    @property
    def __cls__(cls: type[_T]) -> _T:
        """
        Returns the registry class.
        """
        ...

    @classmethod
    def register(cls: type[_T], target: type[_T]):
        """
        Registers a target class in the registry.

        :param target: The class to register.
        """
        ...


class SingletonRegistry(Singleton, Registry):
    """
    Combines the functionality of both Singleton and Registry patterns.
    """
    __slots__ = ()


class NotInstantiable(object):
    """
    Base class for objects that should not be instantiated.
    """
    pass


class NotExtensible(object):
    """
    Base class for objects that cannot be extended/subclassed.
    """
    __slots__ = ()

    @classmethod
    def __issubclass__(cls: type[_T], it: type) -> bool:
        """
        Checks if a class is a subclass of NotExtensible.

        :param it: The class to check.
        """
        ...


class AbstractClass(object):
    """
    Base class for defining abstract classes.
    """
    __slots__ = ()

    @classmethod
    def __issubclass__(cls: type[_T], it: type) -> bool:
        """
        Checks if a class is a subclass of the current class.

        :param it: The class to check.
        """
        ...


class Statics(object):
    """
    Base class for implementing only static accesses.
    """
    pass


class SimpleEnum(object):
    """
    Base class for a simple enum-like implementation.
    """

    @classmethod
    def __iter__(cls) -> Iterable[tuple[str, Any]]:
        """
        Returns an iterable over the enum items.
        """
        ...

    @classmethod
    def keys(cls) -> Iterable[str]:
        """
        Returns an iterable over enum names.
        """
        ...

    @classmethod
    def values(cls) -> Iterable[Any]:
        """
        Returns an iterable over enum values.
        """
        ...

    @classmethod
    def items(cls) -> Iterable[tuple[str, Any]]:
        """
        Returns an iterable over enum items (key, value).
        """
        ...
