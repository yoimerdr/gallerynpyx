from renpy.exports import restart_interaction
from renpy.ui import Action


class Interactive(Action):
    def __call__(self, *args, **kwargs):
        restart_interaction()

