style gx_fill:
    xfill True
    yfill True

style gx_navigation:
    xsize int(config.screen_width * 0.218)
    yalign 1.0
    padding (10, 20)

style gx_navigation_box:
    spacing 20

style gx_text:
    size 22
    color "#fff"

style gx_tooltip is gx_text
style gx_tooltip_text is gx_text
style gx_tooltip is gx_navigation

style gx_tooltip:
    align (0.0, 0.0)
    background None
    padding (0, 10)

style gx_tooltip_text:
    align (0.5, 0.0)

style gx_version is gx_tooltip

style gx_version:
    padding (5, 5)
    align (1.0, 1.0)
    size 10

style gx is gx_fill

style gx:
    spacing 10

style gx_button_text is gx_text

style gx_button_text:
    hover_color "#99ccff"
    selected_color "#99ccff"
    insensitive_color "#dedede"

style gx_vscrollbar is vscrollbar

style gx_vscrollbar:
    xsize 8

style gx_items is gx_fill

style gx_slides:
    xfill True
    ysize 250

style gx_controls:
    xfill True
