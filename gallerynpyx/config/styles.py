from ..common.helpers import tostring
from ..common.classes.objects import SingletonRegistry

__all__ = (
    'StylesConfig',
)

class StylesConfig(SingletonRegistry):
    __slots__ = (
        '_root', '_tip',
        '_nav', '_vs', '_it',
        '_sld', '_ctrl',
    )

    def __init__(self):
        self.root = self.tooltip = None
        self.navigation = self.scrollbar = self.items = None
        self.slides = self.controls = None

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
