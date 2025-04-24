from .base import Interactive
from ..config.resources import ResourcesConfig

__all__ = ('ChangeAnimationSpeed',)


class ChangeAnimationSpeed(Interactive):
    def __init__(self, speed):
        self.__speed = speed
        super(ChangeAnimationSpeed, self).__init__()

    def get_sensitive(self):
        return True

    def get_selected(self):
        return self.__speed == ResourcesConfig.get_instance().animation_speed

    def __call__(self, *args, **kwargs):
        ResourcesConfig.get_instance().animation_speed = self.__speed
        super(ChangeAnimationSpeed, self).__call__(*args, **kwargs)
