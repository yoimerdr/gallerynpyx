from renpy.exports import restart_interaction
from renpy.ui import Action


class Interactive(Action):
    def __call__(self, *args, **kwargs):
        restart_interaction()


class HandlerInteractive(Interactive):
    def __init__(self, handler=None):
        self._handler = handler
        super(HandlerInteractive, self).__init__()

    @property
    def handler(self):
        from ..handler.helpers import coerce

        return coerce(name=self._handler)
