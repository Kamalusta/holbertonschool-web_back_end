#!/usr/bin/env python3
"""return the list of all random delays"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all random delays"""
    delays = []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))
    results = await asyncio.gather(*delays)
    return sorted(results)
