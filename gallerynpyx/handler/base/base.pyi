from typing import AnyStr, Callable, Iterable, Union

from renpy.display.behavior import Button
from renpy.display.displayable import Displayable
from renpy.display.im import Image
from renpy.display.layout import Null
from renpy.display.transform import ATLTransform
from renpy.display.video import Movie

from ...config.base.resources import ResourcesConfig
from ...config.base.screens import ScreensConfig
from ...config.base.styles import StylesConfig
from ...resources.resource import Resource
from ...sizes.size_int import SizeInt
from ...slides.base import SlideBase
from ...slides.items import Item
from ...slides.slide import Slide
from ...slides.slider import Slider

__all__ = ("BaseHandler",)


class BaseHandler(object):
    """
    Core gallery handler with paging, routing and slide navigation support.
    """

    def __init__(self) -> None:
        """
        Creates the root slider and initializes the default page distribution.
        """
        ...

    @property
    def resources_config(self) -> ResourcesConfig:
        """
        Resource configuration bound to this handler.
        """
        ...

    @property
    def styles_config(self) -> StylesConfig:
        """
        Style configuration bound to this handler.
        """
        ...

    @property
    def screens_config(self) -> ScreensConfig:
        """
        Screen configuration bound to this handler.
        """
        ...

    @property
    def rows(self) -> int:
        """
        Number of rows rendered per page.
        """
        ...

    @rows.setter
    def rows(self, rows: int) -> None:
        """
        :param rows: New number of rows per page.
        """
        ...

    @property
    def cols(self) -> int:
        """
        Number of columns rendered per page.
        """
        ...

    @cols.setter
    def cols(self, cols: int) -> None:
        """
        :param cols: New number of columns per page.
        """
        ...

    @property
    def per_page(self) -> int:
        """
        Number of item slots available on each page.
        """
        ...

    @property
    def pages(self) -> int:
        """
        Total number of pages for the active slide.
        """
        ...

    @property
    def page(self) -> int:
        """
        Zero-based page index for the active slide.
        """
        ...

    @property
    def start(self) -> int:
        """
        Index of the first item displayed on the current page.
        """
        ...

    @property
    def end(self) -> int:
        """
        Index after the last slot displayed on the current page.
        """
        ...

    @property
    def items(self) -> Iterable[Item]:
        """
        Items shown by the active slide on the current page.
        """
        ...

    @property
    def available_items(self) -> int:
        """
        Number of real items shown on the current page.
        """
        ...

    @property
    def total(self) -> int:
        """
        Total number of items in the active slide.
        """
        ...

    @property
    def slides(self) -> Iterable[SlideBase]:
        """
        Child slides and sliders contained by the current slider.
        """
        ...

    @property
    def has_animation(self) -> bool:
        """
        Whether the active slide contains at least one animation item.
        """
        ...

    @property
    def slide(self) -> Slide | None:
        """
        Active slide for the current gallery route.
        """
        ...

    @property
    def root(self) -> Slider:
        """
        Root slider for the handler.
        """
        ...

    @property
    def current(self) -> Slider:
        """
        Current slider in the active route.
        """
        ...

    @property
    def thumbnail_size(self) -> SizeInt:
        """
        Thumbnail size derived from the current grid distribution.
        """
        ...

    @property
    def ibuttons(self) -> Iterable[Union[Button, Null]]:
        """
        Iterator with button displayables for the current page.
        """
        ...

    @property
    def buttons(self) -> tuple[Union[Button, Null], ...]:
        """
        Cached button displayables for the current page.
        """
        ...

    def change_distribution(self, rows: int | None = None, cols: int | None = None) -> None:
        """
        Updates the number of rows and columns used by each page.

        :param rows: Optional new number of rows.
        :param cols: Optional new number of columns.
        """
        ...

    def put_item(self,
                 names: Union[AnyStr, Iterable[AnyStr], SlideBase],
                 item: Item,
                 label: AnyStr | None = None,
                 thumbnail: Union[AnyStr, Resource, Displayable, ATLTransform, Image, Movie, None] = None) -> bool:
        """
        Adds an existing item to the given route.

        :param names: Route, route parts or slide container target.
        :param item: Item to add.
        :param label: Optional label used when creating the target slide.
        :param thumbnail: Optional custom thumbnail source.
        """
        ...

    def put(self,
            names: Union[AnyStr, Iterable[AnyStr], SlideBase],
            resource: Union[Resource, AnyStr, Movie, ATLTransform, Image, Displayable],
            song: AnyStr | None = None,
            condition: Callable[[Item], bool] | None = None,
            tooltip: AnyStr | None = None,
            locked_tooltip: AnyStr | None = None,
            label: AnyStr | None = None,
            thumbnail: Union[Resource, AnyStr, Movie, ATLTransform, Image, Displayable, None] = None) -> bool:
        """
        Creates an item and adds it to the given route.

        :param names: Route, route parts or slide container target.
        :param resource: Resource source assigned to the new item.
        :param song: Optional song path to play while the item is shown.
        :param condition: Optional callable used to determine whether the item is unlocked.
        :param tooltip: Optional tooltip shown when the item is available.
        :param locked_tooltip: Optional tooltip shown when the item is locked.
        :param label: Optional label used when creating the target slide.
        :param thumbnail: Optional custom thumbnail source.
        """
        ...

    def change(self, name: AnyStr | None, *names: AnyStr) -> None:
        """
        Changes the active route, slide or slider.

        :param name: First route segment, or ``None`` to return to the root.
        :param names: Additional route segments.
        """
        ...

    def to_first(self) -> None:
        """
        Moves the current slider to its first available slide.
        """
        ...

    def next(self) -> bool:
        """
        Advances the page in the active slide.
        """
        ...

    def previous(self) -> bool:
        """
        Goes back one page in the active slide.
        """
        ...

    def reset(self) -> None:
        """
        Clears cached state and returns the handler to the root route.
        """
        ...
