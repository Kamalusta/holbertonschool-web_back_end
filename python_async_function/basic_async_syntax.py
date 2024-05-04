#!/usr/bin/env python3
"""waits for a random delay """


from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay"""
    sec = uniform(0, max_delay)
    await asyncio.sleep(sec)
    return sec
