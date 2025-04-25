class Memoized(object):
    __slots__ = (
        '_res', '_fn',
        '_val',
    )

    def __init__(self, builder):
        self._fn = builder
        self._val = None

    def dispose(self):
        self._val = None
        try:
            delattr(self, '_res')
        except AttributeError:
            pass

    def evaluate(self, *args):
        if self._val != args or not hasattr(self, '_res'):
            self._val = args
            setattr(self, '_res', self._fn(*args))

        return self._res

    def __call__(self, *args):
        return self.evaluate(*args)
