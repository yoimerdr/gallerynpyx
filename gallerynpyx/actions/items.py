from renpy.config import screen_width, screen_height
from renpy.exports import music_start, movie_cutscene, show_screen, music_stop, invoke_in_new_context, transition
from renpy.ui import Action, saybehavior, interact

from ..anim import set_speed
from ..common.classes.helpers import add_metaclass
from ..common.classes.meta import RegistryMeta
from ..config import ScreensConfig, ResourcesConfig
from ..resources.displayable import DisplayableResource
from ..resources.thumbnail import creates
from ..resources.video import VideoResource
from ..slides.items import isitem
from ..common.helpers import isdefine
from ..common.exceptions import AssignmentError

__all__ = ('ShowItem',)


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

    def show(self):
        item = self._item
        if item.locked:
            return None

        song, resource = item.song, item.resource
        if song:
            music_start(song)

        saybehavior()
        cfg = ResourcesConfig.get_instance()
        transition(cfg.transition)
        if isinstance(resource, VideoResource):
            return movie_cutscene(resource.load(True), loops=-1, stop_music=isdefine(song))
        else:
            if isinstance(resource, DisplayableResource):
                res = creates(resource, (screen_width, screen_height))
            else:
                res = resource.load(True)
                if cfg.allow_animation_speeds:
                    set_speed(res, cfg.animation_speed)

            show_screen(ScreensConfig.get_instance().images_screen, res, item)
        if song:
            music_stop(song)
        interact()
        transition(cfg.transition)
        return None

    def __call__(self, *args, **kwargs):
        if self._item.locked:
            return

        invoke_in_new_context(self.show)
