from typing import TypeVar, override, Any, Iterable

_T = TypeVar("_T")


class SingletonMeta(type):
    """
    A metaclass for implements the Singleton pattern.
    """
    @property
    def __cls__(cls: type[_T]) -> type[_T]:
        """
        The actual class type.

        :getter: Gets the actual class type.
        """
        ...

    @property
    def __instance__(cls: type[_T]) -> _T:
        """
        The single instance of the class.

        :getter: Gets the single instance of the class.
        """
        ...


class RegistryMeta(type):
    """
    The metaclass for implements the Registry pattern.
    """
    @property
    def __cls__(cls: type[_T]) -> type[_T]:
        """
        The actual class type.

        :getter: Gets the actual class type.
        """
        ...

    @override
    @property
    def __cls__(cls: Any) -> type[_T]: ...

    def register(cls: type[_T], target: type[_T]):
        """
        Register a class as active class.

        :param target: The new active class.
        """
        ...

    @override
    def register(cls: Any, target: type[_T]): ...


class SingletonRegistryMeta(RegistryMeta, SingletonMeta):
    """
    Metaclass for implements the Singleton and Registry pattern.
    """
    ...


class NotInstantiableMeta(type):
    """
    Metaclass for not instantiable classes.
    """
    ...


class NotExtensibleMeta(type):
    """
    Metaclass for not extensible classes.
    """

    @classmethod
    def __issubclass__(cls, it: type) -> bool:
        """
        Checks if the give class is subclass of the current class.

        :param it: The target class.
        """
        ...


class AbstractClassMeta(type):
    """
    Metaclass for abstract classes.
    """
    @classmethod
    def __issubclass__(cls, it: type) -> bool:
        """
        Checks if the give class is subclass of the current class.

        :param it: The target class.
        """
        ...


class StaticsMeta(NotExtensibleMeta):
    """
    Metaclass for classes that only allow static accesses.
    """
    ...


class SimpleEnumMeta(StaticsMeta):
    """
    Metaclass for simple enum-like classes.
    """
    def __iter__(cls) -> Iterable[tuple[str, Any]]:
        """
        Returns an iterator over the enum items.
        """
        ...

    def keys(cls) -> Iterable[str]:
        """
        Returns an iterator over enum names.
        """
        ...

    def values(cls) -> Iterable[Any]:
        """
        Returns an iterator over enum values.
        """
        ...

    def items(cls) -> Iterable[tuple[str, Any]]:
        """
        Returns an iterator over enum items (key, value).
        """
        ...
