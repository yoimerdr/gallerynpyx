from .base import SlideBase
from .items import isitem
from ..common.iters import ifilter

__all__ = ('Slide',)

class Slide(SlideBase):
    __slots__ = ()

    def __init__(self, name, parent=None, label=None):
        super(Slide, self).__init__(name, parent, label)
        self._items = []

    def _add(self, item):
        if not isitem(item):
            return False
        self._items.append(item)
        return True

    def _remove(self, index):
        try:
            del self._items[index]
            return True
        except (IndexError, TypeError):
            return False

    def _get(self, index):
        try:
            return self._items[index]
        except (IndexError, TypeError):
            return None

    def _clear(self):
        del self._items[:]

    def _set(self, index, value):
        try:
            if isinstance(index, slice):
                self._items[index] = ifilter(isitem, value)
            elif not isitem(value, ):
                return False
            else:
                self._items[index] = value
            return True
        except (IndexError, TypeError):
            return False

    def extend(self, iterable):
        self._items.extend(ifilter(isitem, iterable))

    def insert(self, index, item):
        if not isitem(item):
            return False
        try:
            self._items.insert(index, item)
        except (IndexError, TypeError):
            return False
        return True

    def index(self, item, start=None, end=None):
        if start is None:
            start = 0
        if end is None:
            end = len(self)
        return self._items.index(item, start, end)
