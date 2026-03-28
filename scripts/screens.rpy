screen gallerynpyx(gx_handler=None, gx_size=None):
    tag menu
    
    python:
        gx_size = gx_size if gx_size is not None else (config.screen_width, config.screen_height)
        gx_handler = gallerynpyx.handler.coerce(name=gx_handler)
        gx_config = gx_handler.screens_config

    add gx_config.background.resource.displayable(gx_size)
    add gx_config.foreground.resource.displayable(gx_size)

    use expression gx_config.root_screen pass (gx_handler,)

    text _("gallerynpyx v[gallerynpyx.version]"):
        style "gx_version"


screen gx_root(gx_handler=None):
    python:
        gx_handler = gallerynpyx.handler.coerce(name=gx_handler)

        gx_config = gx_handler.styles_config

    hbox:
        style gx_config.root
        style_prefix gx_config.root

        $ gx_config = gx_handler.screens_config

        use expression gx_config.navigation_screen pass (gx_handler,)
        use expression gx_config.items_screen pass (gx_handler,)

    use expression gx_config.tooltip_screen pass (GetTooltip(), gx_handler)


screen gx_navigation(gx_handler=None):
    python:
        gx_handler = gallerynpyx.handler.coerce(name=gx_handler)
        gx_config = gx_handler.styles_config

    frame:
        style gx_config.navigation
        style_prefix gx_config.navigation
        has vbox

        $ gx_config = gx_handler.resources_config

        if gx_config.allow_animation_speeds and gx_handler.has_animation:
            $ gx_config = gx_handler.screens_config
            use expression gx_config.animation_controls_screen pass (gx_handler,)
            use expression gx_config.controls_screen pass (True, gx_handler)
        else:
            $ gx_config = gx_handler.screens_config
            use expression gx_config.slide_controls_screen pass (gx_handler,)
            use expression gx_config.controls_screen pass (False, gx_handler)

screen gx_items(gx_handler=None):
    python:
        gx_handler = gallerynpyx.handler.coerce(name=gx_handler)
        gx_config = gx_handler.styles_config

    grid gx_handler.cols gx_handler.rows:
        style gx_config.items
        style_prefix gx_config.items
        for gx_button in gx_handler.buttons:
            add gx_button

screen gx_slide_controls(gx_handler=None):
    python:
        gx_handler = gallerynpyx.handler.coerce(name=gx_handler)
        gx_config = gx_handler.styles_config

    side "c r":
        viewport id "gx_slide_controls":
            style gx_config.slide_controls
            style_prefix gx_config.slide_controls
            mousewheel True
            draggable True
            vbox:
                for gx_slide in gx_handler.slides:
                    textbutton _("[gx_slide.label!t]"):
                        action gallerynpyx.actions.ChangeSlide(gx_slide, gx_handler)

        $ gx_config = gx_handler.screens_config
        if gx_config.show_scrollbar:
            $ gx_config = gx_handler.styles_config
            vbar:
                style gx_config.scrollbar
                value YScrollValue("gx_slide_controls")
        else:
            null

screen gx_animation_controls(gx_handler=None):
    python:
        gx_handler = gallerynpyx.handler.coerce(name=gx_handler)
        gx_config = gx_handler.styles_config
    hbox:
        style gx_config.animation_controls
        style_prefix gx_config.animation_controls
        for speed in range(1, 5):
            textbutton _("x[speed]"):
                action gallerynpyx.actions.ChangeAnimationSpeed(speed, gx_handler.resources_config)

screen gx_controls(has_animations=False, gx_handler=None, ):
    python:
        gx_handler = gallerynpyx.handler.coerce(name=gx_handler)
        gx_config = gx_handler.styles_config

    vbox:
        style gx_config.controls
        style_prefix gx_config.controls

        textbutton _("Previous"):
            action gallerynpyx.actions.PreviousPage(gx_handler)

        textbutton _("Next"):
            action gallerynpyx.actions.NextPage(gx_handler)

        textbutton _("Return"):
            action gallerynpyx.actions.ReturnSlide(has_animations, gx_handler)

screen gx_tooltip(text, gx_handler=None):
    if text:
        python:
            gx_handler = gallerynpyx.handler.coerce(name=gx_handler)
            gx_config = gx_handler.styles_config

        frame:
            style gx_config.tooltip
            style_prefix gx_config.tooltip
            text _("[text!t]")

screen gx_images(displayable, item, *args):
    add displayable
