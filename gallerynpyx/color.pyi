from typing import AnyStr, Union, SupportsIndex


def ishex(color: AnyStr, alpha: bool = False) -> bool:
    """
    Checks if the given string is a valid hexadecimal color code.

    :param color: A string value.
    :param alpha: Whether to allow alpha values.
    """
    ...


def normhex(color: AnyStr, alpha: bool = False) -> Union[None, str]:
    """
    Normalizes a hexadecimal color value to standard format.

    :notes: If the given string is not a valid hexadecimal color value, returns None.
    :param color: A string value.
    :param alpha: Whether to allow alpha values.
    """
    ...


def rgba2hex(red: SupportsIndex, green: SupportsIndex,
             blue: SupportsIndex, alpha: SupportsIndex = None) -> Union[None, str]:
    """
    Converts RGBA color values to hexadecimal color string.

    :notes:
        * If the alpha value is not given, use 1.
        * If the conversion raises an exception (``TypeError``, ``ValueError``), returns None.
    :param red: Red component value (0-255)
    :param green: Green component value (0-255)
    :param blue: Blue component value (0-255)
    :param alpha: Alpha component value (0-1)
    """
    ...


def rgb2hex(red: SupportsIndex, green: SupportsIndex, blue: SupportsIndex) -> Union[None, str]:
    """
    Converts RGB color values to hexadecimal color code.

    :notes: If the conversion raises an exception (``TypeError``, ``ValueError``), returns None.
    :param red: Red component value (0-255)
    :param green: Green component value (0-255)
    :param blue: Blue component value (0-255)
    """
    ...


def hex2rgba(color: AnyStr) -> Union[None, tuple[int, int, int, int]]:
    """
    Converts a hexadecimal color string to RGBA values.

    :notes:
        * If the given string is not a valid hexadecimal color value, returns None.
        * If the conversion raises an exception (``TypeError``, ``ValueError``), returns None.
    :param color: The hexadecimal color string.
    """
    ...


def hex2rgb(color: AnyStr) -> Union[None, tuple[int, int, int]]:
    """
    Converts a hexadecimal color string to RGB values.

    :notes:
        * If the given string is not a valid hexadecimal color value, returns None.
        * If the conversion raises an exception (``TypeError``, ``ValueError``), returns None.
    :param color: The hexadecimal color string.
    """
    ...
