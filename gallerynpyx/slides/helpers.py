from .base import route, isslide
from .slider import Slider
from .slide import Slide
from ..resources.animation import AnimationResource


def slide(name, *names, **kwargs):
    routes = route((name,) + names)
    label = kwargs.get("label", None)
    if not routes:
        return None

    if len(routes) == 1:
        return Slide(routes[0], label=label)

    parent, name = routes[:-1], routes[-1]

    parent = slider(*parent)
    return Slide(name, parent, label)


def slider(name, *names, **kwargs):
    slider = Slider.chain((name, ) + names, creates=True)
    slider.label = kwargs.get('label', None)
    return slider


def has_animation(slide):
    if not isslide(slide):
        return False
    return any(isinstance(it.resource, AnimationResource) for it in slide)
