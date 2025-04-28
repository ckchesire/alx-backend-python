#!/usr/bin/env python3
"""Module to run task_await_random multiple times and return sorted delays.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Method to execute task_wait_random n times and return sorted delays list

       Args:
          n (int): No. of times to call task_wait_random.
          max_delay (int): Maximum delay for each call.

       Returns:
          List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
