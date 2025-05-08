from typing import Any, SupportsInt, Iterable, Union, AnyStr, Callable

from renpy.display.behavior import Button
from renpy.display.displayable import Displayable
from renpy.display.im import Image
from renpy.display.layout import Null
from renpy.display.transform import ATLTransform
from renpy.display.video import Movie
from .common.classes.objects import SingletonRegistry
from .resources.resource import Resource
from .sizes.size_int import SizeInt
from .slides.base import SlideBase
from .slides.items import Item
from .slides.slide import Slide
from .slides.slider import Slider


class Handler(SingletonRegistry):
    """
    Basic handler for a gallery.

    :notes:
        * There will be only one instance
        * You can register a custom handler by using the ``register`` class method before the first use of the class.
    """

    def __init__(self: Any):
        ...

    @classmethod
    def register(cls: Any, target: type[Handler]):
        """
        Registers a target class in the registry.

        :param target: The class to register.
        """
        ...

    @classmethod
    def get_instance(cls: Any, *args, **kwargs) -> Handler:
        """
        Creates or returns the singleton instance.

        :param args: Init class arguments.
        :param kwargs: Init class keyword arguments.
        """
        ...

    @property
    def rows(self: Any) -> int:
        """
        Rows in a slide.

        :getter: Returns the number of rows
        :setter: Sets the number of rows
        """
        ...

    @rows.setter
    def rows(self: Any, rows: int):
        ...

    @property
    def cols(self: Any) -> int:
        """
        Columns in a slide.

        :getter: Returns the number of columns
        :setter: Sets the number of columns
        """
        ...

    @cols.setter
    def cols(self: Any, cols: int):
        ...

    @property
    def per_page(self: Any) -> int:
        """
        The number of items per page in a slide.
        """
        ...

    @property
    def pages(self: Any) -> int:
        """
        The number of pages in the active ``slide``.
        """
        ...

    @property
    def page(self: Any) -> int:
        """
        The number of page in the active ``slide``.
        """
        ...

    @property
    def start(self: Any) -> int:
        """
        The index of the first item in the active ``slide`` at ``page``.
        """
        ...

    @property
    def end(self: Any) -> int:
        """
        The index of the last item in the active ``slide`` at ``page``.
        """
        ...

    @property
    def items(self: Any) -> Iterable[Item]:
        """
        The items in the active ``slide`` at ``page``.
        """
        ...

    @property
    def available_items(self: Any) -> int:
        """
        The number of items in the active ``slide`` at ``page``.
        """
        ...

    @property
    def total(self: Any) -> int:
        """
        The total number of items in the active ``slide``.

        :notes: If the active slide is None, then it returns 0.
        """
        ...

    @property
    def slides(self: Any) -> Iterable[SlideBase]:
        """
        The slides (sliders) in the ``current`` slider.
        """
        ...

    @property
    def has_animation(self: Any) -> bool:
        """
        Whether any item in the active ``slide`` has an animation resource.
        """
        ...

    @property
    def slide(self: Any) -> Union[Slide, None]:
        """
        The active ``slide``.
        """
        ...

    @property
    def root(self: Any) -> Slider:
        """
        The root slider.
        """
        ...

    @property
    def current(self: Any) -> Slider:
        """
        The ``current`` slider.
        """
        ...

    @property
    def thumbnail_size(self: Any) -> SizeInt:
        """
        The thumbnail size.

        :notes:
            * This value is set on each change of the distribution.
            * You can set the size properties directly, but it's not recommended.
        :getter: Gets the thumbnail size
        """
        ...

    @property
    def ibuttons(self: Any) -> Iterable[Union[Button, Null]]:
        """
        An iterator of the buttons in the active ``slide``.

        :notes:
            * The order of the buttons is the same as the order of the items in the active ``slide``.
            * If the total number of items is not enough to fill the current page, then the remaining buttons are ``Null`` displayables.
        """
        ...

    @property
    def buttons(self: Any) -> tuple[Union[Button, Null], ...]:
        """
        A tuple of the buttons in the active ``slide``.

        :notes:
            * The order of the buttons is the same as the order of the items in the active ``slide``.
            * If the total number of items is not enough to fill the current page, then the remaining buttons are ``Null`` displayables.
        """
        ...

    def change_distribution(self: Any, rows: int = None, cols: int = None):
        """
        Changes the distribution of each page.

        :notes: This method updates the ``thumbnail_size`` property.
        :param rows: The number of rows
        :param cols: The number of columns
        """
        ...

    def put_item(self: Any, names: Union[AnyStr, Iterable[AnyStr], SlideBase], item: Item, label: AnyStr = None,
                 thumbnail: Union[AnyStr, Resource, Displayable, ATLTransform, Image, Movie] = None) -> bool:
        """
        Puts an item in the route.

        :param names: The route for the slide container.
        :param item: An ``Item`` instance.
        :param label: A label text (Only used when the target slide doesn't exist).
        :param thumbnail: Any valid source or a resource.
        :return: True if the item was added, False otherwise.
        """
        ...

    def put(self: Any, names: Union[AnyStr, Iterable[AnyStr], SlideBase],
            resource: Union[Resource, AnyStr, Movie, ATLTransform, Image, Displayable], song: AnyStr = None,
            condition: Callable[[Item], bool] = None, tooltip: AnyStr = None, locked_tooltip: AnyStr = None,
            label: AnyStr = None,
            thumbnail: Union[Resource, AnyStr, Movie, ATLTransform, Image, Displayable] = None) -> bool:
        """
        Creates an item and puts it in the route.

        :param names: The route for the slide container.
        :param resource: Any valid source or a resource.
        :param song: A filepath for a song.
        :param condition: A callable to evaluate.
        :param tooltip: A text for a tooltip.
        :param locked_tooltip: A text for a tooltip.
        :param label: A label text (Only used when the target slide doesn't exist).
        :param thumbnail: Any valid source or a resource.
        :return: True if the item was added, False otherwise.
        """

        ...

    def change(self: Any, name: AnyStr, *names: AnyStr):
        """
        Changes the active slide.

        :notes: If the target slide is a slider, then use the ``to_first`` method.
        :param name: The first part of the route.
        :param names: The other parts of the route.
        """
        ...

    def to_first(self: Any):
        """
        Changes the active slide to the first slide in the current slider.
        """
        ...

    def next(self: Any) -> bool:
        """
        Changes the active ``page`` in the active ``slide``.

        :return: True if the page changed, False otherwise.
        """
        ...

    def previous(self: Any) -> bool:
        """
        Changes the active ``page`` in the active ``slide``.

        :return: True if the page changed, False otherwise.
        """
        ...

    def reset(self: Any):
        """
        Resets the handler to its initial state.
        """
        ...
