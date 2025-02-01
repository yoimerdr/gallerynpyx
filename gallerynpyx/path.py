import os.path

from renpy.exports import loadable

__all__ = ('sep', 'isloadable', 'normpath', 'join')

sep = "/"


def isloadable(path, normalized=False, extensions=None):
    if not normalized:
        path = normpath(path)
    if not path or (extensions and not path.endswith(extensions)):
        return False

    return loadable(path)


def normpath(path):
    if path is None:
        return None

    path = os.path.normpath(path)

    return path if os.path.sep == sep else path.replace(os.path.sep, sep)


def join(path, *paths):
    return sep.join((path,) + paths)
