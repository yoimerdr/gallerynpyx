class ConfigManager(object):
    __slots__ = (
        "_cfgs",
        "_gb_bdr",
        "_lc_bdr",
    )

    def __init__(self, global_builder, local_builder):
        self._cfgs = {}
        self._gb_bdr = global_builder
        self._lc_bdr = local_builder

    def get(self, name=None, override=False):
        name = str(name) if name is not None else ""
        if not name.strip():
            return self._gb_bdr()

        if not name in self._cfgs or override:
            self._cfgs[name] = self._lc_bdr()

        return self._cfgs[name]

    def flush(self, name=None):
        if name is None:
            self._cfgs.clear()
        else:
            name = str(name)
            if name in self._cfgs:
                self._cfgs.pop(name)
