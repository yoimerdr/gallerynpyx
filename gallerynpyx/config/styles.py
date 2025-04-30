from ..common.helpers import tostring
from ..common.classes.objects import SingletonRegistry

__all__ = (
    'StylesConfig',
)


class StylesConfig(SingletonRegistry):
    __slots__ = (
        '_root', '_tip',
        '_nav', '_vs', '_it',
        '_sld_crt', '_ctrl',
        '_anim_crt'
    )

    def __init__(self):
        self.root = self.tooltip = None
        self.navigation = self.scrollbar = self.items = None
        self.slide_controls = self.controls = None
        self.animation_controls = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = tostring(value, "gx")

    @property
    def tooltip(self):
        return self._tip

    @tooltip.setter
    def tooltip(self, value):
        self._tip = tostring(value, "gx_tooltip")

    @property
    def navigation(self):
        return self._nav

    @navigation.setter
    def navigation(self, value):
        self._nav = tostring(value, "gx_navigation")

    @property
    def scrollbar(self):
        return self._vs

    @scrollbar.setter
    def scrollbar(self, value):
        self._vs = tostring(value, "gx_scrollbar")

    @property
    def items(self):
        return self._it

    @items.setter
    def items(self, value):
        self._it = tostring(value, "gx_items")

    @property
    def slide_controls(self):
        return self._sld_crt

    @slide_controls.setter
    def slide_controls(self, value):
        self._sld_crt = tostring(value, "gx_slide_controls")

    @property
    def animation_controls(self):
        return self._anim_crt

    @animation_controls.setter
    def animation_controls(self, value):
        self._anim_crt = tostring(value, "gx_animation_controls")

    @property
    def controls(self):
        return self._ctrl

    @controls.setter
    def controls(self, value):
        self._ctrl = tostring(value, "gx_controls")
