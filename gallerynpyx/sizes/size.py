from ..common.classes.helpers import representation
from ..common.exceptions import AssignmentError

__all__ = ('Size',)


class Size(object):
    __slots__ = (
        '_wt', '_ht'
    )

    def __init__(self, width=0, height=0):
        self._wt = width
        self.width = width
        self.height = height

    def _assign_measure(self, value, name):
        if value is None:
            raise AssignmentError("{} cannot be None.".format(name))
        return max(float(value), 0.0)

    @property
    def width(self):
        return self._wt

    @width.setter
    def width(self, value):
        self._wt = self._assign_measure(value, "width")

    @property
    def height(self):
        return self._ht

    @height.setter
    def height(self, value):
        self._ht = self._assign_measure(value, "height")

    @property
    def aspect_ratio(self):
        if self.height == 0:
            return 0.0
        return self.width / float(self.height)

    @property
    def is_empty(self):
        return self.width == 0 and self.height == 0

    def set(self, unpackable):
        self.width, self.height = unpackable

    def scale(self, ratio):
        if not isinstance(ratio, (int, float)):
            ratio = Size.of(ratio).aspect_ratio

        width, height = self.width, self.height
        current_ratio = self.aspect_ratio
        if current_ratio < ratio:
            height = width / ratio
        else:
            width = height * ratio
        return Size(width, height)

    @classmethod
    def of(cls, unpackable):
        w, h = unpackable
        return cls(w, h)

    def __iter__(self):
        return iter((self.width, self.height))

    def __getitem__(self, item):
        return (self.width, self.height)[item]

    def __eq__(self, other):
        w, h = other
        return self.width == w and self.height == h

    def __repr__(self):
        return representation(
            self,
            width=self.width,
            height=self.height
        )
