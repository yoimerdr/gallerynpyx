from typing import AnyStr

sep: str
"""
The path separator for renpy.
"""

def isloadable(path: AnyStr, normalized: bool = False, extensions: tuple[AnyStr, ...] = None):
    """
    Checks if the path is loadable.

    :param path: The path to check.
    :param normalized: Whether the path is already normalized.
    :param extensions: The valid extensions for the path.
    :see: `loadable <https://www.renpy.org/doc/html/file_python.html#renpy.loadable>`_
    """
    ...


def normpath(path: AnyStr):
    """
    Normalizes the path for renpy.

    :param path: The path to normalize.
    """
    ...


def join(path: AnyStr, *paths: AnyStr):
    """
    Joins the given paths.

    :notes: The joining is made using the ``join`` method of ``sep``
    :param path: The first path.
    :param paths: Other paths.
    """
    ...
