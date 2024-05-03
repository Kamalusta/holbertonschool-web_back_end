#!/usr/bin/env python3
"""doc"""


from random import uniform
import asyncio


async def wait_random(max_delay: int = 10):
    sec = uniform(0, max_delay)
    await asyncio.sleep(sec)
    return sec
