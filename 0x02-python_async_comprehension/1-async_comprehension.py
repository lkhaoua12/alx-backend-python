#!/usr/bin/env python3
"""  a coroutine called async_generator that takes no arguments """
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """  a coroutine called async_generator that takes no arguments """
    call_list = [random async for random in async_generator()]
    return call_list
