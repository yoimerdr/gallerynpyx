from typing import SupportsIndex, Iterable, Callable, TypeVar, Union

_T = TypeVar('_T')
_R = TypeVar('_R')


def imap(fn: Callable[[_T], _R], iterable: Iterable[_T]) -> Iterable[_R]:
    """
    Map a function over an iterable, returning an iterator.

    :param fn: Function to apply to each element.
    :param iterable: Input iterable of elements
    """
    ...


def ifilter(fn: Callable[[_T], bool], iterable: Iterable[_T]) -> Iterable[_T]:
    """
    Filter an iterable by applying a predicate function, returning an iterator.

    :param fn: Predicate function that returns True for elements to keep
    :param iterable: Input iterable of elements
    """
    ...


def irange(start: SupportsIndex, stop: SupportsIndex = None, step: SupportsIndex = 1) -> Iterable[int]:
    """
    Create an iterator that generates a sequence of numbers.
    """
    ...


def first(iterable: Iterable[_T], default: _T = None, key: Callable[[_T], bool] = None) -> Union[_T, None]:
    """
    Return the first element of an iterable that matches the key function.

    :notes: The default key is ``bool``
    :param iterable: Input iterable of elements
    :param default: Value to return if no element is found
    :param key: Optional predicate function to filter elements
    :return: First matching element or default if none found
    """
    ...


def last(iterable, default=None, key: Callable[[_T], bool] = None) -> Union[_T, None]:
    """
    Return the last element of an iterable that matches the key function.

    :notes: The default key is ``bool``
    :param iterable: Input sequence of elements
    :param default: Value to return if no element is found, defaults to None
    :param key: Optional predicate function to filter elements
    :return: Last matching element or default if none found
    """
    ...
