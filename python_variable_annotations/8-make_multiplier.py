#!/usr/bin/env python3
"""takes a float to func"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float to func"""
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
