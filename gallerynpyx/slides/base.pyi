from typing import Any, AnyStr, Union, Iterable, Container

from .slider import Slider
from ..common.classes.objects import AbstractClass


def isslider(value) -> bool:
    """
    Checks if value is a ``Slider``.

    :param value: The object to check.
    """
    ...


def isslide(value) -> bool:
    """
    Checks if value is a ``Slide``.

    :param value: The object to check.
    """
    ...


def route(source: Union[AnyStr, Iterable[AnyStr], SlideBase], relative=None) -> tuple[AnyStr, ...]:
    """
    Creates a route from the source.

    :notes:
        * Only the defined values are converted to strings.
        * If the source is a ``SlideBase``, use the ``route`` method.
        * The ``relative`` parameter is ignored if the source is not a ``SlideBase``.

    :param source: The source object.
    :param relative: The slider to which the route will be relative to.
    """
    ...


class SlideBase(AbstractClass, Iterable, Container):
    """
    Base class for slides and sliders.
    """
    def __init__(self: Any, name: AnyStr, parent: Slider = None, label: AnyStr = None):
        """
        :param name: The unique name.
        :param parent: The slider parent.
        :param label: A label text.
        """
        ...

    @property
    def name(self: Any) -> str:
        """
        The unique name.

        :getter: Gets the name.
        """
        ...

    @property
    def parent(self: Any) -> Union[Slider, None]:
        """
        The slider parent.

        :getter: Gets the slider parent or None if it is not set.
        :setter: Sets the slider parent.
        """
        ...

    @parent.setter
    def parent(self: Any, value: Union[Slider, None]):
        ...

    @property
    def label(self: Any) -> str:
        """
        The label text.

        :getter: Gets the label text or capitalizes the name if it is not set.
        :setter: Sets the label text.
        """
        ...

    @label.setter
    def label(self: Any, value: Union[AnyStr, None]):
        ...

    @property
    def has_parent(self: Any) -> bool:
        """
        Checks if the ``parent`` is not None.

        """
        ...

    @property
    def root_parent(self: Any) -> Union[Slider, None]:
        """
        The root slider parent.

        :getter: Iterates over the parents and returns the last one.
        """
        ...

    @property
    def parents(self: Any) -> Iterable[Slider]:
        """
        The slider parents.

        :getter: Returns an iterable of slider parents.
        """
        ...

    def route(self: Any, relative: Slider = None) -> tuple[str, ...]:
        """
        Creates a route for the current instance.

        :notes: If relative is None, the route will be relative to the root slider.
        :param relative: The slider to which the route will be relative to.
        """
        ...

    def add(self: Any, item) -> bool:
        """
        Adds an item.

        :param item: The item to add.
        :return: True if the item was added, False otherwise.
        """
        ...

    def remove(self: Any, item) -> bool:
        """
        Removes an item.

        :param item: The item to remove.
        :return: True if the item was removed, False otherwise.
        """
        ...

    def get(self: Any, item) -> Any:
        """
        Gets an item.

        :param item: The identifier of the item.
        :return: The item or None if it was not found.
        """
        ...

    def set(self: Any, key, item) -> bool:
        """
        Sets an item.

        :param key: The item identifier.
        :param item: The item to set.
        :return: True if the item was set, False otherwise.
        """
        ...

    def clear(self: Any):
        """
        Clears the items.
        """
        ...

    def removeself(self: Any) -> bool:
        """
        Removes the current instance from its parent.

        :return: True if was removed, False otherwise.
        """
        ...

    def __str__(self: Any) -> str:
        ...

    def __hash__(self: Any) -> int:
        ...

    def __iter__(self: Any) -> Iterable:
        ...

    def __len__(self: Any) -> int:
        ...

    def __contains__(self: Any, item) -> bool:
        ...

    def __getitem__(self: Any, item) -> Any:
        ...

    def __setitem__(self: Any, key, value) -> bool:
        ...

    def __delitem__(self: Any, key) -> bool:
        ...

    def __repr__(self: Any) -> str:
        ...
