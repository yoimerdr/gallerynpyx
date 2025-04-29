from typing import Union, override, Any, Iterable


class Size(Iterable[float]):
    """
    Class for store width and height dimensions (floats).
    """

    def __init__(self: Any, width: Union[float, int] = 0, height: Union[float, int] = 0): ...

    @property
    def width(self: Any) -> float:
        """
        The width dimension.

        :notes: The value will be greater than or equal to zero

        :getter: Returns the width dimension.
        :setter: Sets the width dimension.
        """
        ...

    @width.setter
    def width(self: Any, value: Union[float, int]): ...

    @property
    def height(self: Any) -> float:
        """
        The height dimension.

        :notes: The value will be greater than or equal to zero

        :getter: Returns the height dimension.
        :setter: Sets the height dimension.
        """
        ...

    @height.setter
    def height(self: Any, value: Union[float, int]): ...

    @property
    def aspect_ratio(self: Any) -> float:
        """
        Gets the aspect ratio **(width / height)** of the size.
        """
        ...

    @property
    def is_empty(self: Any) -> bool:
        """
        Checks if the size is empty (width and height are both zero).
        """
        ...

    def set(self: Any, unpackable: Iterable[float]):
        """
        Sets the dimensions from an unpackable object.

        :param unpackable: An iterable object with width and height dimensions.
        """
        ...

    @classmethod
    def of(cls: Any, unpackable: Iterable[float]) -> Size:
        """
        Creates a size from an unpackable object.

        :param unpackable: An iterable object with width and height dimensions.
        """
        ...

    def scale(self: Any, ratio: Union[float, int, Iterable]) -> Size:
        """
        Scales the size by the given ratio.

        :param ratio: The aspect ratio value or an unpackable object with width and height dimensions.
        :return: The new scaled size.
        """
        ...

    def __iter__(self: Any) -> Iterable[float]: ...

    def __getitem__(self: Any, item: int) -> float: ...

    @override
    def __getitem__(self: Any, item: slice) -> tuple: ...

    def __eq__(self: Any, other: Iterable[float]): ...
