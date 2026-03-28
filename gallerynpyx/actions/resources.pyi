from typing import Any

from .base import Interactive
from ..config.base.resources import ResourcesConfig


class ChangeAnimationSpeed(Interactive):
    """
    An action to change the animation speed.
    """

    def __init__(self: Any,
                 speed: int,
                 resources_config: str | ResourcesConfig | None = None) -> None:
        """
        :param speed: The speed to change to.
        :param resources_config: Optional resources configuration or gallery name.
        """
        ...

    def get_sensitive(self: Any) -> bool:
        """
        Method used internally by renpy
        """
        ...

    def get_selected(self: Any) -> bool:
        """
        Method used internally by renpy
        """
        ...

    def __call__(self: Any, *args, **kwargs) -> None:
        """
        :param args: Positional arguments forwarded by Ren'Py.
        :param kwargs: Keyword arguments forwarded by Ren'Py.
        """
        ...
