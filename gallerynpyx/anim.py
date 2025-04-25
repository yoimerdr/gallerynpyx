import os

from .common.iters import ifilter
from .resources.resource import IMAGES

SPEED_ATTRIBUTE = '__gx_speed__'

__all__ = ('is_pause_statement', 'get_images', 'get_statements', 'set_speed')


def is_pause_statement(statement):
    return getattr(statement, 'warper', None) == "pause"


def get_statements(animation, raw=True):
    atl = getattr(animation, 'atl' if raw else 'block', None)
    statements = getattr(atl, 'statements', ())
    return (it for it in statements)


def set_speed(animation, speed=None):
    if not animation:
        return animation

    current = getattr(animation, SPEED_ATTRIBUTE, 1)
    if current == speed or speed is None:
        return animation

    speed = float(max(speed, 1))
    current = current / speed

    for statement in ifilter(is_pause_statement, get_statements(animation, False)):
        duration = getattr(statement, 'duration', None)
        if duration is None:
            continue

        setattr(statement, 'duration', duration * current)

    setattr(animation, SPEED_ATTRIBUTE, speed)
    return animation


def get_images(animation):
    for statement in get_statements(animation):
        expressions = getattr(statement, 'expressions', ())
        for expression in expressions:
            if not expression or not expression[0]:
                continue

            expr = expression[0].strip('\'"')

            if expr == expression[0]:
                continue

            ext = os.path.splitext(expr)[-1]
            if not ext or ext in IMAGES:
                yield expr
