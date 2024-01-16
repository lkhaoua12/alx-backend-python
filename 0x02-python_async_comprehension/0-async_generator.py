#!/usr/bin/env python3
"""  a coroutine called async_generator that takes no arguments """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """ a coroutine called async_generator that takes no arguments """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
