from .handler import Handler as get_handler
from .resources.helpers import guess as guess_resource
from .slides.base import isslide, isslider
from .slides.helpers import slide as create_slide, slider as create_slider
from .slides.items import Item as create_item, isitem

__all__ = (
    'version',
    'get_handler', 'guess_resource',
    'create_slide', 'create_slider',
    'create_item', 'isitem',
    'isslider', 'isslide'
)

version: str
"""
The gallerynpyx version.
"""
