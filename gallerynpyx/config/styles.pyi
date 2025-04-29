from typing import Any

from ..common.classes.objects import SingletonRegistry


class StylesConfig(SingletonRegistry):

    def __init__(self: Any):
        ...

    @property
    def root(self: Any):
        """
        The style name for the root screen.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @root.setter
    def root(self: Any, value):
        ...

    @property
    def root_prefix(self: Any):
        """
        The prefix name for each element of the root screen.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @root_prefix.setter
    def root_prefix(self: Any, value):
        ...

    @property
    def tooltip(self: Any):
        """
        The style name for the tooltip screen.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @tooltip.setter
    def tooltip(self: Any, value):
        ...

    @property
    def tooltip_prefix(self: Any):
        """
        The prefix name for each element of the tooltip screen.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @tooltip_prefix.setter
    def tooltip_prefix(self: Any, value):
        ...

    @property
    def navigation(self: Any):
        """
        The style name for the navigation ``frame``.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @navigation.setter
    def navigation(self: Any, value):
        ...

    @property
    def navigation_box(self: Any):
        """
        The style name for the navigation ``vbox``.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @navigation_box.setter
    def navigation_box(self: Any, value):
        ...

    @property
    def scrollbar(self: Any):
        """
        The style name for the ``scrollbar`` on slides.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @scrollbar.setter
    def scrollbar(self: Any, value):
        ...

    @property
    def items(self: Any):
        """
        The style name for the ``grid`` of items.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @items.setter
    def items(self: Any, value):
        ...

    @property
    def slides(self: Any):
        """
        The style name for the ``viewport`` of slides.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @slides.setter
    def slides(self: Any, value):
        ...

    @property
    def controls(self: Any):
        """
        The style name for the ``vbox`` of the controls.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @controls.setter
    def controls(self: Any, value):
        ...
