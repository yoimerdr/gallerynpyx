from renpy.display.transition import Transition
from store import dissolve
from ..common.classes.objects import SingletonRegistry
from ..common.helpers import coerce, cast
from ..path import join
from ..resources.thumbnail import Thumbnail

__all__ = ('ResourcesConfig',)


class ResourcesConfig(SingletonRegistry):
    _slots_ = (
        '_not_found', '_idle',
        '_play_hover', '_play_idle',
        '_locked', '_vdo_thumbs_folds',
        '_al_anim_thumbs', '_al_anim_speeds',
        '_anim_speed', '_tran',
    )

    def __init__(self):
        resources = join("gallerynpyx", "images")
        self._not_found = Thumbnail(join(resources, "not_found.png"))
        self._idle = Thumbnail(join(resources, "idle.png"))
        self._play_hover = Thumbnail(join(resources, "play_hover.png"))
        self._play_idle = Thumbnail(join(resources, "play_idle.png"))
        self._locked = Thumbnail(join(resources, "locked.png"))

        self.video_thumbnails_folder = self.allow_animation_thumbnail = self.allow_animation_speeds = None
        self.animation_speed = self.transition = None

    @property
    def not_found(self):
        return self._not_found

    @not_found.setter
    def not_found(self, value):
        self.not_found.set_custom(value)

    @property
    def idle(self):
        return self._idle

    @idle.setter
    def idle(self, value):
        self.idle.set_custom(value)

    @property
    def play_hover(self):
        return self._play_hover

    @play_hover.setter
    def play_hover(self, value):
        self.play_hover.set_custom(value)

    @property
    def play_idle(self):
        return self._play_idle

    @play_idle.setter
    def play_idle(self, value):
        self.play_idle.set_custom(value)

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        self.locked.set_custom(value)

    @property
    def video_thumbnails_folder(self):
        return self._vdo_thumbs_folds

    @video_thumbnails_folder.setter
    def video_thumbnails_folder(self, value):
        if value is None:
            value = join("gallerynpyx", "thumbnails")
        self._vdo_thumbs_folds = value

    @property
    def allow_animation_thumbnail(self):
        return self._al_anim_thumbs

    @allow_animation_thumbnail.setter
    def allow_animation_thumbnail(self, value):
        self._al_anim_thumbs = bool(value)

    @property
    def allow_animation_speeds(self):
        return self._al_anim_speeds

    @allow_animation_speeds.setter
    def allow_animation_speeds(self, value):
        self._al_anim_speeds = bool(value)

    @property
    def animation_speed(self):
        return self._anim_speed

    @animation_speed.setter
    def animation_speed(self, value):
        value = coerce(cast(value, int, 1), 1, 4)
        self._anim_speed = value

    @property
    def transition(self):
        return self._tran

    @transition.setter
    def transition(self, value):
        if value is None:
            self._tran = dissolve
            return
        tp = getattr(value, 'func', None)
        if tp is None:
            self._tran = dissolve
            return

        self._tran = value

