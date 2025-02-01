from .displayable import Displayable

class Surfer:     
    def get_size(self): return (1920, 1080)

class Image(Displayable):     
    def __init__(self, path): pass
    
    def load(self): return Surfer()

class Scale(Displayable):     
    def __init__(self, path, width, height, *args, **kwargs): pass

class FactorScale(Displayable):
    def __init__(self, path, width, height=None, *args, **kwargs): pass
    image = None

class Composite:     
    def __init__(self, size, positions, displayable): pass


