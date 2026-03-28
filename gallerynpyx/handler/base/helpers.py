from ...config.helpers import coerce_resources
from ...resources.animation import AnimationResource
from ...resources.exceptions import IncompatibleResourceError
from ...resources.thumbnail import creates
from ...resources.video import VideoResource
from ...sizes.size_int import SizeInt


def create_items_thumbnail(items, size, resources_config=None, ):
    size = tuple(SizeInt.of(size))
    resources_config = coerce_resources(resources_config)

    not_found = resources_config.not_found.create(size)

    thumbnails = {}

    allow_anim, video_fol = resources_config.allow_animation_thumbnail, resources_config.video_thumbnails_folder
    for item in items:
        resource = item.thumbnail.prepare(allow_anim, video_fol)
        try:
            key = (resource.source,)
            displayable = thumbnails.get(key, None)
            if displayable is None:
                displayable = thumbnails[key] = creates(resource, size)

        except IncompatibleResourceError:
            displayable = not_found

        yield item, displayable


def create_items_overlay(items, size, resources_config=None, ):
    size = tuple(SizeInt.of(size))
    resources_config = coerce_resources(resources_config)

    locked = resources_config.locked.create(size), resources_config.not_found.create(size)
    play_idle, play_hover = resources_config.play_idle.create(size), resources_config.play_hover.create(size)
    idle, hover = resources_config.idle.create(size), None

    for (item, displayable) in create_items_thumbnail(items, size, resources_config):
        if isinstance(item.resource, (VideoResource, AnimationResource)):
            idle, hover = play_idle, play_hover

        yield (
            (item, displayable),
            (idle, hover, locked),
        )
