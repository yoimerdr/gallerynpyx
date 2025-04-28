__evts = {
    "gx-slide-change": None,
    "gx-page-change": None,
}


def on(event, callback):
    if not callable(callback) or not event in __evts:
        return

    listeners = __evts.get(event, None)
    if listeners is None:
        listeners = []
        __evts[event] = listeners

    listeners.append(callback)


def off(event, callback):
    if not callable(callback) or not event in __evts:
        return

    listeners = __evts.get(event, None)
    if listeners:
        listeners.remove(callback)

    if not listeners:
        __evts[event] = None


def _emit(event, *args, **kwargs):
    listeners = __evts.get(event, None)
    if listeners:
        for listener in listeners:
            listener(*args, **kwargs)


def clear(event):
    if event in __evts:
        __evts[event] = None
