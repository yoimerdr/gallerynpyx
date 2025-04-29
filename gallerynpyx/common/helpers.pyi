from typing import Any, Callable, AnyStr, TypeVar

_T = TypeVar("_T")


def noact(*args, **kwargs):
    """
    A no-operation function that accepts any arguments and does nothing.

    :param args: The arguments.
    :param kwargs: The keyword arguments.
    """
    ...


def tostring(obj, default: str = None) -> str:
    """
    Converts an object to its string.

    :param obj: The object to convert.
    :param default: Value to return if conversion fails.
    """
    ...


def cast(obj, caster: Callable[[Any, ...], _T], default: _T = None,
         allowed_exceptions: tuple[type, ...] = None, **kwargs) -> _T:
    """
    Attempts to cast an object to a specified type.

    :notes: If the allowed_exceptions is not specified, all exceptions will be caught.
    :param obj: The object to cast.
    :param caster: The casting function or type to use.
    :param default: Value to return if casting fails.
    :param allowed_exceptions: Tuple of exceptions to catch during casting
    :param kwargs: Additional keyword arguments passed to the caster
    :return: The cast object or default value if casting fails.
    """
    ...


def isdefine(obj) -> bool:
    """
    Checks if an object is defined (not None).

    :param obj: The object to check.
    """
    ...


def coerce(value: int, minimum: int, maximum: int) -> int:
    """
    Coerces a value to stay within specified minimum and maximum bounds.

    :param value: The value to coerce.
    :param minimum: The minimum allowed value.
    :param maximum: The maximum allowed value.
    """
    ...
