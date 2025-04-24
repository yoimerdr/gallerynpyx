from renpy.exports import restart_interaction
from renpy.ui import Action


class Interactive(Action):
    def __call__(self, *args, **kwargs):
        restart_interaction()

class HandlerInteractive(Interactive):
    @property
    def handler(self):
        from ..handler import Handler
        return Handler.get_instance()
