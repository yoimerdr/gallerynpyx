from typing import Iterable, SupportsIndex, Any

from .items import Item
from .base import SlideBase


class Slide(SlideBase):
    """
    A sequence of ``Item``.
    """

    def add(self: Any, item: Item) -> bool: ...

    def remove(self: Any, item: Item) -> bool: ...

    def get(self: Any, item: SupportsIndex) -> Any: ...

    def set(self: Any, key: SupportsIndex, item: Item) -> bool: ...

    def __iter__(self: Any) -> Iterable[Item]: ...

    def __contains__(self: Any, item: Item) -> bool: ...

    def __getitem__(self: Any, item: SupportsIndex) -> Item: ...

    def __setitem__(self: Any, key: SupportsIndex, value: Item) -> bool: ...

    def __delitem__(self: Any, key: SupportsIndex) -> bool: ...

    def extend(self: Any, iterable: Iterable[Item]):
        """
        Extend the sequence by appending items.
        :param iterable: An iterable of items
        """
        ...

    def insert(self: Any, index: SupportsIndex, item: Item) -> bool:
        """
        Inserts an item at the given index.

        :param index: The index where the item will be inserted.
        :param item: The item to be inserted.
        :return: True if the insertion was successful, False otherwise.
        """
        ...

    def index(self: Any, item: Item, start: SupportsIndex = None, end: SupportsIndex = None) -> int:
        """
        Gets the index of the given item.

        :param item: The item to be searched.
        :param start: The start index.
        :param end: The end index.
        """
        ...
