from typing import Iterable

from renpy.display.displayable import Displayable

from ...config.base.resources import ResourcesConfig
from ...sizes.size import Size
from ...slides.items import Item


def create_items_thumbnail(items: Iterable[Item],
                           size: Iterable | Size,
                           resources_config: str | ResourcesConfig | None = None) -> Iterable[tuple[Item, Displayable]]:
    """
    Resolves the thumbnails that should be rendered for the given items.

    :param items: Items whose thumbnails should be resolved.
    :param size: Target thumbnail size.
    :param resources_config: Optional resources configuration or gallery name.
    """
    ...


def create_items_overlay(items: Iterable[Item],
                         size: Iterable | Size,
                         resources_config: str | ResourcesConfig | None = None
                         ) -> Iterable[tuple[tuple[Item, Displayable], tuple[Displayable, Displayable | None, Displayable]]]:
    """
    Resolves thumbnails together with idle, hover and locked overlays.

    :param items: Items whose overlays should be resolved.
    :param size: Target thumbnail size.
    :param resources_config: Optional resources configuration or gallery name.
    """
    ...
