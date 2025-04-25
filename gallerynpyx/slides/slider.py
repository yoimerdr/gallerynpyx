from collections import OrderedDict

from .exceptions import NameAlreadyExistsError
from .base import SlideBase, route, isslider
from .slide import Slide
from ..common.helpers import isdefine

__all__ = ('Slider',)



class Slider(SlideBase):
    __slots__ = ()

    def __init__(self, name, parent=None, label=None):
        super(Slider, self).__init__(name, parent, label)
        self._items = OrderedDict()

    @classmethod
    def chain(cls, key, source=None, creates=False):
        target = None
        routes = route(key)

        if not routes:
            return None

        size = len(routes)
        for index, name in enumerate(routes, start=1):
            if creates and source is None:
                target = source = cls(name)
                continue

            target = source._items.get(name, None)
            if target is None:
                if not creates:
                    return None
                target = cls(name, parent=source)
            elif not isslider(target):
                if creates:
                    raise NameAlreadyExistsError(name, source)
                elif index < size:
                    return None
            source = target
        return target

    def _add(self, slide, routes=None):
        if not isinstance(slide, SlideBase):
            return False

        items = self._items
        name = slide.name
        source = self

        if routes:
            source = self.chain(routes, self, True)
            source = self if source is None else source
            items = source.items

        current = items.get(name, None)
        if isdefine(current):
            return False
        elif slide.parent is not source:
            slide.parent = source

        items[name] = slide
        return True

    def _get(self, key):
        return self.chain(key, self, False)

    def _set(self, key, value):
        if not isinstance(value, SlideBase):
            return False

        target = self.chain(key, self, False)
        if target is None:
            return False
        elif value is target:
            return True

        parent = target.parent
        target.removeself()
        return parent.add(value)

    def _remove(self, key):
        target = self.get(key)
        if target is None:
            return False

        target.parent._items.pop(target.name)
        target.parent = None
        return True

    def _clear(self):
        for _, value in self.items():
            value.removeself()

    def add(self, item, routes=None):
        return self._add(item, routes)

    def slider(self, *routes, **kwargs):
        slider = self.chain(routes, self, True)
        slider.label = kwargs.get("label", None)
        return slider

    def slide(self, *routes, **kwargs):
        routes = route(routes)
        label = kwargs.get("label", None)
        if not routes:
            return None
        if len(routes) == 1:
            return Slide(routes[0], self, label)

        parent, name = routes[:-1], routes[-1]

        parent = self.slider(*parent)
        return Slide(name, parent, label)

    def items(self):
        source = self._items
        return ((k, source[k]) for k in source)

    def values(self):
        return (v for _, v in self.items())

    def names(self):
        return (k for k in self._items)

    def __contains__(self, item):
        return isdefine(item) and item == self._items.get(item.name, None)
