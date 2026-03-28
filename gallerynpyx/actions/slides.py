from renpy.display import predict
from store import Return
from .base import HandlerInteractive
from .. import isslide
from ..common.classes.helpers import add_metaclass
from ..common.classes.meta import RegistryMeta
from ..common.helpers import isdefine
from ..common.iters import paginate
from ..handler.base.helpers import create_items_thumbnail

__all__ = ('NextPage', 'PreviousPage', 'ChangeSlide', 'ReturnSlide')


@add_metaclass(RegistryMeta)
class NextPage(HandlerInteractive):
    def __init__(self, handler=None):
        super(NextPage, self).__init__(handler)

    def get_sensitive(self):
        handler = self.handler
        return handler.end < handler.total

    def __call__(self, *args, **kwargs):
        self.handler.next()
        super(NextPage, self).__call__(*args, **kwargs)

    def predict(self):
        if not self.get_sensitive():
            return

        for (_, displayable) in create_items_thumbnail(
                items=paginate(
                    items=self.handler.slide,
                    page=self.handler.page + 1,
                    per_page=self.handler.per_page
                ),
                size=self.handler.thumbnail_size,
                resources_config=self.handler.resources_config,
        ):
            predict.displayable(displayable)


@add_metaclass(RegistryMeta)
class PreviousPage(HandlerInteractive):
    def __init__(self, handler=None):
        super(PreviousPage, self).__init__(handler)

    def get_sensitive(self):
        return self.handler.start > 0

    def __call__(self, *args, **kwargs):
        self.handler.previous()
        super(PreviousPage, self).__call__(*args, **kwargs)

    def predict(self):
        if not self.get_sensitive():
            return

        index = self.handler.start - self.handler.per_page
        if index < 0:
            return

        for (_, displayable) in create_items_thumbnail(
                items=paginate(
                    items=self.handler.slide,
                    page=self.handler.page - 1,
                    per_page=self.handler.per_page
                ),
                size=self.handler.thumbnail_size,
                resources_config=self.handler.resources_config,
        ):
            predict.displayable(displayable)


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

    def predict(self):
        slide = self.__slide
        if isslide(slide):
            for (_, displayable) in create_items_thumbnail(
                    items=paginate(
                        items=slide,
                        page=1,
                        per_page=self.handler.per_page
                    ),
                    size=self.handler.thumbnail_size,
                    resources_config=self.handler.resources_config,
            ):
                predict.displayable(displayable)


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
