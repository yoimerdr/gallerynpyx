from typing import Any
from .base import Interactive


class ChangeAnimationSpeed(Interactive):
    """
    An action to change the animation speed.
    """

    def __init__(self: Any, speed: int):
        """
        :param speed: The speed to change to.
        """
        ...

    def get_sensitive(self: Any):
        """
        Method used internally by renpy
        """
        ...

    def get_selected(self: Any):
        """
        Method used internally by renpy
        """
        ...

    def __call__(self: Any, *args, **kwargs):
        ...
