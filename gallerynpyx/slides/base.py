from .exceptions import NameAlreadyExistsError
from ..common.classes.helpers import not_implemented, representation
from ..common.classes.objects import AbstractClass
from ..common.compat import basestring
from ..common.exceptions import AssignmentError
from ..common.helpers import tostring, isdefine
from ..common.iters import imap, ifilter

__all__ = ('isslider', 'isslide', 'SlideBase')


def isslider(value):
    from .slider import Slider
    return isinstance(value, Slider)


def isslide(value):
    from .slide import Slide
    return isinstance(value, Slide)


def route(source, relative=None):
    if isinstance(source, SlideBase):
        return source.route(relative)
    elif isinstance(source, basestring):
        return (source,)
    try:
        return tuple(imap(tostring, ifilter(isdefine, source)))
    except TypeError:
        return (tostring(source),)


class SlideBase(AbstractClass):
    __slots__ = (
        '_items', '_parent',
        '_name', '_label'
    )

    def __init__(self, name, parent=None, label=None):
        self._name = tostring(name)
        self.label = label
        self._parent = self._items = None
        self.parent = parent

    @property
    def name(self):
        return self._name

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        if value is None:
            self.removeself()
            self._parent = None
            return

        if not isslider(value) or self.parent is value:
            return

        if self is value:
            raise AssignmentError("Cannot assign parent as itself.")
        if self in value:
            raise NameAlreadyExistsError(self.name, value)

        self.removeself()
        self._parent = value
        value.add(self)

    @property
    def label(self):
        return self._label or self.name.capitalize()

    @label.setter
    def label(self, value):
        self._label = tostring(value)

    @property
    def has_parent(self):
        return isdefine(self.parent)

    @property
    def root_parent(self):
        if not self.has_parent:
            return None
        parent = self.parent
        while parent.has_parent:
            parent = parent.parent
        return parent

    @property
    def parents(self):
        source = self
        while source.has_parent:
            source = source.parent
            yield source

    def route(self, relative=None):
        names = [self.name]
        for parent in self.parents:
            if parent is relative:
                break
            names.append(parent.name)
        names = tuple(reversed(names))
        return names[1:] if relative is None else names

    def add(self, item):
        return self._add(item)

    def remove(self, item):
        return self._remove(item)

    def get(self, item):
        return self._get(item)

    def set(self, key, item):
        return self._set(key, item)

    def clear(self):
        return self._clear()

    def removeself(self):
        return self.parent.remove(self.name) if self.has_parent else False

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __iter__(self):
        return iter(self._items if isdefine(self._items) else ())

    def __len__(self):
        return len(self._items) if isdefine(self._items) else 0

    def __contains__(self, item):
        return self._items and item in self._items

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __delitem__(self, key):
        return self.remove(key)

    def __repr__(self):
        name, label = self.name, self.label
        return representation(
            self,
            name=name,
            parent=self.parent,
            label=None if label == name.capitalize() else label,
        )

    _add = _set = _get = _remove = _clear = not_implemented
