from .base import Interactive
from ..config import coerce_resources

__all__ = ('ChangeAnimationSpeed',)


class ChangeAnimationSpeed(Interactive):
    def __init__(self, speed, resources_config=None):
        self.__speed = speed
        self._resources_config = resources_config
        super(ChangeAnimationSpeed, self).__init__()

    def get_sensitive(self):
        return True

    def get_selected(self):
        cfg = coerce_resources(self._resources_config)
        return self.__speed == cfg.animation_speed

    def __call__(self, *args, **kwargs):
        cfg = coerce_resources(self._resources_config)
        cfg.animation_speed = self.__speed
        super(ChangeAnimationSpeed, self).__call__(*args, **kwargs)
