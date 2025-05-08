from typing import override, Any, Callable


def classname(target, *, fully: bool = False) -> str:
    """
    Gets the class name of the target object.

    :param target: An instance or a class.
    :param fully: Whether to return the fully qualified name.
    """
    ...


def representation(target, **kwargs: Any) -> str:
    """
    Creates a representation of the target object.

    :param target: An instance.
    :param kwargs: The arguments into the representation.
    """
    ...


def with_metaclass(cls: type, metaclass: type) -> type:
    """
    Creates a type with the given metaclass.

    :param cls: The class to create a type from.
    :param metaclass: The metaclass to use.
    """
    ...


def add_metaclass(metaclass: type) -> Callable[[type], type]:
    """
    Adds a metaclass to a class.

    :param metaclass: The metaclass to add.
    """
    ...


def classof(cls: type) -> type:
    """
    Gets the active class.

    :notes: The active class is the ``__cls__`` class attribute.
    :param cls: A class type
    :returns: The active class or itself if it doesn't have one.
    """
    ...


@override
def add_metaclass(cls: type, metaclass: type) -> type:
    """
    Creates a type with the given metaclass.

    :param cls: The class to create a type from.
    :param metaclass: The metaclass to use.
    """
    ...


def not_instantiable(self, *args, **kwargs):
    """
    :raises NotInstantiableError: When the function is called.
    :param self: The self-instance.
    :param args: Method arguments.
    :param kwargs: Method keyword arguments.
    """
    ...


def not_implemented(self, *args, **kwargs):
    """
    :raises NotImplementedError: When the function is called.
    :param self: The self-instance.
    :param args: Method arguments.
    :param kwargs: Method keyword arguments.
    :return:
    """
    ...
