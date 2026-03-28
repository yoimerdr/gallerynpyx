from renpy.display.behavior import Button
from .actions.items import ShowItem
from .handler.base.helpers import create_items_overlay

__all__ = ('create_buttons',)


def create_buttons(items, size, resources_config=None, screens_config=None):
    for ((item, displayable), (idle, hover, locked)) in create_items_overlay(items, size, resources_config):
        yield Button(
            child=item, selected_child=locked,
            action=ShowItem(item, ),
            idle_foreground=idle, hover_foreground=hover,
            yalign=0.5, xalign=0.5,
            xysize=size, padding=(0, 0)
        )
