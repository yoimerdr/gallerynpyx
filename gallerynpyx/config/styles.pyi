from typing import Any, AnyStr

from ..common.classes.objects import SingletonRegistry


class StylesConfig(SingletonRegistry):
    """
    Common configuration for screens-related properties.

    :notes:
        * There will be only one instance
        * You can register a custom configuration by using the ``register`` class method before the first use of the class.
    """

    def __init__(self: Any):
        ...

    @classmethod
    def register(cls: Any, target: type[StylesConfig]):
        """
        Registers a target class in the registry.

        :param target: The class to register.
        """
        ...

    @classmethod
    def get_instance(cls: Any, *args, **kwargs) -> StylesConfig:
        """
        Creates or returns the singleton instance.

        :param args: Init class arguments.
        :param kwargs: Init class keyword arguments.
        """
        ...

    @property
    def root(self: Any) -> str:
        """
        The style name for the root screen.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @root.setter
    def root(self: Any, value: AnyStr):
        ...

    @property
    def tooltip(self: Any) -> str:
        """
        The style name for the tooltip screen.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @tooltip.setter
    def tooltip(self: Any, value: AnyStr):
        ...

    @property
    def navigation(self: Any) -> str:
        """
        The style name for the navigation ``frame``.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @navigation.setter
    def navigation(self: Any, value: AnyStr):
        ...

    @property
    def scrollbar(self: Any) -> str:
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
    def items(self: Any) -> str:
        """
        The style name for the ``grid`` of items.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @items.setter
    def items(self: Any, value: AnyStr):
        ...

    @property
    def slide_controls(self: Any) -> str:
        """
        The style name for the ``viewport`` of slides.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @slide_controls.setter
    def slide_controls(self: Any, value: AnyStr):
        ...

    @property
    def animation_controls(self: Any) -> str:
        ...

    @animation_controls.setter
    def animation_controls(self: Any, value: AnyStr):
        ...

    @property
    def controls(self: Any) -> str:
        """
        The style name for the ``vbox`` of the controls.

        :getter: Gets the style name.
        :setter: Sets a new style name.
        """
        ...

    @controls.setter
    def controls(self: Any, value: AnyStr):
        ...
