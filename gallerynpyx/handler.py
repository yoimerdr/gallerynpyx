from math import ceil

from renpy.config import screen_width, screen_height
from renpy.display.layout import Null
from .common.memoized import Memoized
from .helpers import create_buttons
from .common.classes.objects import SingletonRegistry, Singleton
from .common.helpers import isdefine
from .common.iters import first
from .sizes.size_int import SizeInt
from .slides.base import route, isslide
from .slides.helpers import has_animation, eachitem
from .slides.items import Item
from .slides.slider import Slider

__all__ = ('Handler',)


class Handler(SingletonRegistry):
    __slots__ = (
        '_rt', '_crt', '_sld',
        '_pg', '_rows', '_cols',
        '_sz', '_bmem',
    )

    def __init__(self):
        self._rt = self._crt = Slider("root")
        self._sld = self._sz = self._cols = self._rows = None
        self._bmem = Memoized(self._buttons)
        self._pg = 0
        self.change_distribution(4, 4)

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, rows):
        self.change_distribution(rows)

    @property
    def cols(self):
        return self._cols

    @cols.setter
    def cols(self, cols):
        self.change_distribution(cols=cols)

    @property
    def per_page(self):
        return self.rows * self.cols

    @property
    def pages(self):
        return ceil(self.total / self.per_page)

    @property
    def page(self):
        return self._pg

    @property
    def start(self):
        return self.page * self.per_page

    @property
    def end(self):
        return self.start + self.per_page

    @property
    def items(self):
        return self._sld[self.start:self.end] if self._sld else []

    @property
    def available_items(self):
        return min(self.per_page, self.total - self.start)

    @property
    def total(self):
        return len(self._sld) if self._sld else 0

    @property
    def slides(self):
        return self._crt.values() if self._crt else ()

    @property
    def has_animation(self):
        return has_animation(self._sld)

    @property
    def slide(self):
        return self._sld

    @property
    def root(self):
        return self._rt

    @property
    def current(self):
        return self._crt

    @property
    def thumbnail_size(self):
        return self._sz

    @property
    def ibuttons(self):
        start, end = self.start, self.end

        if self._sld:
            for button in create_buttons(self._sld[start:end], self.thumbnail_size):
                yield button
                start += 1

        for _ in range(start, end):
            yield Null()

    @property
    def buttons(self):
        return self._bmem.evaluate(self.start, self.end, self.slide)

    def _buttons(self, *args):
        return tuple(self.ibuttons)

    def change_distribution(self, rows=None, cols=None):
        if isdefine(rows):
            rows = max(rows, 1)
        if isdefine(cols):
            cols = max(cols, 1)

        if cols == self.cols and rows == self.rows:
            return

        self._rows, self._cols = rows, cols
        mx = max(rows, cols)

        width = screen_width * 0.782 - 20 * mx
        width = width / mx

        size = (width, width / (screen_width / screen_height))

        if self._sz is None:
            self._sz = SizeInt.of(size)
            return
        self._sz.set(size)

    def put_item(self, names, item, label=None, thumbnail=None):
        names, root = route(names), self.root

        target = root.get(names)
        if target is None:
            target = root.slide(*names, label=label)

        item.thumbnail.set_custom(thumbnail)
        return target.add(item)

    def put(self, names, resource, song=None, condition=None, tooltip=None,
            locked_tooltip=None, label=None, thumbnail=None):
        item = Item(resource, song, condition, tooltip, locked_tooltip)
        return self.put_item(names, item, label, thumbnail)

    def change(self, name, *names):
        root = self.root
        target = None if name is None and not names else root.get((name,) + names)
        if target is None:
            target = root
        elif isslide(target):
            self._sld, self._pg = target, 0
            self._crt = target.parent
            return
        self._crt = target
        self.to_first()

    def to_first(self):
        self._sld = first(self.slides, key=isslide)
        if self.has_animation:
            self._sld = None
        self._pg = 0
        self._bmem.dispose()

    def next(self):
        if not self._sld:
            return False

        if self.end >= len(self._sld):
            return False

        self._pg += 1
        return True

    def previous(self):
        if not self._sld:
            return False

        prev_index = self.start - self.per_page

        if prev_index < 0:
            return False

        self._pg -= 1
        return True

    def clear(self):
        self._bmem.dispose()
        for item in eachitem(self.root):
            item.resource.dispose()
        self._pg, self._sld = 0, None
        self._crt = self.root
        self.to_first()
