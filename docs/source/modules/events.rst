events
------

This module provides several functions for subscribing to and listening to internal events broadcast.
These functions allow you to react to them, facilitating the implementation of logic with the gallery.

.. autoapifunction:: gallerynpyx.events.on

.. py:function:: on(event: Literal['gx-slide-change'], callback: Callable[[Literal['slider'], Slider], None])
    :no-index:

    .. include:: _on_doc.txt

.. py:function:: on(event: Literal['gx-page-change'], callback: Callable[[int, int], None])
    :no-index:

    .. include:: _on_doc.txt

.. py:function:: on(event: Literal['gx-item-show', 'gx-item-hide'], callback: Callable[[Item], None])
    :no-index:

    .. include:: _on_doc.txt

.. autoapifunction:: gallerynpyx.events.off
