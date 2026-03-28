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
    res_cfg = coerce_resources(resources_config)

    idle, not_found = res_cfg.idle.create(size), res_cfg.not_found.create(size)
    play_idle, play_hover = res_cfg.play_idle.create(size), res_cfg.play_hover.create(size)
    locked, hover = res_cfg.locked.create(size), None

    allow_anim, video_fol = res_cfg.allow_animation_thumbnail, res_cfg.video_thumbnails_folder
    thumbnails = {}

    for item in items:
        try:
            res_cfg = item.thumbnail.prepare(allow_anim, video_fol)
            key = (res_cfg.source,)
            dis = thumbnails.get(key, None)
            if dis is None:
                dis = thumbnails[key] = creates(res_cfg, size)
        except IncompatibleResourceError:
            dis = not_found

        if isinstance(item.resource, (VideoResource, AnimationResource)):
            idle = play_idle
            hover = play_hover

        yield Button(
            child=dis, selected_child=locked,
            action=ShowItem(
                item,
                resources_config=res_cfg,
                screens_config=screens_config
            ),
            idle_foreground=idle, hover_foreground=hover,
            yalign=0.5, xalign=0.5,
            xysize=size, padding=(0, 0)
        )
