from typing import Union, Any, AnyStr, Iterable

from renpy.display.transform import ATLTransform
from .resource import Resource


class AnimationResource(Resource):
    """
    The class for animations resources, whether named or the object itself.
    """
    def __init__(self: Any, source: Union[AnyStr, ATLTransform, AnimationResource]):
        """
        :param source: The animation's name, the animation itself or an animation resource.
        """
        ...

    @property
    def source(self: Any) -> Union[AnyStr, ATLTransform]:
        """
        The animation source (name or animation object).

        :getter: Gets the source.
        :setter: Sets a new source.
        """
        ...

    @source.setter
    def source(self: Any, value: Union[AnyStr, ATLTransform, AnimationResource]): ...


    def displayable(self: Any, size: Iterable[int] = None, ) -> ATLTransform:
        """
        Loads (force flag) the animation and returns it.

        :notes: Sets the size parameter to the animation state if it is provided.
        :param size: Optional iterable object with width and height dimensions.
        """
        ...

    def load(self: Any, force: bool = False) -> ATLTransform:
        """
        Loads the source.

        :raises UnsupportedSourceError: If the object retrieved from the name is not an animation.
        :raises UnloadableSourceError: If the object retrieved from the name is None and you force the load.

        :param force: Whether to force the load.
        :return: The loaded animation object.
        """
        ...