#!/usr/bin/env python3
""" Creating a task routine """
import asyncio


def task_wait_random(max_delay: int):
    """ Create an asyncio Task """
    wait_random = __import__('0-basic_async_syntax').wait_random
    task = asyncio.create_task(wait_random(max_delay))
    return task
