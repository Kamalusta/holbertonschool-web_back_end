#!/usr/bin/env python3
"""doc"""


from basic_async_syntax import wait_random
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of floats representing random delays.
    delays = []
    coroutines = [wait_random(max_delay) for _ in range(n)]

    for future in asyncio.as_completed(coroutines):
        delay = await future
        delays.append(delay)

    return delays"""

    delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    results = await asyncio.gather(*delays)
    return sorted(results)
