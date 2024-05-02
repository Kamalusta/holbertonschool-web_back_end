#!/usr/bin/env python3
"""takes a string and an int OR float to tuple"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string and an int OR float to tuple"""
    v = v * v
    return (k, v)
