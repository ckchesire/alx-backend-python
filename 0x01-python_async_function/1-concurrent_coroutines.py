#!/usr/bin/env python3
"""Module to define an async routine to run multiple wait_random coroutines
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function to spawn wait_random n times with the specified max_delay
       and collect days.

       Args:
           n (int): Number of times to call wait_random.
           max_delay (int): Maximum possible delay value for each wait_random.

       Returns:
           List[float]: List of delays in ascending order.
    """
    delays: List[float]= []
    for _ in range(n):
        delay = await wait_random(max_delay)
        i = 0
        while i < len(delays) and delays[i] < delay:
            i += 1
        delays.insert(i, delay)
    return delays
