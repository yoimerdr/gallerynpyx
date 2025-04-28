from renpy.config import screen_width, screen_height
from renpy.exports import music_start, show_screen, music_stop, invoke_in_new_context, transition
from renpy.ui import Action, saybehavior, interact
from ..anim import set_speed
from ..common.classes.helpers import add_metaclass
from ..common.classes.meta import RegistryMeta
from ..common.exceptions import AssignmentError
from ..config import ScreensConfig, ResourcesConfig
from ..resources.displayable import DisplayableResource
from ..resources.video import VideoResource
from ..slides.items import isitem

__all__ = ('ShowItem', 'prepare_resource')


def prepare_resource(resource):
    cfg = ResourcesConfig.get_instance()
    if isinstance(resource, (DisplayableResource, VideoResource)):
        return resource.displayable((screen_width, screen_height))
    res = resource.load(True)
    if cfg.allow_animation_speeds:
        set_speed(res, cfg.animation_speed)
    return res


@add_metaclass(RegistryMeta)
class ShowItem(Action):

    def __init__(self, item):
        super(ShowItem, self).__init__()
        if not isitem(item):
            raise AssignmentError("The argument must be an 'Item' instance.")
        self._item = item

    def get_selected(self):
        return self._item.locked

    def get_tooltip(self):
        item = self._item
        return item.locked_tooltip if item.locked else item.tooltip

    def _show_displayable(self, resource, ):
        item = self._item
        cfg = ResourcesConfig.get_instance()
        saybehavior()
        transition(cfg.transition)
        res = prepare_resource(resource)
        show_screen(ScreensConfig.get_instance().images_screen, res, item)
        interact()
        if not isinstance(resource, VideoResource):
            transition(cfg.transition)
        elif item.song:
            music_stop()

    def show(self):
        item = self._item
        if item.locked:
            return

        song, resource = item.song, item.resource
        if song:
            music_start(song)

        if isinstance(resource, VideoResource):
            self._show_movie(resource)
            return
        else:
            self._show_displayable(resource)

        if song:
            music_stop()

    def __call__(self, *args, **kwargs):
        if self._item.locked:
            return

        invoke_in_new_context(self.show)

    _show_movie = _show_displayable
