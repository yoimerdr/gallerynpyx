from typing import Iterable, AnyStr

from renpy.display.transform import ATLTransform

SPEED_ATTRIBUTE: str
"""
The attribute name where the speed is stored.
"""

def is_pause_statement(statement) -> bool:
    """
    Checks if the value is an ATL pause statement.

    :param statement: The value to check.
    """
    ...


def get_statements(animation: ATLTransform, raw: bool = True) -> Iterable:
    """
    Returns an iterator with the statements of the animation.

    :param animation: The animation object
    :param raw: Whether to use the raw statements
    """
    ...


def set_speed(animation: ATLTransform, speed: int = None):
    """
    Sets the speed to the animation.

    :notes: This function modifies each ``raw pause statement``, assigning a new value to its ``duration`` according to the corresponding speed.
    :param animation: The animation object.
    :param speed: The speed to set.
    """
    ...


def get_images(animation: ATLTransform) -> Iterable[AnyStr]:
    """
    Returns an iterator with the image names (or filepaths) using in the animation.

    :notes: An image is considered to be any string used in an expression within an ATL block.
    :param animation: The animation object.
    """
    ...
