from ..helpers import isdefine


def classname(target, **kwargs):
    if not isinstance(target, type):
        target = type(target)
    name = target.__name__
    if not kwargs.get("fully", False):
        return name

    mod = target.__module__
    qualname = "{}.{}".format(mod, name) if mod != "__builtin__" else name

    return qualname


def representation(cls, **kwargs):
    return "{}({})".format(
        classname(cls),
        ", ".join(
            "{}={!r}".format(k, v)
            for k, v in kwargs.items() if isdefine(v)
        )
    )


def with_metaclass(cls, metaclass):
    return metaclass(cls.__name__, cls.__bases__, dict(cls.__dict__))


def add_metaclass(*args):
    if not args:
        raise ValueError("You must pass at least the metaclass.")

    metaclass = args[0]

    if len(args) > 1:
        return with_metaclass(metaclass, args[1])

    def wrapper(cls):
        return with_metaclass(cls, metaclass)

    return wrapper


def classof(cls):
    if not isinstance(cls, type):
        raise TypeError("The class {!r} is not a class.".format(cls))
    return getattr(cls, "__cls__", cls)


def not_instantiable(self, *args, **kwargs):
    from .exceptions import NotInstantiableError

    raise NotInstantiableError(self)


def not_implemented(self, *args, **kwargs):
    raise NotImplementedError("Method not implemented for {!r}".format(classname(self)))
