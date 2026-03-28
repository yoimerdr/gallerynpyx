from store import Return
from .base import HandlerInteractive
from ..common.helpers import isdefine
from ..common.classes.helpers import add_metaclass
from ..common.classes.meta import SingletonMeta, RegistryMeta

__all__ = ('NextPage', 'PreviousPage', 'ChangeSlide', 'ReturnSlide')

@add_metaclass(SingletonMeta)
class NextPage(HandlerInteractive):
    def __init__(self, handler=None):
        super(NextPage, self).__init__(handler)

    def get_sensitive(self):
        handler = self.handler
        return handler.end < handler.total

    def __call__(self, *args, **kwargs):
        self.handler.next()
        super(NextPage, self).__call__(*args, **kwargs)


@add_metaclass(SingletonMeta)
class PreviousPage(HandlerInteractive):
    def __init__(self, handler=None):
        super(PreviousPage, self).__init__(handler)

    def get_sensitive(self):
        return self.handler.start > 0

    def __call__(self, *args, **kwargs):
        self.handler.previous()
        super(PreviousPage, self).__call__(*args, **kwargs)

@add_metaclass(RegistryMeta)
class ChangeSlide(HandlerInteractive):
    def __init__(self, slide, handler=None):
        super(ChangeSlide, self).__init__(handler)
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
    def __init__(self, has_animations=False, handler=None):
        super(ReturnSlide, self).__init__(handler)
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
            handler.resources_config.animation_speed = 1

        if isdefine(target):
            route = target.route()
            handler.change(*route if route else (None,))

            super(ReturnSlide, self).__call__(*args, **kwargs)

        return None
