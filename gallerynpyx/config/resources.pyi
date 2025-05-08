from typing import Any, Union, AnyStr, SupportsInt

from renpy.display.displayable import Displayable
from renpy.display.im import Image
from ..common.classes.objects import SingletonRegistry
from ..resources.displayable import DisplayableResource
from ..resources.thumbnail import Thumbnail


class ResourcesConfig(SingletonRegistry):
    """
    Common configuration for resource-related properties.

    :notes:
        * There will be only one instance
        * You can register a custom configuration by using the ``register`` class method before the first use of the class.
    """

    def __init__(self: Any):
        ...

    @classmethod
    def register(cls: Any, target: type[ResourcesConfig]):
        """
        Registers a target class in the registry.

        :param target: The class to register.
        """
        ...

    @classmethod
    def get_instance(cls: Any, *args, **kwargs) -> ResourcesConfig:
        """
        Creates or returns the singleton instance.

        :param args: Init class arguments.
        :param kwargs: Init class keyword arguments.
        """
        ...

    @property
    def not_found(self: Any) -> Thumbnail:
        """
        Thumbnail for not found resources.

        :getter: Gets the thumbnail for not found.
        :setter: Sets a new resource for the not found thumbnail.
        """
        ...

    @not_found.setter
    def not_found(self: Any, value: Union[AnyStr, DisplayableResource, Displayable, Image]):
        ...

    @property
    def idle(self: Any) -> Thumbnail:
        """
        Thumbnail for idle status in resources.

        :getter: Gets the thumbnail for idle.
        :setter: Sets a new resource for the idle thumbnail.
        """
        ...

    @idle.setter
    def idle(self: Any, value: Union[AnyStr, DisplayableResource, Displayable, Image]):
        ...

    @property
    def play_hover(self: Any) -> Thumbnail:
        """
        Thumbnail for hover status in playable resources.

        :getter: Gets the thumbnail for idle.
        :setter: Sets a new resource for the idle thumbnail.
        """
        ...

    @play_hover.setter
    def play_hover(self: Any, value: Union[AnyStr, DisplayableResource, Displayable, Image]):
        ...

    @property
    def play_idle(self: Any) -> Thumbnail:
        """
        Thumbnail for hover status in playable resources.

        :getter: Gets the thumbnail for idle.
        :setter: Sets a new resource for the idle thumbnail.
        """
        ...

    @play_idle.setter
    def play_idle(self: Any, value: Union[AnyStr, DisplayableResource, Displayable, Image]):
        ...

    @property
    def locked(self: Any) -> Thumbnail:
        """
        Thumbnail for locked resources.

        :getter: Gets the thumbnail for idle.
        :setter: Sets a new resource for the idle thumbnail.
        """
        ...

    @locked.setter
    def locked(self: Any, value: Union[AnyStr, DisplayableResource, Displayable, Image]):
        ...

    @property
    def video_thumbnails_folder(self: Any) -> str:
        """
        The folder where video thumbnails are stored.

        :getter: Gets the folder path.
        :setter: Sets a new folder path.
        """
        ...

    @video_thumbnails_folder.setter
    def video_thumbnails_folder(self: Any, value: AnyStr):
        ...

    @property
    def allow_animation_thumbnail(self: Any) -> bool:
        """
        Whether to allow the search of an image for a thumbnail in animation objects

        :getter: Gets the value.
        :setter: Sets a new value.
        """
        ...

    @allow_animation_thumbnail.setter
    def allow_animation_thumbnail(self: Any, value):
        ...

    @property
    def allow_animation_speeds(self: Any):
        """
        Whether to allow the dynamic changes of speeds in animation objects.

        :getter: Gets the value.
        :setter: Sets a new value.
        """
        ...

    @allow_animation_speeds.setter
    def allow_animation_speeds(self: Any, value) -> bool:
        ...

    @property
    def animation_speed(self: Any) -> int:
        """
        The animation speed for animation objects.

        :getter: Gets the current speed.
        :setter: Sets a new speed.
        """
        ...

    @animation_speed.setter
    def animation_speed(self: Any, value: SupportsInt):
        ...

    @property
    def allow_animation_size(self: Any) -> bool:
        """
        Whether to allow the dynamic changes of size in animation objects.

        :getter: Gets the value.
        :setter: Sets a new value.
        """
        ...

    @allow_animation_size.setter
    def allow_animation_size(self: Any, value):
        ...

    @property
    def transition(self: Any) -> Any:
        """
        Transition for show resources.

        :getter: Gets the current transition.
        :setter: Sets a new transition.
        """
        ...

    @transition.setter
    def transition(self: Any, value):
        ...
