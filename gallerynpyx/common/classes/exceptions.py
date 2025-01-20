from .helpers import classname

__all__ = (
    'NotSubclassOfError', 'NotExtensibleError',
    'NotInstantiableError', 'NotInstanceOfError'
)


class NotSubclassOfError(TypeError):
    def __init__(self, cls, base):
        super(NotSubclassOfError, self).__init__("{!r} is not a subclass of {!r}".format(
            classname(cls), classname(base)
        ))


class NotInstanceOfError(TypeError):
    def __init__(self, obj, base):
        super(NotInstanceOfError, self).__init__("{!r} is not an instance of {!r}".format(
            obj, classname(base)
        ))


class NotInstantiableError(TypeError):

    def __init__(self, cls):
        super(NotInstantiableError, self).__init__("The class {!r} is not instantiable.".format(
            classname(cls)
        ))


class NotExtensibleError(TypeError):
    def __init__(self, cls):
        super(NotExtensibleError, self).__init__("The class {!r} is not extensible.".format(
            classname(cls)
        ))
