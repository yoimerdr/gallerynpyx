from renpy.display.behavior import Button
from .actions.items import ShowItem
from .config import coerce_resources
from .resources.animation import AnimationResource
from .resources.exceptions import IncompatibleResourceError
from .resources.thumbnail import creates
from .resources.video import VideoResource
from .sizes.size_int import SizeInt

__all__ = ('create_buttons',)


def create_buttons(items, size, resources_config=None, screens_config=None):
    size = tuple(SizeInt.of(size))
    resources_config = coerce_resources(resources_config)

    idle, not_found = resources_config.idle.create(size), resources_config.not_found.create(size)
    play_idle, play_hover = resources_config.play_idle.create(size), resources_config.play_hover.create(size)
    locked, hover = resources_config.locked.create(size), None

    allow_anim, video_fol = resources_config.allow_animation_thumbnail, resources_config.video_thumbnails_folder
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

        if isinstance(item.resource, (VideoResource, AnimationResource)):
            idle = play_idle
            hover = play_hover

        yield Button(
            child=dis, selected_child=locked,
            action=ShowItem(
                item,
                resources_config=resources_config,
                screens_config=screens_config
            ),
            idle_foreground=idle, hover_foreground=hover,
            yalign=0.5, xalign=0.5,
            xysize=size, padding=(0, 0)
        )
