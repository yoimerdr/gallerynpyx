import sys

from .helpers import cast

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

def paginate(items, page, per_page):
    page = max(1, cast(page, int, default=1))

    start = (page - 1) * per_page
    end = start + per_page

    return items[start:end]