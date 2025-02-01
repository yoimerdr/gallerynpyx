from ..common.classes.helpers import classname

__all__ = (
    'UnsupportedSourceError',
    'IncompatibleResourceError',
    'UnloadableSourceError'
)

class UnsupportedSourceError(ValueError):
    def __init__(self, source, target=None):
        message = "The source {!r} is not supported".format(source)
        message += " for a {!r}".format(classname(target)) if target else "."
        super(UnsupportedSourceError, self).__init__(message)


class IncompatibleResourceError(ValueError):
    def __init__(self, resource, target=None):
        message = "{!r} is not compatible".format(classname(resource))
        message += " with {!r}".format(classname(target)) if target else "."
        super(IncompatibleResourceError, self).__init__(message)


class UnloadableSourceError(ValueError):
    def __init__(self, source):
        super(UnloadableSourceError, self).__init__("The source {!r} is not loadable.".format(source))