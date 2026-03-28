from ... import config
from ..._internal import _events


class HandlerManager(object):
    __slots__ = (
        "_hdls",
        "_gb_bdr",
        "_lc_bdr",
    )

    def __init__(self, global_builder, local_builder):
        self._hdls = {}
        self._gb_bdr = global_builder
        self._lc_bdr = local_builder

    def get(self, name=None, override=False):
        name = str(name) if name is not None else ""
        if not name.strip():
            return self._gb_bdr()

        if not name in self._hdls or override:
            if override:
                self._flush(name)

            self._hdls[name] = self._lc_bdr(name)

        return self._hdls[name]

    def _flush(self, name):
        self._hdls.pop(name)
        config.resources.manager.flush(name)
        config.screens.manager.flush(name)
        config.styles.manager.flush(name)

    def flush(self, name=None):
        _events._emit("gx-handler-flush", name)
        if name is None:
            self._hdls.clear()
            self._flush(None)
        else:
            name = str(name)
            if name in self._hdls:
                self._flush(name)
