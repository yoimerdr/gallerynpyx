import sys

if sys.version_info[0] < 3:
    def imap(fn, iterable):
        return (fn(it) for it in iterable)


    def ifilter(fn, iterable):
        return (it for it in iterable if fn(it))


    irange = xrange
else:
    imap = map
    ifilter = filter
    irange = range


def first(iterable, default=None, key=None):
    if key is None:
        key = bool

    if not iterable:
        return default

    for it in iterable:
        if key(it):
            return it

    return default


def last(iterable, default=None, key=None):
    try:
        first(reversed(iterable), default, key)
    except TypeError:
        return last(tuple(iterable), default, key)
