#!/usr/bin/env python3
""" basic async syntax """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ using basic async - await coroutines """
    rannum: float = random.uniform(0.0, max_delay)
    await asyncio.sleep(rannum)
    return rannum
