from typing import Iterable


class RawStatement:
    pass

class RawMultipurpose(RawStatement):
    warper = None


class RawBlock:
    statements: Iterable[RawStatement]
