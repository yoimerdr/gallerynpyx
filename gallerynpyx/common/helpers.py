from .compat import basestring


def noact(*args, **kwargs): pass


def tostring(obj, default=None):
    if isinstance(obj, basestring):
        return obj
    return default if obj is None else str(obj)


def cast(obj, caster, default=None, allowed_exceptions=None, **kwargs):
    if allowed_exceptions is None:
        allowed_exceptions = Exception

    try:
        return caster(obj, **kwargs)
    except allowed_exceptions:
        return default