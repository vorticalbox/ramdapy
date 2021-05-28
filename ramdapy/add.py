from typing import Union, Callable, Optional


def add(a: int, b: Optional[int] = None) -> Union[int, Callable[[int], int]]:
    def _add(a, b):
        return a + b

    if b is None:
        return lambda b: _add(a, b)
    return _add(a.b)
