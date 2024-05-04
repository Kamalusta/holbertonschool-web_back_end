#!/usr/bin/env python3
""" dioc"""


import asyncio
import random


async def async_generator():
    """doc"""
    for _ in range(10):
        await asyncio.sleep(1)
        nbr = random.uniform(0, 10)
        yield nbr
