#!/usr/bin/env python3
"""takes int and float to sum of float"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes int and float to sum of float"""
    return sum(mxd_lst)
