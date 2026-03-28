from renpy.display.behavior import Button
from .actions.items import ShowItem
from .config.resources import ResourcesConfig
from .resources.animation import AnimationResource
from .resources.displayable import DisplayableResource
from .resources.exceptions import IncompatibleResourceError
from .resources.images import ImageResource
from .resources.thumbnail import creates
from .resources.video import VideoResource
from .sizes.size_int import SizeInt
from .handler.base.helpers import create_items_overlay

__all__ = (
    'create_buttons', 'isvideo',
    'isimage', 'isdisplayable', 'isanimation'
)


def isvideo(source):
    return isinstance(source, VideoResource)


def isimage(source):
    return isinstance(source, ImageResource)


def isdisplayable(source):
    return isinstance(source, DisplayableResource)


def isanimation(source):
    return isinstance(source, AnimationResource)


def create_buttons(items, size):
    size = tuple(SizeInt.of(size))
    res = ResourcesConfig.get_instance()

    idle, not_found = res.idle.create(size), res.not_found.create(size)
    play_idle, play_hover = res.play_idle.create(size), res.play_hover.create(size)
    locked, hover = res.locked.create(size), None

    allow_anim, video_fol = res.allow_animation_thumbnail, res.video_thumbnails_folder
    thumbnails = {}

    for item in items:
        try:
            res = item.thumbnail.prepare(allow_anim, video_fol)
            key = (res.source,)
            dis = thumbnails.get(key, None)
            if dis is None:
                dis = thumbnails[key] = creates(res, size)
        except IncompatibleResourceError:
            dis = not_found

def create_buttons(items, size, resources_config=None, screens_config=None):
    for ((item, displayable), (idle, hover, locked)) in create_items_overlay(items, size, resources_config):
        yield Button(
            child=displayable, selected_child=locked,
            action=ShowItem(item, resources_config=resources_config, screens_config=screens_config),
            idle_foreground=idle, hover_foreground=hover,
            yalign=0.5, xalign=0.5,
            xysize=size, padding=(0, 0)
        )
