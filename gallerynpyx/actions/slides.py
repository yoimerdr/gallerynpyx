from store import Return
from .base import HandlerInteractive
from ..common.helpers import isdefine
from ..common.classes.helpers import add_metaclass
from ..common.classes.meta import SingletonMeta, RegistryMeta
from ..config.resources import ResourcesConfig

__all__ = ('NextPage', 'PreviousPage', 'ChangeSlide', 'ReturnSlide')

@add_metaclass(SingletonMeta)
class NextPage(HandlerInteractive):
    def __init__(self):
        super(NextPage, self).__init__()

    def get_sensitive(self):
        handler = self.handler
        return handler.end < handler.total

    def __call__(self, *args, **kwargs):
        self.handler.next()
        super(NextPage, self).__call__(*args, **kwargs)


@add_metaclass(SingletonMeta)
class PreviousPage(HandlerInteractive):
    def __init__(self):
        super(PreviousPage, self).__init__()

    def get_sensitive(self):
        return self.handler.start > 0

    def __call__(self, *args, **kwargs):
        self.handler.previous()
        super(PreviousPage, self).__call__(*args, **kwargs)

@add_metaclass(RegistryMeta)
class ChangeSlide(HandlerInteractive):
    def __init__(self, slide):
        super(ChangeSlide, self).__init__()
        self.__slide = slide

    def get_selected(self):
        return self.handler.slide is self.__slide

    def get_sensitive(self):
        return True

    def __call__(self, *args, **kwargs):
        if self.get_selected():
            return

        self.handler.change(*self.__slide.route())
        super(ChangeSlide, self).__call__(*args, **kwargs)


@add_metaclass(RegistryMeta)
class ReturnSlide(HandlerInteractive):
    def __init__(self, has_animations=False):
        super(ReturnSlide, self).__init__()
        self._has_animations = has_animations

    def __call__(self, *args, **kwargs):
        handler = self.handler
        slide, root = handler.slide, handler.root

        if slide is None:
            current = handler.current
            if root is current:
                handler.reset()
                return Return()()
            target = current
        else:
            target = slide.parent

        if not self._has_animations and target is root:
            handler.reset()
            return Return()()

        if not self._has_animations:
            target = target.parent
        else:
            ResourcesConfig.get_instance().animation_speed = 1

        if isdefine(target):
            route = target.route()
            handler.change(*route if route else (None,))

            super(ReturnSlide, self).__call__(*args, **kwargs)

        return None
