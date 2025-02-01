class NameAlreadyExistsError(ValueError):
    def __init__(self, name, slider=None):
        message = "The name {!r} already exists".format(name)
        message += "." if slider is None else " in the slider {!r}.".format(slider.name)
        super(NameAlreadyExistsError, self).__init__(message)


class InvalidRouteError(ValueError):
    def __init__(self, reason):
        super(InvalidRouteError, self).__init__(reason)