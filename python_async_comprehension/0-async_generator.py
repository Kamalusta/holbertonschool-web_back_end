#!/usr/bin/env python3
"""yield a random number"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """yield a random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        nbr = random.uniform(0, 10)
        yield nbr
