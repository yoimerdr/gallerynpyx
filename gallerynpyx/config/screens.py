from ..common.classes.objects import SingletonRegistry
from ..common.helpers import tostring
from ..path import join
from ..resources.thumbnail import Thumbnail

__all__ = ('ScreensConfig',)


class ScreensConfig(SingletonRegistry):
    __slots__ = (
        '_s_img', '_fg', '_bg',
        '_sw_sv', '_s_rt',
        '_s_nav', '_s_it', '_s_tip', '_s_ani_crt',
        '_s_sld', '_s_ctr'
    )

    def __init__(self, ):
        self.images_screen = self.show_scrollbar = self.root_screen = None
        self.slide_controls_screen = self.navigation_screen = self.items_screen = None
        self.animation_controls_screen = self.controls_screen = self.tooltip_screen = None
        self._bg = Thumbnail("#fff5")
        self._fg = Thumbnail(join("gallerynpyx", "images", "menu.png"))

    @property
    def images_screen(self):
        return self._s_img

    @images_screen.setter
    def images_screen(self, value):
        self._s_img = tostring(value, default='gx_images')

    @property
    def root_screen(self):
        return self._s_rt

    @root_screen.setter
    def root_screen(self, value):
        self._s_rt = tostring(value, default='gx_root')

    @property
    def navigation_screen(self):
        return self._s_nav

    @navigation_screen.setter
    def navigation_screen(self, value):
        self._s_nav = tostring(value, default='gx_navigation')

    @property
    def items_screen(self):
        return self._s_it

    @items_screen.setter
    def items_screen(self, value):
        self._s_it = tostring(value, default='gx_items')

    @property
    def animation_controls_screen(self):
        return self._s_ani_crt

    @animation_controls_screen.setter
    def animation_controls_screen(self, value):
        self._s_ani_crt = tostring(value, default='gx_animation_controls')

    @property
    def controls_screen(self):
        return self._s_ctr

    @controls_screen.setter
    def controls_screen(self, value):
        self._s_ctr = tostring(value, default='gx_controls')

    @property
    def slide_controls_screen(self):
        return self._s_sld

    @slide_controls_screen.setter
    def slide_controls_screen(self, value):
        self._s_sld = tostring(value, default='gx_slide_controls')

    @property
    def tooltip_screen(self):
        return self._s_tip

    @tooltip_screen.setter
    def tooltip_screen(self, value):
        self._s_tip = tostring(value, default='gx_tooltip')

    @property
    def foreground(self):
        return self._fg

    @foreground.setter
    def foreground(self, value):
        self.foreground.set_custom(value)

    @property
    def background(self):
        return self._bg

    @background.setter
    def background(self, value):
        self.background.set_custom(value)

    @property
    def show_scrollbar(self):
        return self._sw_sv

    @show_scrollbar.setter
    def show_scrollbar(self, value):
        self._sw_sv = bool(value)
