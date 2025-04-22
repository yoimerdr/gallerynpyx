from ..common.helpers import tostring
from ..common.classes.objects import SingletonRegistry

__all__ = (
    'StylesConfig',
)

class StylesConfig(SingletonRegistry):
    __slots__ = (
        '_root', '_root_pr', '_tip', '_tip_pr',
        '_nav', '_nav_box', '_vs', '_it',
        '_sld', '_ctrl',
    )

    def __init__(self):
        self.root = self.root_prefix = self.tooltip = self.tooltip_prefix = None
        self.navigation = self.scrollbar = self.navigation_box = self.items = None
        self.slides = self.controls = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = tostring(value, "gx")

    @property
    def root_prefix(self):
        return self._root_pr

    @root_prefix.setter
    def root_prefix(self, value):
        self._root_pr = tostring(value, "gx")

    @property
    def tooltip(self):
        return self._tip

    @tooltip.setter
    def tooltip(self, value):
        self._tip = tostring(value, "gx_tooltip")

    @property
    def tooltip_prefix(self):
        return self._tip_pr

    @tooltip_prefix.setter
    def tooltip_prefix(self, value):
        self._tip_pr = tostring(value, "gx_tooltip")

    @property
    def navigation(self):
        return self._nav

    @navigation.setter
    def navigation(self, value):
        self._nav = tostring(value, "gx_navigation")

    @property
    def navigation_box(self):
        return self._nav_box

    @navigation_box.setter
    def navigation_box(self, value):
        self._nav_box = tostring(value, "gx_navigation_box")

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
    def slides(self):
        return self._sld

    @slides.setter
    def slides(self, value):
        self._sld = tostring(value, "gx_slides")

    @property
    def controls(self):
        return self._ctrl

    @controls.setter
    def controls(self, value):
        self._ctrl = tostring(value, "gx_controls")
