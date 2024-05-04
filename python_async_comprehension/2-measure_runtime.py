#!/usr/bin/env python3
"""measure the total runtime and return it"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> int:
    """measure the total runtime and return it"""
    start = time.perf_counter()
    delay = []
    for _ in range(4):
        delay.append(async_comprehension())
    await asyncio.gather(*delay)
    elapsed = time.perf_counter() - start
    return elapsed
