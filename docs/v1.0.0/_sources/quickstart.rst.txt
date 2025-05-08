Quickstart
==========

Here you will learn how you can add the gallery offered by gallerynpyx to your game.
We will do this using a basic renpy project like **tutorial**.

Therefore, it is assumed that you have a basic knowledge of how Ren'py works. If not, give the
`docs <https://www.renpy.org/doc/html/quickstart.html>`_ a thorough reading.

The gallerynpyx scripts
-----------------------

Before you start creating the gallery,
you need to download the files necessary for the correct functioning of gallerynpyx.
To get started you must download the
`latest release <https://www.github.com/yoimerdr/gallerynpyx/releases/latest>`_ of gallerynpyx.

Once you have downloaded ``gallerynpyx``, you must extract it into the ``game`` folder of the game.

.. figure:: quickstart/extract.png
    :width: 45em
    :align: center

    The game folder of the game.


.. _default-gallery:

The default gallery
-------------------

After extracting the files into the game folder, you can add some items to display in the gallerynpyx gallery.

::

    image gx_image = "images/concert1.png"

    image gx_animation:
        "concert1" with Dissolve(.1)
        pause .4
        "concert2" with Dissolve(.1)
        pause .4
        "concert3" with Dissolve(.1)
        pause .4
        "concert2" with Dissolve(.1)
        pause .4
        repeat

    init python:
        # init handler
        gx_handler = gallerynpyx.get_handler()
        gx_handler.put("images", "gx_image")
        gx_handler.put("animations", gallerynpyx.resources.AnimationResource("gx_animation"),)
        gx_handler.put("videos", "oa4_launch.webm", thumbnail="concert1")

        gx_handler.to_first()

And to display the gallery, inside the ``screens.rpy`` file and on the ``navigation screen``,
or wherever you want to display the option, you could put something like:

::

    # the renpy default navigation
    screen navigation():
        vbox:
            # ..... other options
            textbutton _("Gallerynpyx") action ShowMenu("gallerynpyx")
            # ..... other options

And that's it, you now have a basic gallery to display in your renpy games.

.. figure:: quickstart/gallery.png
    :width: 70em
    :align: center

    A basic gallerynpyx gallery.


The gallery with sliders
------------------------

When displaying the gallery, you may want to qualify the images, animations or videos to be displayed according to certain parameters.
For example, divide them by chapter or game character. Gallerynpyx also offers methods for this.
They are :class:`~gallerynpyx.slides.slide.Slide` and :class:`~gallerynpyx.slides.slider.Slider`.

**Slide** refers to a list of items (images, animations or videos) and **Slider** refers to a collection of Slide and others Slider.
For example in :ref:`default-gallery`, the function :func:`~gallerynpyx.handler.Handler.put` creates and places the item in the Slide with the designated name.
But if it does not exist, it creates it first.
Thus, the Slide are created: ``images``, ``animations`` and ``videos``.

But if you wanted those slides to be inside a slider called ``Chapter 1``, you could do something like this:


::

    init python:
        gx_handler = gallerynpyx.get_handler()
        chapter1 = gallerynpyx.create_slider("ch1", label="Chapter 1")
        gx_handler.root.add(chapter1)

        gx_handler.put(("ch1", "images"), "gx_image")
        gx_handler.put(("ch1", "anim"), gallerynpyx.resources.AnimationResource("gx_animation"), label="animations")
        gx_handler.put(("ch1", "videos"), "oa4_launch.webm", thumbnail="concert1")


Thus, the result obtained would be:

.. figure:: quickstart/sliders.gif
    :width: 70em
    :align: center

    A basic slider like gallery

Gallery Items
-------------

Animations with speed
^^^^^^^^^^^^^^^^^^^^^

In your gallery you may want to display animations with the option to view them with more speed according to a certain value,
``gallerynpyx`` offers an extra display for these elements. For example, for animation in :ref:`default-gallery`.

::

    init python:
        # ...
        gx_handler.put("anim", gallerynpyx.resources.AnimationResource("gx_animation"), thumbnail="concert1", label="animations")

        gx_config = gallerynpyx.config.get_resources()
        gx_config.allow_animation_speeds = True

.. note::
    This setting will affect all animations (references) used in the gallery.

These changes will allow the display of speed-controlled animations in simple cases. However, in more complex animations,
it will be necessary to explicitly add the speed property to each pause or delay to achieve the desired behavior.

::

    image gx_complex_animation:
        "concert1" with Dissolve(.1)
        # ...
        pause 0.4 / gallerynpyx.config.get_resources().animation_speed
        # ...
        repeat


.. figure:: quickstart/item_animation_speed.png
    :width: 70em
    :align: center

    The animation screen with speed