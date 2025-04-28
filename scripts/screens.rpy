screen gallerynpyx():
    tag menu
    
    python:
        gx_size = (config.screen_width, config.screen_height)
        gx_config = gallerynpyx.config.get_screens()

    add gx_config.background.resource.displayable(gx_size)
    add gx_config.foreground.resource.displayable(gx_size)

    use expression gx_config.root_screen

    $ gx_config = gallerynpyx.config.get_styles()

    text _("gallerynpyx v[gallerynpyx.version]"):
        style "gx_version"


screen gx_root():
    $ gx_config = gallerynpyx.config.get_styles()

    hbox:
        style gx_config.root
        style_prefix gx_config.root_prefix

        $ gx_config = gallerynpyx.config.get_screens()

        use expression gx_config.navigation_screen
        use expression gx_config.items_screen

    use expression gx_config.tooltip_screen pass (GetTooltip(),)


screen gx_navigation():
    python:
        gx_handler = gallerynpyx.get_handler()
        gx_config = gallerynpyx.config.get_styles()

    frame:
        style gx_config.navigation
        has vbox
        style gx_config.navigation_box

        $ gx_config = gallerynpyx.config.get_resources()

        if gx_config.allow_animation_speeds and gx_handler.has_animation:
            $ gx_config = gallerynpyx.config.get_screens()
            use expression gx_config.animations_screen
            use expression gx_config.controls_screen pass (True,)
        else:
            $ gx_config = gallerynpyx.config.get_screens()
            use expression gx_config.slides_screen
            use expression gx_config.controls_screen pass (False,)

screen gx_items():
    python:
        gx_handler = gallerynpyx.get_handler()
        gx_config = gallerynpyx.config.get_styles()

    grid gx_handler.cols gx_handler.rows:
        style gx_config.items
        for gx_button in gx_handler.buttons:
            add gx_button

screen gx_slides():
    python:
        gx_handler = gallerynpyx.get_handler()
        gx_config = gallerynpyx.config.get_styles()

    side "c r":
        viewport id "gx_slides":
            style gx_config.slides
            mousewheel True
            draggable True
            vbox:
                for gx_slide in gx_handler.slides:
                    textbutton _("[gx_slide.label!t]"):
                        action gallerynpyx.actions.ChangeSlide(gx_slide)
        
        $ gx_config = gallerynpyx.config.get_screens()
        if gx_config.show_scrollbar:
            $ gx_config = gallerynpyx.config.get_styles()
            vbar:
                style gx_config.scrollbar
                value YScrollValue("gx_slides")
        else:
            null

screen gx_animations():
    hbox:
        for speed in range(1, 5):
            textbutton _("x[speed]"):
                action gallerynpyx.actions.ChangeAnimationSpeed(speed)

screen gx_controls(has_animations=False):
    $ gx_config = gallerynpyx.config.get_styles()
    vbox:
        style gx_config.controls
        textbutton _("Previous"):
            action gallerynpyx.actions.PreviousPage()
        
        textbutton _("Next"):
            action gallerynpyx.actions.NextPage()

        textbutton _("Return"):
            action gallerynpyx.actions.ReturnSlide(has_animations)
        
screen gx_tooltip(text):
    if text:
        $ gx_config = gallerynpyx.config.get_styles()

        frame:
            style gx_config.tooltip
            style_prefix gx_config.tooltip_prefix
            text _("[text!t]")

screen gx_images(displayable, item, *args):
    add displayable
