from renpy.display.displayable import Displayable


class Null(Displayable):
    pass


def Composite(size, positions, displayable, *args, **kwargs):
    from renpy.display.im import Composite
    return Composite(size, positions, displayable)
