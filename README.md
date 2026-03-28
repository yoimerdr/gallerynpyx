# gallerynpyx

[![Version](https://img.shields.io/badge/version-2.0.0-2ea043.svg)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/python-2.7%20%7C%203.x-3776AB.svg)](CHANGELOG.md)
[![Ren%27Py](https://img.shields.io/badge/Ren%27Py-7.x%20%7C%208.x-ff69b4.svg)](https://www.renpy.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-online-0A66C2.svg)](https://yoimerdr.github.io/gallerynpyx/docs/)

`gallerynpyx` is a modular gallery library for Ren'Py games. It is the next evolution of
`gallerynpy`, focused on customization, cleaner extension points, events, and support for
multiple gallery scopes through shared or local handlers/configurations.

The built-in screen can display images, animations, and videos that you register in a
`gallerynpyx` handler.

## Installation

Download the [latest release](https://github.com/yoimerdr/gallerynpyx/releases/tag/gallerynpyx-latest)
and copy the module into your game project.

## Quick Start

This is a shared-gallery setup using the tutorial assets, with its own style set for
the default gallery.

```renpy
image gx_image = "images/concert1.png"

image gx_animation:
    # concert# is an image inside the images folder.
    "concert1" with Dissolve(.1)
    pause .4
    "concert2" with Dissolve(.1)
    pause .4
    "concert3" with Dissolve(.1)
    pause .4
    "concert2" with Dissolve(.1)
    pause .4
    repeat

style gx_main_navigation is gx_navigation
style gx_main_navigation:
    xsize 280
    padding (12, 12)

style gx_main_navigation_vbox is gx_navigation_vbox

style gx_main_controls is gx_controls
style gx_main_controls:
    spacing 6

style gx_main_controls_button is button
style gx_main_controls_button_text is button_text

style gx_main_tooltip is gx_tooltip
style gx_main_tooltip_text is gx_tooltip_text

init python:
    gx_resources = gallerynpyx.config.get_resources()
    gx_resources.allow_animation_speeds = True
    gx_resources.allow_animation_thumbnail = True
    gx_resources.transition = fade

    gx_screens = gallerynpyx.config.get_screens()
    gx_screens.background = "#10141d"
    gx_screens.show_scrollbar = True

    gx_styles = gallerynpyx.config.get_styles()
    gx_styles.navigation = "gx_main_navigation"
    gx_styles.controls = "gx_main_controls"
    gx_styles.tooltip = "gx_main_tooltip"

    gx_handler = gallerynpyx.get_handler()
    gx_handler.put("images", "gx_image")

    # If the ATL image is not ready at this init priority, use AnimationResource
    # explicitly or initialize this later with a higher init priority.
    gx_handler.put(
        "animations",
        gallerynpyx.resources.AnimationResource("gx_animation"),
    )
    gx_handler.put("videos", "oa4_launch.webm", thumbnail="concert1")
    gx_handler.to_first()
```

To open the default gallery from your UI:

```renpy
screen navigation():
    vbox:
        textbutton _("Gallery") action ShowMenu("gallerynpyx")
```

## Local Galleries

`gallerynpyx` 2.x also supports local gallery scopes. A local gallery keeps its own
resources, screens, styles, and handler state under a name. You can still resolve
configs by name, but you can also access them directly from the local handler.
This example keeps the same tutorial assets, but gives the local gallery its own styles.


```renpy
style gx_extras_navigation is gx_navigation
style gx_extras_navigation:
    xsize 320
    padding (18, 18)

style gx_extras_navigation_vbox is gx_navigation_vbox
style gx_extras_navigation_button is button
style gx_extras_navigation_button_text is button_text

style gx_extras_controls is gx_controls
style gx_extras_controls:
    spacing 10

style gx_extras_controls_button is button
style gx_extras_controls_button_text is button_text

style gx_extras_tooltip is gx_tooltip
style gx_extras_tooltip_text is gx_tooltip_text

init python:
    gx_extras_handler = gallerynpyx.get_handler("extras")

    # Both approaches are valid for local galleries.
    gx_extras_resources = gallerynpyx.config.get_resources("extras")
    gx_extras_resources.allow_animation_speeds = True
    gx_extras_resources.allow_animation_thumbnail = True
    gx_extras_resources.transition = dissolve

    gx_extras_screens = gx_extras_handler.screens_config
    gx_extras_screens.background = "#141821"
    gx_extras_screens.show_scrollbar = True

    gx_extras_styles = gx_extras_handler.styles_config
    gx_extras_styles.navigation = "gx_extras_navigation"
    gx_extras_styles.controls = "gx_extras_controls"
    gx_extras_styles.tooltip = "gx_extras_tooltip"

    gx_extras_handler.put("images", "gx_image")
    gx_extras_handler.put(
        "animations",
        gallerynpyx.resources.AnimationResource("gx_animation"),
    )
    gx_extras_handler.put("videos", "oa4_launch.webm", thumbnail="concert1")
    gx_extras_handler.to_first()
```

You can then open that gallery by passing either the gallery name or the handler itself.
The built-in screens now work with whichever handler is passed in.

```renpy
screen navigation():
    vbox:
        textbutton _("Main Gallery") action ShowMenu("gallerynpyx")
        textbutton _("Extras Gallery") action ShowMenu("gallerynpyx", gx_handler="extras")
        textbutton _("Extras Gallery (Handler)") action ShowMenu("gallerynpyx", gx_handler=gx_extras_handler)
```

## Documentation

Read the quick guide and additional documentation at
[gallerynpyx/docs](https://yoimerdr.github.io/gallerynpyx/docs/).

## Changelog

Release history is tracked in [CHANGELOG.md](CHANGELOG.md).

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Issues

If you find a bug or run into a problem, please open an issue in the GitHub repository.
