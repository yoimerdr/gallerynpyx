from typing import Any

from renpy.display.transform import ATLTransform
from renpy.ui import Action

from ..config.base.resources import ResourcesConfig
from ..config.base.screens import ScreensConfig
from ..resources.resource import Resource
from ..slides.items import Item


def prepare_resource(resource: Resource,
                     resources_config: str | ResourcesConfig | None = None) -> Any:
    """
    Prepares the resource for display.

    :param resource: Any resource.
    :param resources_config: Optional resources configuration or gallery name.
    """
    ...


def reset_resource(resource: Resource,
                   resources_config: str | ResourcesConfig | None = None) -> None:
    """
    Resets any temporary animation state applied during display.

    :param resource: Resource to reset.
    :param resources_config: Optional resources configuration or gallery name.
    """
    ...


class ShowItem(Action):
    """
    An action to display the resource of an item.
    """

    def __init__(self: Any,
                 item: Item,
                 resources_config: str | ResourcesConfig | None = None,
                 screens_config: str | ScreensConfig | None = None) -> None:
        """
        :param item: The item instance.
        :param resources_config: Optional resources configuration or gallery name.
        :param screens_config: Optional screens configuration or gallery name.
        """
        ...

    @classmethod
    def register(cls, target: type[ShowItem]) -> None:
        """
        Registers the subclass that should be instantiated for this action.

        :param target: Class that inherits from ``ShowItem`` and should replace it when instantiated.
        """
        ...

    def get_selected(self: Any) -> bool:
        """
        Method used internally by renpy
        """
        ...

    def get_tooltip(self: Any) -> str | None:
        """
        Method used internally by renpy
        """
        ...

    def show(self: Any) -> None:
        """
        Shows the resource of the item.
        """
        ...

    def __call__(self: Any, *args, **kwargs) -> None:
        """
        :param args: Positional arguments forwarded by Ren'Py.
        :param kwargs: Keyword arguments forwarded by Ren'Py.
        """
        ...
