from .size import Size

__all__ = ('SizeInt',)

class SizeInt(Size):
    __slots__ = ()

    def _assign_measure(self, value, name):
        return int(super(SizeInt, self)._assign_measure(value, name))

    def scale(self, ratio):
        return SizeInt.of(super(SizeInt, self).scale(ratio))