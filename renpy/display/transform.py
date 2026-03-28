class Transform:
    def __init__(self, *args, **kwargs): pass


class TransformState:
    size = (None, None)

    def set_size(self, xysize):
        pass


class ATLTransform(Transform):
    state = TransformState()
