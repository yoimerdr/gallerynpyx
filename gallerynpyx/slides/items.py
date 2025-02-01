from ..common.classes.helpers import representation
from ..common.helpers import tostring
from ..path import isloadable
from ..resources.resource import AUDIO
from ..resources.thumbnail import Thumbnail

__all__ = ('Item', 'isitem')


def isitem(value): return isinstance(value, Item)


class Item(object):
    __slots__ = (
        '_res', '_song',
        '_cond', '_tip',
        '_thumb', '_lock_tip'
    )

    def __init__(self, resource, song=None, condition=None, tooltip=None, locked_tooltip=None):
        self._thumb = Thumbnail(resource)
        self._res = self._thumb.resource
        self.song = song
        self.condition = condition
        self.tooltip = tooltip
        self.locked_tooltip = locked_tooltip

    @property
    def resource(self):
        return self._res

    @property
    def thumbnail(self):
        return self._thumb

    @property
    def locked(self):
        return not eval(self.condition) if self.condition else False

    @property
    def song(self):
        return self._song

    @song.setter
    def song(self, song):
        self._song = song if song and isloadable(tostring(song), extensions=AUDIO) else None

    @property
    def condition(self):
        return self._cond

    @condition.setter
    def condition(self, condition):
        self._cond = tostring(condition) if condition else None

    @property
    def tooltip(self):
        return self._tip

    @tooltip.setter
    def tooltip(self, tooltip):
        self._tip = tostring(tooltip) if tooltip else None

    @property
    def locked_tooltip(self):
        return self._lock_tip

    @locked_tooltip.setter
    def locked_tooltip(self, tooltip):
        self._lock_tip = tostring(tooltip) if tooltip else None

    def __repr__(self):
        return representation(
            self,
            resource=self._res,
            song=self.song,
            condition=self.condition,
            tooltip=self.tooltip
        )

    def __hash__(self):
        return hash((self.resource,))
