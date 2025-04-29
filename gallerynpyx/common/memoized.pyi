from typing import Any, Callable


class Memoized(object):
    """
    A class that caches function results based on input arguments.

    Stores and reuses previously calculated results,
    avoiding redundant computations for the same input arguments.
    """

    def __init__(self: Any, builder: Callable):
        """
        :param builder: The function to be memoized
        """
        ...

    def dispose(self: Any):
        """
        Clear the memoization cache and release stored results.
        """
        ...

    def evaluate(self: Any, *args) -> Any:
        """
        Evaluate the function with given arguments.

        :param args: Arguments to pass to the builder function.
        :return: Cached or newly computed result for the given arguments.
        """
        ...

    def __call__(self: Any, *args):
        """
        Make the instance callable and invoke ``evaluate`` method.

        :param args: Arguments to pass to the builder function.
        :return: Cached or newly computed result for the given arguments.
        """
        ...
