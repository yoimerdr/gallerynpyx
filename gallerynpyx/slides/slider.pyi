from typing import Any, Iterable, AnyStr, Union

from .base import SlideBase
from .slide import Slide

__all__ = ('Slider',)


class Slider(SlideBase):
    """
    A dictionary-like of ``Slide`` or ``Slider``.
    """

    @classmethod
    def chain(cls, key: Union[AnyStr, Iterable[AnyStr], SlideBase], source: Slider = None, creates: bool = False) -> \
    Union[Slider, None]:
        """
        Iterates over the route and returns the slider at the end.

        :notes: If any slider in the route does not exist and the ``creates`` flag is not specified, returns None.
        :notes: If any item in the route is not a slider and the ``creates`` flag is not specified, returns None.
        :raises NameAlreadyExistsError: If any item in the route is not a slider and the ``creates`` flag is specified.
        :param key: The slider routes.
        :param source: The slider source.
        :param creates: Whether to create the slider if it doesn't exist.
        """
        ...

    def remove(self: Any, item: Union[AnyStr, Iterable[AnyStr], SlideBase]) -> bool:
        """
        Removes a slide/slider at the specified route.

        :param item: The target route.
        :return: True if the target was removed, False otherwise.
        """
        ...

    def get(self: Any, item: Union[AnyStr, Iterable[AnyStr], SlideBase]) -> Union[SlideBase, None]:
        """
        Gets a slide/slider at the specified route.

        :param item: The target route.
        :return: The target slide/slider or None if it was not found.
        """
        ...

    def set(self: Any, key: Union[AnyStr, Iterable[AnyStr], SlideBase], item: SlideBase) -> bool:
        """
        Sets an slide/slider at the specified route.

        :param key: The target route.
        :param item: The slide/slider to set.
        :return: True if the item was set, False otherwise.
        """
        ...

    def add(self: Any, item: Union[AnyStr, SlideBase], routes: Union[AnyStr, Iterable[AnyStr], SlideBase] = None):
        """
        Adds an slide/slider.

        :param item: The slide/slider to add.
        :param routes: Optional parent route for the item.
        :return: True if the item was added, False otherwise.
        """
        ...

    def slider(self: Any, *routes: Union[AnyStr, SlideBase], label: AnyStr = None) -> Union[Slider, None]:
        """
        Creates a slider with this as its parent.

        :notes: If the routes are empty, will return None.
        :param routes: The slider route.
        :param label: The slider label text.
        """
        ...

    def slide(self: Any, *routes: Union[AnyStr, SlideBase], label: AnyStr = None) -> Union[Slide, None]:
        """
        Creates a slide with this as its parent.

        :notes: If the routes are empty, will return None.
        :param routes: The slide route.
        :param label: The slide label text.
        """
        ...

    def items(self: Any) -> Iterable[tuple[str, SlideBase]]:
        """
        Returns an iterable with (name, item) of each element in the slider.
        """
        ...

    def values(self: Any) -> Iterable[SlideBase]:
        """
        Returns an iterable with the items in the slider.
        """
        ...

    def names(self: Any) -> Iterable[str]:
        """
        Returns an iterable with the names of the items in the slider.
        """
        ...

    def __iter__(self: Any) -> Iterable[SlideBase]: ...

    def __contains__(self: Any, item: SlideBase) -> bool: ...

    def __getitem__(self: Any, item: Union[AnyStr, Iterable[AnyStr], SlideBase]) -> SlideBase: ...

    def __setitem__(self: Any, key: Union[AnyStr, Iterable[AnyStr], SlideBase], value: SlideBase) -> bool: ...

    def __delitem__(self: Any, key: AnyStr) -> bool: ...
