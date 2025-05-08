# gallerynpyx

The next gallerynpy. A library to create and display a gallery in renpy games. 
gallerynpyx is a new improved, modularized and optimized version of gallerynpy (v2.0).
It improves usability and customization, adds events and aims to allow the integration of gallery extensions without much difficulty.

The gallery screen displays all images, animations and videos that have been inserted
into gallerynpyx handler.

## usage

Before using gallerynpyx, you need to download
the [latest version](https://github.com/yoimerdr/gallerynpyx/releases/latest) and copy it to your game.

Below is a simple use of gallerynpyx. The game in which it is used is in `tutorial (renpy 8.2.0)`.

```renpy
image gx_image = "images/concert1.png"

image gx_animation:
    # the concert# is an image file inside the images folder, renpy treats it automatically as an `image` type
    "concert1" with Dissolve(.1)
    pause .4
    "concert2" with Dissolve(.1)
    pause .4
    "concert3" with Dissolve(.1)
    pause .4
    "concert2" with Dissolve(.1)
    pause .4
    repeat

style gx_custom is gx_root

style gx_custom:
    # styling
    pass

init python:
    # resources config
    gx_config = gallerynpyx.config.get_resources()
    gx_config.allow_animation_speeds = True
    gx_config.allow_animation_thumbnail = True
    gx_config.transition = fade

    # screens config
    gx_config = gallerynpyx.config.get_screens()
    gx_config.show_scrollbar = True
    
    # styles config
    gx_config = gallerynpyx.config.get_styles()
    gx_config.root = "gx_custom"
    
    # init handler
    gx_handler = gallerynpyx.get_handler()
    gx_handler.put("images", "gx_image")
    
    # the following will give an error when you try to access the 'animations' slide, 
    # you can fix this by changing the init python to something like init 999 python 
    # or by explicitly specifying the type of resource.
    # gx_handler.put("animations", "gx_animation",)  
    gx_handler.put("animations", gallerynpyx.resources.AnimationResource("gx_animation"),)  
    gx_handler.put("videos", "oa4_launch.webm", thumbnail="concert1")

    gx_handler.to_first()    
```

And after adding and customizing, you can add some button to display the gallerynpyx screen

```renpy
# the renpy default navigation
screen navigation():
    vbox:
        # ..... other options
        textbutton _("Gallerynpyx") action ShowMenu("gallerynpyx")
        # ..... other options
```

## docs

You can read a quick guide and more about gallerynpyx in the [docs](https://yoimerdr.github.io/gallerynpyx/docs/).

## license

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## problems

If you encounter any problems or bugs while using the script, please open an issue in the GitHub repository.

Thanks for using my script! If you have any questions or suggestions, feel free to contact me.
