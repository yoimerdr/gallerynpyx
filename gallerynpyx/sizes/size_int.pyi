from typing import Any, Union, Iterable

from .size import Size


class SizeInt(Size):
    """
    Class for store width and height dimensions (integers).
    """

    @property
    def width(self: Any) -> int: ...

    @property
    def height(self: Any) -> int: ...

    def scale(self: Any, ratio: Union[float, int, Iterable[int], Iterable[float]]) -> SizeInt:
        ...

    @classmethod
    def of(cls: Any, unpackable: Union[Iterable, Iterable[int], Iterable[float]]) -> SizeInt: ...

    def __iter__(self: Any) -> Iterable[int]: ...

    def __getitem__(self: Any, item: int) -> int: ...
