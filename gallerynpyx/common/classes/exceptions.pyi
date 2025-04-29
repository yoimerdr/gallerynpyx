from typing import Any


class NotSubclassOfError(TypeError):
    """
    A class is not a subclass of another class.
    """
    def __init__(self: Any, cls: type, base: type):
        """
        :param cls: The target class.
        :param base: The base class.
        """
        ...


class NotInstanceOfError(TypeError):
    """
    An object is not an instance of a class.
    """
    def __init__(self: Any, obj: Any, base: type):
        """
        :param obj: The instance object.
        :param base: The base class.
        """
        ...


class NotInstantiableError(TypeError):
    """
    A class is not instantiable.
    """
    def __init__(self: Any, cls: type):
        """
        :param cls: The not instantiable class.
        """
        ...


class NotExtensibleError(TypeError):
    """
    A class is not extensible.
    """
    def __init__(self: Any, cls: type):
        """
        :param cls: The not extensible class.
        """
        ...
