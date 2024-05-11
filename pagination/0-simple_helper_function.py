#!/usr/bin/env python3
"""doc"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """doc"""
    nbr1 = page - 1
    nbr1 = page_size * nbr1
    nbr2 = page * page_size
    return (nbr1, nbr2)
