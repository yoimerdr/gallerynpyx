from typing import Any, AnyStr, SupportsInt, Union

from renpy.display.displayable import Displayable
from renpy.display.im import Image

from ...resources.displayable import DisplayableResource
from ...resources.thumbnail import Thumbnail
from .base import BaseConfig

__all__ = ("ResourcesConfig",)


class ResourcesConfig(BaseConfig):
    """
    Resource configuration shared by the global gallery and named local galleries.
    """

    def __init__(self) -> None:
        """
        Creates the default gallery resources configuration.
        """
        ...

    @property
    def not_found(self) -> Thumbnail:
        """
        Thumbnail used when a resource thumbnail cannot be resolved.
        """
        ...

    @not_found.setter
    def not_found(self, value: Union[AnyStr, DisplayableResource, Displayable, Image]) -> None:
        """
        :param value: New fallback thumbnail source.
        """
        ...

    @property
    def idle(self) -> Thumbnail:
        """
        Thumbnail overlay used by idle resources.
        """
        ...

    @idle.setter
    def idle(self, value: Union[AnyStr, DisplayableResource, Displayable, Image]) -> None:
        """
        :param value: New idle overlay source.
        """
        ...

    @property
    def play_hover(self) -> Thumbnail:
        """
        Thumbnail overlay used when a playable resource is hovered.
        """
        ...

    @play_hover.setter
    def play_hover(self, value: Union[AnyStr, DisplayableResource, Displayable, Image]) -> None:
        """
        :param value: New hover overlay source for playable resources.
        """
        ...

    @property
    def play_idle(self) -> Thumbnail:
        """
        Thumbnail overlay used when a playable resource is idle.
        """
        ...

    @play_idle.setter
    def play_idle(self, value: Union[AnyStr, DisplayableResource, Displayable, Image]) -> None:
        """
        :param value: New idle overlay source for playable resources.
        """
        ...

    @property
    def locked(self) -> Thumbnail:
        """
        Thumbnail overlay used for locked resources.
        """
        ...

    @locked.setter
    def locked(self, value: Union[AnyStr, DisplayableResource, Displayable, Image]) -> None:
        """
        :param value: New locked overlay source.
        """
        ...

    @property
    def video_thumbnails_folder(self) -> str:
        """
        Folder used to search generated video thumbnails.
        """
        ...

    @video_thumbnails_folder.setter
    def video_thumbnails_folder(self, value: AnyStr | None) -> None:
        """
        :param value: Folder path used to resolve generated video thumbnails.
        """
        ...

    @property
    def allow_animation_thumbnail(self) -> bool:
        """
        Whether animations may provide an image thumbnail automatically.
        """
        ...

    @allow_animation_thumbnail.setter
    def allow_animation_thumbnail(self, value: Any) -> None:
        """
        :param value: Truthy value to enable automatic animation thumbnails.
        """
        ...

    @property
    def allow_animation_speeds(self) -> bool:
        """
        Whether animation speeds may be changed dynamically.
        """
        ...

    @allow_animation_speeds.setter
    def allow_animation_speeds(self, value: Any) -> None:
        """
        :param value: Truthy value to enable dynamic animation speeds.
        """
        ...

    @property
    def animation_speed(self) -> int:
        """
        Active speed multiplier used for animation resources.
        """
        ...

    @animation_speed.setter
    def animation_speed(self, value: SupportsInt) -> None:
        """
        :param value: New animation speed multiplier.
        """
        ...

    @property
    def allow_animation_size(self) -> bool:
        """
        Whether animation resources should adapt to the current screen size.
        """
        ...

    @allow_animation_size.setter
    def allow_animation_size(self, value: Any) -> None:
        """
        :param value: Truthy value to resize animations to the screen.
        """
        ...

    @property
    def transition(self) -> Any:
        """
        Transition used when showing gallery resources.
        """
        ...

    @transition.setter
    def transition(self, value: Any) -> None:
        """
        :param value: Transition object used when showing resources.
        """
        ...
