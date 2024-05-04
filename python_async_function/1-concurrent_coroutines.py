#!/usr/bin/env python3
""" return the list of all the delays """


import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    results = await asyncio.gather(*delays)
    return sorted(results)
